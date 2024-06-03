# file lib/ansible/plugins/action/reboot.py:158-201
# lines [167, 170]
# branches ['160->167', '169->170']

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule
from ansible.plugins.action import ActionBase

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {}
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

@pytest.fixture
def task_vars():
    return {
        'ansible_facts': {
            'SHUTDOWN_COMMANDS': {
                'default': '/sbin/shutdown'
            }
        }
    }

def test_get_shutdown_command_no_reboot_command(action_module, task_vars):
    distribution = 'default'
    with patch.object(action_module, '_get_value_from_facts', return_value='/sbin/shutdown') as mock_get_value_from_facts:
        result = action_module.get_shutdown_command(task_vars, distribution)
        mock_get_value_from_facts.assert_called_once_with('SHUTDOWN_COMMANDS', distribution, 'DEFAULT_SHUTDOWN_COMMAND')
        assert result == '/sbin/shutdown'

def test_get_shutdown_command_no_reboot_command_relative_path(action_module, task_vars):
    distribution = 'default'
    with patch.object(action_module, '_get_value_from_facts', return_value='shutdown') as mock_get_value_from_facts, \
         patch.object(action_module, '_execute_module', return_value={'files': [{'path': '/sbin/shutdown'}]}) as mock_execute_module:
        result = action_module.get_shutdown_command(task_vars, distribution)
        mock_get_value_from_facts.assert_called_once_with('SHUTDOWN_COMMANDS', distribution, 'DEFAULT_SHUTDOWN_COMMAND')
        mock_execute_module.assert_called_once()
        assert result == '/sbin/shutdown'
