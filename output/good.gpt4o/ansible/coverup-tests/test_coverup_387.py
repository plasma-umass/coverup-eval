# file lib/ansible/cli/console.py:135-145
# lines [135, 136, 137, 138, 139, 140, 141, 143, 144, 145]
# branches ['139->140', '139->143']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible import constants as C
import getpass
from ansible.utils.color import stringc

@pytest.fixture
def mock_inventory():
    inventory = mock.Mock()
    inventory.list_hosts.return_value = ['host1', 'host2']
    return inventory

@pytest.fixture
def console_cli(mock_inventory):
    args = mock.Mock()
    cli = ConsoleCLI(args)
    cli.remote_user = None
    cli.cwd = 'test_cwd'
    cli.forks = 5
    cli.inventory = mock_inventory
    cli.become = False
    cli.become_user = None
    cli.NORMAL_PROMPT = 'normal_prompt_color'
    return cli

def test_set_prompt_no_become(console_cli, mocker):
    mocker.patch('getpass.getuser', return_value='test_user')
    console_cli.set_prompt()
    expected_prompt = stringc("test_user@test_cwd (2)[f:5]$ ", 'normal_prompt_color', wrap_nonvisible_chars=True)
    assert console_cli.prompt == expected_prompt

def test_set_prompt_become_root(console_cli, mocker):
    mocker.patch('getpass.getuser', return_value='test_user')
    console_cli.become = True
    console_cli.become_user = 'root'
    console_cli.set_prompt()
    expected_prompt = stringc("test_user@test_cwd (2)[f:5]# ", C.COLOR_ERROR, wrap_nonvisible_chars=True)
    assert console_cli.prompt == expected_prompt

def test_set_prompt_become_non_root(console_cli, mocker):
    mocker.patch('getpass.getuser', return_value='test_user')
    console_cli.become = True
    console_cli.become_user = 'non_root_user'
    console_cli.set_prompt()
    expected_prompt = stringc("test_user@test_cwd (2)[f:5]$ ", 'normal_prompt_color', wrap_nonvisible_chars=True)
    assert console_cli.prompt == expected_prompt
