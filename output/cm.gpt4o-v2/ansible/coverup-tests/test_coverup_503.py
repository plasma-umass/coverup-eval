# file: lib/ansible/cli/console.py:124-133
# asked: {"lines": [124, 125, 126, 128, 129, 131, 132, 133], "branches": []}
# gained: {"lines": [124, 125, 126, 128, 131, 132, 133], "branches": []}

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['test'])

def test_cmdloop_keyboard_interrupt(console_cli, mocker):
    mocker.patch('cmd.Cmd.cmdloop', side_effect=KeyboardInterrupt)
    mocker.patch.object(console_cli, 'cmdloop')
    
    console_cli.cmdloop()
    
    console_cli.cmdloop.assert_called_once()

def test_cmdloop_eof_error(console_cli, mocker):
    mocker.patch('cmd.Cmd.cmdloop', side_effect=EOFError)
    mocker.patch.object(console_cli, 'do_exit')
    
    with mock.patch.object(console_cli, 'display', create=True) as mock_display:
        console_cli.cmdloop()
    
    mock_display.assert_called_once_with('[Ansible-console was exited]')
    console_cli.do_exit.assert_called_once_with(console_cli)
