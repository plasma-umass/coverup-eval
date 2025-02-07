# file: lib/ansible/cli/console.py:183-256
# asked: {"lines": [183, 185, 186, 188, 189, 190, 192, 193, 194, 196, 197, 199, 200, 201, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 222, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 240, 242, 243, 244, 245, 247, 248, 249, 250, 251, 252, 253, 254, 256], "branches": [[185, 186], [185, 188], [188, 189], [188, 192], [192, 193], [192, 196], [199, 200], [199, 203], [242, 243], [242, 244], [244, 245], [244, 247], [247, 0], [247, 248]]}
# gained: {"lines": [183, 185, 188, 189, 190, 192, 193, 194, 196, 197, 199, 200, 201, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 240, 242, 243, 244, 245, 247, 250, 251, 252, 253, 254, 256], "branches": [[185, 188], [188, 189], [188, 192], [192, 193], [192, 196], [199, 200], [199, 203], [242, 243], [244, 245], [247, 0]]}

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
    cli.passwords = {}
    cli.remote_user = 'test_user'
    cli.become = False
    cli.become_user = 'root'
    cli.become_method = 'sudo'
    cli.check_mode = False
    cli.diff = False
    cli.forks = 5
    cli.task_timeout = 10
    cli.inventory = MagicMock()  # Add inventory attribute
    return cli

def test_default_no_host(console_cli):
    console_cli.cwd = None
    with patch('ansible.cli.console.display') as mock_display:
        result = console_cli.default('ping')
        mock_display.error.assert_called_with('No host found')
        assert result is False

def test_default_module_not_found(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        result = console_cli.default('nonexistent_module')
        assert result is None  # Ensure the function runs to completion

def test_default_forceshell(console_cli):
    with patch('ansible.cli.console.TaskQueueManager') as mock_tqm:
        mock_tqm_instance = mock_tqm.return_value
        mock_tqm_instance.run.return_value = 0
        result = console_cli.default('echo hello', forceshell=True)
        assert result is None
        mock_tqm_instance.run.assert_called_once()

def test_default_keyboard_interrupt(console_cli):
    with patch('ansible.cli.console.TaskQueueManager') as mock_tqm, \
         patch('ansible.cli.console.display') as mock_display:
        mock_tqm_instance = mock_tqm.return_value
        mock_tqm_instance.run.side_effect = KeyboardInterrupt
        result = console_cli.default('ping')
        mock_display.error.assert_called_with('User interrupted execution')
        assert result is False

def test_default_exception(console_cli):
    with patch('ansible.cli.console.TaskQueueManager') as mock_tqm, \
         patch('ansible.cli.console.display') as mock_display:
        mock_tqm_instance = mock_tqm.return_value
        mock_tqm_instance.run.side_effect = Exception('Test exception')
        result = console_cli.default('ping')
        mock_display.error.assert_called_with('Test exception')
        assert result is False
