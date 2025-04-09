# file: lib/ansible/cli/console.py:135-145
# asked: {"lines": [135, 136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[139, 140], [139, 143]]}
# gained: {"lines": [135, 136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[139, 140], [139, 143]]}

import pytest
import getpass
from unittest.mock import MagicMock, patch
from ansible.cli.console import ConsoleCLI
from ansible import constants as C
from ansible.utils.color import stringc

@pytest.fixture
def console_cli():
    args = MagicMock()
    cli = ConsoleCLI(args)
    cli.inventory = MagicMock()
    cli.inventory.list_hosts = MagicMock(return_value=['host1', 'host2'])
    return cli

def test_set_prompt_normal_user(console_cli):
    console_cli.remote_user = None
    console_cli.cwd = 'test_cwd'
    console_cli.forks = 5
    console_cli.become = False
    console_cli.NORMAL_PROMPT = 'normal_color'

    with patch('getpass.getuser', return_value='test_user'):
        console_cli.set_prompt()

    assert console_cli.prompt == stringc('test_user@test_cwd (2)[f:5]$ ', 'normal_color', wrap_nonvisible_chars=True)

def test_set_prompt_become_root(console_cli):
    console_cli.remote_user = 'admin'
    console_cli.cwd = 'test_cwd'
    console_cli.forks = 5
    console_cli.become = True
    console_cli.become_user = 'root'

    console_cli.set_prompt()

    assert console_cli.prompt == stringc('admin@test_cwd (2)[f:5]# ', C.COLOR_ERROR, wrap_nonvisible_chars=True)

def test_set_prompt_become_non_root(console_cli):
    console_cli.remote_user = 'admin'
    console_cli.cwd = 'test_cwd'
    console_cli.forks = 5
    console_cli.become = True
    console_cli.become_user = 'non_root'
    console_cli.NORMAL_PROMPT = 'normal_color'

    console_cli.set_prompt()

    assert console_cli.prompt == stringc('admin@test_cwd (2)[f:5]$ ', 'normal_color', wrap_nonvisible_chars=True)
