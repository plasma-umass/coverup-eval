# file: lib/ansible/cli/console.py:331-338
# asked: {"lines": [331, 333, 334, 335, 336, 338], "branches": [[333, 334], [333, 338]]}
# gained: {"lines": [331, 333, 334, 335, 336, 338], "branches": [[333, 334], [333, 338]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI
from ansible.module_utils.parsing.convert_bool import boolean
from ansible.utils.display import Display

display = Display()

@pytest.fixture
def console_cli():
    cli = ConsoleCLI(args=['test'])
    cli.remote_user = 'test_user'
    cli.cwd = 'test_cwd'
    cli.forks = 1
    cli.inventory = MagicMock()
    cli.inventory.list_hosts.return_value = ['host1', 'host2']
    return cli

def test_do_become_with_arg(console_cli, mocker):
    mocker.patch.object(display, 'v')
    mocker.patch.object(ConsoleCLI, 'set_prompt')
    
    console_cli.do_become('yes')
    
    assert console_cli.become is True
    display.v.assert_called_once_with("become changed to True")
    console_cli.set_prompt.assert_called_once()

def test_do_become_without_arg(console_cli, mocker):
    mocker.patch.object(display, 'display')
    
    console_cli.do_become('')
    
    display.display.assert_called_once_with("Please specify become value, e.g. `become yes`")
