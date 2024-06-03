# file lib/ansible/plugins/action/reboot.py:211-233
# lines [211, 212, 213, 214, 216, 217, 218, 219, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233]
# branches ['213->214', '213->221', '224->225', '224->232']

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {}
    task.action = 'reboot'
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_get_system_boot_time_default_command(action_module):
    with patch.object(action_module, '_get_value_from_facts', return_value='default_boot_time_command'), \
         patch.object(action_module, '_low_level_execute_command', return_value={'rc': 0, 'stdout': '2023-10-01 12:00:00', 'stderr': ''}), \
         patch('ansible.plugins.action.reboot.display') as mock_display:
        
        boot_time = action_module.get_system_boot_time({'name': 'some_distribution', 'version': '1.0', 'family': 'some_family'})
        assert boot_time == '2023-10-01 12:00:00'
        mock_display.debug.assert_any_call("reboot: getting boot time with command: 'default_boot_time_command'")
        mock_display.debug.assert_any_call("reboot: last boot time: 2023-10-01 12:00:00")

def test_get_system_boot_time_custom_command(action_module):
    action_module._task.args['boot_time_command'] = 'custom_boot_time_command'
    with patch.object(action_module, '_low_level_execute_command', return_value={'rc': 0, 'stdout': '2023-10-01 12:00:00', 'stderr': ''}), \
         patch('ansible.plugins.action.reboot.display') as mock_display:
        
        boot_time = action_module.get_system_boot_time({'name': 'some_distribution', 'version': '1.0', 'family': 'some_family'})
        assert boot_time == '2023-10-01 12:00:00'
        mock_display.debug.assert_any_call("reboot: getting boot time with command: 'custom_boot_time_command'")
        mock_display.debug.assert_any_call("reboot: last boot time: 2023-10-01 12:00:00")

def test_get_system_boot_time_invalid_command(action_module):
    action_module._task.args['boot_time_command'] = 12345  # Invalid type
    with pytest.raises(AnsibleError, match="Invalid value given for 'boot_time_command'"), \
         patch('ansible.plugins.action.reboot.check_type_str', side_effect=TypeError('Invalid type')), \
         patch('ansible.plugins.action.reboot.to_native', return_value='Invalid type'):
        
        action_module.get_system_boot_time({'name': 'some_distribution', 'version': '1.0', 'family': 'some_family'})

def test_get_system_boot_time_command_failure(action_module):
    with patch.object(action_module, '_get_value_from_facts', return_value='default_boot_time_command'), \
         patch.object(action_module, '_low_level_execute_command', return_value={'rc': 1, 'stdout': 'error output', 'stderr': 'error message'}), \
         patch('ansible.plugins.action.reboot.display') as mock_display, \
         patch('ansible.plugins.action.reboot.to_native', side_effect=lambda x: x):
        
        with pytest.raises(AnsibleError, match="failed to get host boot time info"):
            action_module.get_system_boot_time({'name': 'some_distribution', 'version': '1.0', 'family': 'some_family'})
        mock_display.debug.assert_any_call("reboot: getting boot time with command: 'default_boot_time_command'")
