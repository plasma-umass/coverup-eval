# file lib/ansible/plugins/action/reboot.py:323-350
# lines [323, 324, 325, 326, 327, 328, 330, 331, 332, 333, 334, 336, 337, 339, 341, 342, 343, 344, 345, 346, 347, 349, 350]
# branches ['341->342', '341->349']

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.action.reboot import ActionModule
from ansible.errors import AnsibleConnectionFailure
from datetime import datetime

@pytest.fixture
def mock_task():
    return MagicMock()

@pytest.fixture
def mock_task_vars():
    return {'ansible_distribution': 'Ubuntu'}

@pytest.fixture
def action_module(mock_task):
    return ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_perform_reboot_success(action_module, mock_task_vars):
    with patch.object(action_module, 'get_shutdown_command', return_value='shutdown') as mock_get_shutdown_command, \
         patch.object(action_module, 'get_shutdown_command_args', return_value='-r now') as mock_get_shutdown_command_args, \
         patch.object(action_module, '_low_level_execute_command', return_value={'rc': 0, 'stdout': '', 'stderr': ''}) as mock_execute_command, \
         patch('ansible.plugins.action.reboot.display') as mock_display:
        
        result = action_module.perform_reboot(mock_task_vars, 'Ubuntu')
        
        mock_get_shutdown_command.assert_called_once_with(mock_task_vars, 'Ubuntu')
        mock_get_shutdown_command_args.assert_called_once_with('Ubuntu')
        mock_execute_command.assert_called_once_with('shutdown -r now', sudoable=action_module.DEFAULT_SUDOABLE)
        
        assert result['failed'] is False
        assert 'start' in result

def test_perform_reboot_failure(action_module, mock_task_vars):
    with patch.object(action_module, 'get_shutdown_command', return_value='shutdown') as mock_get_shutdown_command, \
         patch.object(action_module, 'get_shutdown_command_args', return_value='-r now') as mock_get_shutdown_command_args, \
         patch.object(action_module, '_low_level_execute_command', return_value={'rc': 1, 'stdout': 'error', 'stderr': 'failure'}) as mock_execute_command, \
         patch('ansible.plugins.action.reboot.display') as mock_display:
        
        result = action_module.perform_reboot(mock_task_vars, 'Ubuntu')
        
        mock_get_shutdown_command.assert_called_once_with(mock_task_vars, 'Ubuntu')
        mock_get_shutdown_command_args.assert_called_once_with('Ubuntu')
        mock_execute_command.assert_called_once_with('shutdown -r now', sudoable=action_module.DEFAULT_SUDOABLE)
        
        assert result['failed'] is True
        assert result['rebooted'] is False
        assert result['msg'] == "Reboot command failed. Error was: 'error, failure'"
        assert 'start' in result

def test_perform_reboot_connection_failure(action_module, mock_task_vars):
    with patch.object(action_module, 'get_shutdown_command', return_value='shutdown') as mock_get_shutdown_command, \
         patch.object(action_module, 'get_shutdown_command_args', return_value='-r now') as mock_get_shutdown_command_args, \
         patch.object(action_module, '_low_level_execute_command', side_effect=AnsibleConnectionFailure('connection lost')) as mock_execute_command, \
         patch('ansible.plugins.action.reboot.display') as mock_display:
        
        result = action_module.perform_reboot(mock_task_vars, 'Ubuntu')
        
        mock_get_shutdown_command.assert_called_once_with(mock_task_vars, 'Ubuntu')
        mock_get_shutdown_command_args.assert_called_once_with('Ubuntu')
        mock_execute_command.assert_called_once_with('shutdown -r now', sudoable=action_module.DEFAULT_SUDOABLE)
        
        assert result['failed'] is False
        assert 'start' in result
