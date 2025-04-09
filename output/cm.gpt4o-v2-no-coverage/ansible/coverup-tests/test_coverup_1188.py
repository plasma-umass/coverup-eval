# file: lib/ansible/cli/console.py:183-256
# asked: {"lines": [186], "branches": [[185, 186], [242, 244], [244, 247]]}
# gained: {"lines": [186], "branches": [[185, 186]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    args = MagicMock()
    cli = ConsoleCLI(args)
    cli.cwd = 'localhost'
    cli.modules = ['ping', 'shell']
    cli.variable_manager = MagicMock()
    cli.loader = MagicMock()
    cli.inventory = MagicMock()
    cli.passwords = MagicMock()
    cli.remote_user = 'user'
    cli.become = False
    cli.become_user = 'root'
    cli.become_method = 'sudo'
    cli.check_mode = False
    cli.diff = False
    cli.forks = 5
    cli.task_timeout = 10
    return cli

def test_default_with_comment(console_cli):
    result = console_cli.default("# This is a comment")
    assert result is False

def test_default_no_host_found(console_cli):
    console_cli.cwd = None
    with patch('ansible.cli.console.display') as mock_display:
        result = console_cli.default("ping")
        mock_display.error.assert_called_once_with("No host found")
        assert result is False

def test_default_module_in_modules(console_cli):
    with patch('ansible.cli.console.TaskQueueManager') as MockTQM, \
         patch('ansible.cli.console.display') as mock_display, \
         patch('ansible.cli.console.Play') as MockPlay, \
         patch('ansible.cli.console.parse_kv', return_value='parsed_args'):
        
        mock_tqm_instance = MockTQM.return_value
        mock_tqm_instance.run.return_value = 0
        mock_play_instance = MockPlay.return_value
        mock_play_instance.load.return_value = MagicMock()

        result = console_cli.default("ping arg1=val1 arg2=val2")
        
        MockPlay.assert_called_once()
        MockTQM.assert_called_once()
        mock_tqm_instance.run.assert_called_once()
        mock_tqm_instance.cleanup.assert_called_once()
        console_cli.loader.cleanup_all_tmp_files.assert_called_once()
        assert result is not False

def test_default_forceshell_true(console_cli):
    with patch('ansible.cli.console.TaskQueueManager') as MockTQM, \
         patch('ansible.cli.console.display') as mock_display, \
         patch('ansible.cli.console.Play') as MockPlay, \
         patch('ansible.cli.console.parse_kv', return_value='parsed_args'):
        
        mock_tqm_instance = MockTQM.return_value
        mock_tqm_instance.run.return_value = 0
        mock_play_instance = MockPlay.return_value
        mock_play_instance.load.return_value = MagicMock()

        result = console_cli.default("somecommand", forceshell=True)
        
        MockPlay.assert_called_once()
        MockTQM.assert_called_once()
        mock_tqm_instance.run.assert_called_once()
        mock_tqm_instance.cleanup.assert_called_once()
        console_cli.loader.cleanup_all_tmp_files.assert_called_once()
        assert result is not False

def test_default_unable_to_build_command(console_cli):
    with patch('ansible.cli.console.display') as mock_display, \
         patch('ansible.cli.console.Play.load', side_effect=Exception("Error")):
        
        result = console_cli.default("ping arg1=val1 arg2=val2")
        
        mock_display.error.assert_called_once_with("Unable to build command: Error")
        assert result is False

def test_default_keyboard_interrupt(console_cli):
    with patch('ansible.cli.console.TaskQueueManager') as MockTQM, \
         patch('ansible.cli.console.display') as mock_display:
        
        mock_tqm_instance = MockTQM.return_value
        mock_tqm_instance.run.side_effect = KeyboardInterrupt

        result = console_cli.default("ping arg1=val1 arg2=val2")
        
        mock_display.error.assert_called_once_with('User interrupted execution')
        assert result is False

def test_default_generic_exception(console_cli):
    with patch('ansible.cli.console.TaskQueueManager') as MockTQM, \
         patch('ansible.cli.console.display') as mock_display:
        
        mock_tqm_instance = MockTQM.return_value
        mock_tqm_instance.run.side_effect = Exception("Generic Error")

        result = console_cli.default("ping arg1=val1 arg2=val2")
        
        mock_display.error.assert_called_once_with("Generic Error")
        assert result is False
