# file: lib/ansible/cli/console.py:183-256
# asked: {"lines": [183, 185, 186, 188, 189, 190, 192, 193, 194, 196, 197, 199, 200, 201, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 222, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 240, 242, 243, 244, 245, 247, 248, 249, 250, 251, 252, 253, 254, 256], "branches": [[185, 186], [185, 188], [188, 189], [188, 192], [192, 193], [192, 196], [199, 200], [199, 203], [242, 243], [242, 244], [244, 245], [244, 247], [247, 0], [247, 248]]}
# gained: {"lines": [183, 185, 188, 189, 190, 192, 193, 194, 196, 197, 199, 200, 201, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 222, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 240, 242, 243, 244, 245, 247, 248, 249, 250, 251, 252, 253, 254, 256], "branches": [[185, 188], [188, 189], [188, 192], [192, 193], [192, 196], [199, 200], [199, 203], [242, 243], [244, 245], [247, 0], [247, 248]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.console import ConsoleCLI
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.module_utils._text import to_text
from ansible.parsing.splitter import parse_kv
from ansible.playbook.play import Play

@pytest.fixture
def console_cli():
    cli = ConsoleCLI(args=['test'])
    cli.cwd = 'localhost'
    cli.modules = ['ping', 'shell']
    cli.task_timeout = 10
    cli.remote_user = 'user'
    cli.become = False
    cli.become_user = None
    cli.become_method = None
    cli.check_mode = False
    cli.diff = False
    cli.inventory = MagicMock()
    cli.variable_manager = MagicMock()
    cli.loader = MagicMock()
    cli.passwords = MagicMock()
    cli.forks = 5
    return cli

def test_default_no_host_found(console_cli, mocker):
    console_cli.cwd = None
    mock_display = mocker.patch('ansible.cli.console.display')
    result = console_cli.default('ping')
    mock_display.error.assert_called_once_with('No host found')
    assert result is False

def test_default_module_not_found(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display')
    result = console_cli.default('nonexistent_module')
    assert result is not False

def test_default_forceshell(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display')
    result = console_cli.default('ping', forceshell=True)
    assert result is not False

def test_default_exception_build_command(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display')
    mocker.patch('ansible.playbook.play.Play.load', side_effect=Exception('test exception'))
    result = console_cli.default('ping')
    mock_display.error.assert_called_once_with('Unable to build command: test exception')
    assert result is False

def test_default_keyboard_interrupt(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display')
    mocker.patch.object(TaskQueueManager, 'run', side_effect=KeyboardInterrupt)
    result = console_cli.default('ping')
    mock_display.error.assert_called_once_with('User interrupted execution')
    assert result is False

def test_default_exception_run(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display')
    mocker.patch.object(TaskQueueManager, 'run', side_effect=Exception('run exception'))
    result = console_cli.default('ping')
    mock_display.error.assert_called_once_with('run exception')
    assert result is False

def test_default_no_hosts_found(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display')
    mocker.patch.object(TaskQueueManager, 'run', return_value=None)
    result = console_cli.default('ping')
    mock_display.error.assert_called_once_with('No hosts found')
    assert result is False

def test_default_successful_run(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display')
    mocker.patch.object(TaskQueueManager, 'run', return_value=0)
    result = console_cli.default('ping')
    assert result is not False
