# file: lib/ansible/plugins/action/reboot.py:323-350
# asked: {"lines": [324, 325, 326, 327, 328, 330, 331, 332, 333, 334, 336, 337, 339, 341, 342, 343, 344, 345, 346, 347, 349, 350], "branches": [[341, 342], [341, 349]]}
# gained: {"lines": [324, 325, 326, 327, 328, 330, 331, 332, 333, 334, 336, 337, 339, 341, 342, 343, 344, 345, 346, 347, 349, 350], "branches": [[341, 342], [341, 349]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule
from ansible.errors import AnsibleConnectionFailure
from datetime import datetime

@pytest.fixture
def action_module():
    task = MagicMock()
    task.action = 'reboot'
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_perform_reboot_success(action_module, monkeypatch):
    task_vars = {}
    distribution = 'linux'
    
    def mock_get_shutdown_command(task_vars, distribution):
        return 'shutdown'
    
    def mock_get_shutdown_command_args(distribution):
        return '-r now'
    
    def mock_low_level_execute_command(command, sudoable):
        return {'rc': 0, 'stdout': 'Rebooting', 'stderr': ''}
    
    monkeypatch.setattr(action_module, 'get_shutdown_command', mock_get_shutdown_command)
    monkeypatch.setattr(action_module, 'get_shutdown_command_args', mock_get_shutdown_command_args)
    monkeypatch.setattr(action_module, '_low_level_execute_command', mock_low_level_execute_command)
    
    result = action_module.perform_reboot(task_vars, distribution)
    
    assert result['failed'] is False
    assert 'start' in result

def test_perform_reboot_failure(action_module, monkeypatch):
    task_vars = {}
    distribution = 'linux'
    
    def mock_get_shutdown_command(task_vars, distribution):
        return 'shutdown'
    
    def mock_get_shutdown_command_args(distribution):
        return '-r now'
    
    def mock_low_level_execute_command(command, sudoable):
        return {'rc': 1, 'stdout': 'Error', 'stderr': 'Failed to reboot'}
    
    monkeypatch.setattr(action_module, 'get_shutdown_command', mock_get_shutdown_command)
    monkeypatch.setattr(action_module, 'get_shutdown_command_args', mock_get_shutdown_command_args)
    monkeypatch.setattr(action_module, '_low_level_execute_command', mock_low_level_execute_command)
    
    result = action_module.perform_reboot(task_vars, distribution)
    
    assert result['failed'] is True
    assert result['rebooted'] is False
    assert result['msg'] == "Reboot command failed. Error was: 'Error, Failed to reboot'"
    assert 'start' in result

def test_perform_reboot_connection_failure(action_module, monkeypatch):
    task_vars = {}
    distribution = 'linux'
    
    def mock_get_shutdown_command(task_vars, distribution):
        return 'shutdown'
    
    def mock_get_shutdown_command_args(distribution):
        return '-r now'
    
    def mock_low_level_execute_command(command, sudoable):
        raise AnsibleConnectionFailure('Connection lost')
    
    monkeypatch.setattr(action_module, 'get_shutdown_command', mock_get_shutdown_command)
    monkeypatch.setattr(action_module, 'get_shutdown_command_args', mock_get_shutdown_command_args)
    monkeypatch.setattr(action_module, '_low_level_execute_command', mock_low_level_execute_command)
    
    result = action_module.perform_reboot(task_vars, distribution)
    
    assert result['failed'] is False
    assert 'start' in result
