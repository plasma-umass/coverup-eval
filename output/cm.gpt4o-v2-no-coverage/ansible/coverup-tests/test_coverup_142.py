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
    task = MagicMock()
    task.args = {
        'reboot_command': None,
        'msg': 'Rebooting now'
    }
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_perform_reboot_success(action_module):
    task_vars = {}
    distribution = 'Linux'
    
    with patch.object(action_module, 'get_shutdown_command', return_value='/sbin/shutdown'), \
         patch.object(action_module, 'get_shutdown_command_args', return_value='-r now'), \
         patch.object(action_module, '_low_level_execute_command', return_value={'rc': 0, 'stdout': 'Rebooting', 'stderr': ''}), \
         patch('ansible.plugins.action.reboot.datetime') as mock_datetime:
        
        mock_datetime.utcnow.return_value = datetime(2023, 1, 1)
        
        result = action_module.perform_reboot(task_vars, distribution)
        
        assert result['failed'] is False
        assert result['start'] == datetime(2023, 1, 1)

def test_perform_reboot_failure(action_module):
    task_vars = {}
    distribution = 'Linux'
    
    with patch.object(action_module, 'get_shutdown_command', return_value='/sbin/shutdown'), \
         patch.object(action_module, 'get_shutdown_command_args', return_value='-r now'), \
         patch.object(action_module, '_low_level_execute_command', return_value={'rc': 1, 'stdout': 'Error', 'stderr': 'Failed'}), \
         patch('ansible.plugins.action.reboot.datetime') as mock_datetime:
        
        mock_datetime.utcnow.return_value = datetime(2023, 1, 1)
        
        result = action_module.perform_reboot(task_vars, distribution)
        
        assert result['failed'] is True
        assert result['rebooted'] is False
        assert result['msg'] == "Reboot command failed. Error was: 'Error, Failed'"
        assert result['start'] == datetime(2023, 1, 1)

def test_perform_reboot_connection_failure(action_module):
    task_vars = {}
    distribution = 'Linux'
    
    with patch.object(action_module, 'get_shutdown_command', return_value='/sbin/shutdown'), \
         patch.object(action_module, 'get_shutdown_command_args', return_value='-r now'), \
         patch.object(action_module, '_low_level_execute_command', side_effect=AnsibleConnectionFailure('Connection lost')), \
         patch('ansible.plugins.action.reboot.datetime') as mock_datetime:
        
        mock_datetime.utcnow.return_value = datetime(2023, 1, 1)
        
        result = action_module.perform_reboot(task_vars, distribution)
        
        assert result['failed'] is False
        assert result['start'] == datetime(2023, 1, 1)
