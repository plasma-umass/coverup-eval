# file: lib/ansible/plugins/action/reboot.py:323-350
# asked: {"lines": [323, 324, 325, 326, 327, 328, 330, 331, 332, 333, 334, 336, 337, 339, 341, 342, 343, 344, 345, 346, 347, 349, 350], "branches": [[341, 342], [341, 349]]}
# gained: {"lines": [323, 324, 325, 326, 327, 328, 330, 331, 332, 333, 334, 336, 337, 339, 341, 342, 343, 344, 345, 346, 347, 349, 350], "branches": [[341, 342], [341, 349]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleConnectionFailure
from ansible.plugins.action.reboot import ActionModule
from datetime import datetime

@pytest.fixture
def action_module():
    return ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=MagicMock())

def test_perform_reboot_success(action_module, monkeypatch):
    task_vars = {}
    distribution = 'test_distribution'
    
    def mock_get_shutdown_command(task_vars, distribution):
        return '/sbin/shutdown'
    
    def mock_get_shutdown_command_args(distribution):
        return '-r now'
    
    def mock_low_level_execute_command(cmd, sudoable=True):
        return {'rc': 0, 'stdout': 'Rebooting', 'stderr': ''}
    
    monkeypatch.setattr(action_module, 'get_shutdown_command', mock_get_shutdown_command)
    monkeypatch.setattr(action_module, 'get_shutdown_command_args', mock_get_shutdown_command_args)
    monkeypatch.setattr(action_module, '_low_level_execute_command', mock_low_level_execute_command)
    
    result = action_module.perform_reboot(task_vars, distribution)
    
    assert result['failed'] is False
    assert 'start' in result

def test_perform_reboot_failure(action_module, monkeypatch):
    task_vars = {}
    distribution = 'test_distribution'
    
    def mock_get_shutdown_command(task_vars, distribution):
        return '/sbin/shutdown'
    
    def mock_get_shutdown_command_args(distribution):
        return '-r now'
    
    def mock_low_level_execute_command(cmd, sudoable=True):
        return {'rc': 1, 'stdout': 'Failed to reboot', 'stderr': 'Error'}
    
    monkeypatch.setattr(action_module, 'get_shutdown_command', mock_get_shutdown_command)
    monkeypatch.setattr(action_module, 'get_shutdown_command_args', mock_get_shutdown_command_args)
    monkeypatch.setattr(action_module, '_low_level_execute_command', mock_low_level_execute_command)
    
    result = action_module.perform_reboot(task_vars, distribution)
    
    assert result['failed'] is True
    assert result['rebooted'] is False
    assert "Reboot command failed" in result['msg']

def test_perform_reboot_connection_failure(action_module, monkeypatch):
    task_vars = {}
    distribution = 'test_distribution'
    
    def mock_get_shutdown_command(task_vars, distribution):
        return '/sbin/shutdown'
    
    def mock_get_shutdown_command_args(distribution):
        return '-r now'
    
    def mock_low_level_execute_command(cmd, sudoable=True):
        raise AnsibleConnectionFailure('Connection lost')
    
    monkeypatch.setattr(action_module, 'get_shutdown_command', mock_get_shutdown_command)
    monkeypatch.setattr(action_module, 'get_shutdown_command_args', mock_get_shutdown_command_args)
    monkeypatch.setattr(action_module, '_low_level_execute_command', mock_low_level_execute_command)
    
    result = action_module.perform_reboot(task_vars, distribution)
    
    assert result['failed'] is False
    assert 'start' in result
