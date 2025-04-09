# file: lib/ansible/plugins/action/reboot.py:211-233
# asked: {"lines": [212, 213, 214, 216, 217, 218, 219, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233], "branches": [[213, 214], [213, 221], [224, 225], [224, 232]]}
# gained: {"lines": [212, 213, 214, 216, 217, 218, 219, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233], "branches": [[213, 214], [213, 221], [224, 225], [224, 232]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule
from unittest.mock import MagicMock, patch

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

def test_get_system_boot_time_default_command(action_module):
    action_module._get_value_from_facts = MagicMock(return_value="default_boot_time_command")
    action_module._low_level_execute_command = MagicMock(return_value={'rc': 0, 'stdout': 'boot_time', 'stderr': ''})
    
    result = action_module.get_system_boot_time({'name': 'TestOS', 'version': '1.0', 'family': 'TestFamily'})
    
    action_module._get_value_from_facts.assert_called_once_with('BOOT_TIME_COMMANDS', {'name': 'TestOS', 'version': '1.0', 'family': 'TestFamily'}, 'DEFAULT_BOOT_TIME_COMMAND')
    action_module._low_level_execute_command.assert_called_once_with('default_boot_time_command', sudoable=action_module.DEFAULT_SUDOABLE)
    assert result == 'boot_time'

def test_get_system_boot_time_custom_command(action_module):
    action_module._task.args['boot_time_command'] = 'custom_boot_time_command'
    action_module._low_level_execute_command = MagicMock(return_value={'rc': 0, 'stdout': 'boot_time', 'stderr': ''})
    
    result = action_module.get_system_boot_time({'name': 'TestOS', 'version': '1.0', 'family': 'TestFamily'})
    
    action_module._low_level_execute_command.assert_called_once_with('custom_boot_time_command', sudoable=action_module.DEFAULT_SUDOABLE)
    assert result == 'boot_time'

def test_get_system_boot_time_invalid_command(action_module):
    action_module._task.args['boot_time_command'] = 123  # Invalid type to trigger TypeError
    
    with pytest.raises(AnsibleError, match="Invalid value given for 'boot_time_command'"):
        action_module.get_system_boot_time({'name': 'TestOS', 'version': '1.0', 'family': 'TestFamily'})

def test_get_system_boot_time_command_failure(action_module):
    action_module._get_value_from_facts = MagicMock(return_value="default_boot_time_command")
    action_module._low_level_execute_command = MagicMock(return_value={'rc': 1, 'stdout': 'error_output', 'stderr': 'error_message'})
    
    with pytest.raises(AnsibleError, match="failed to get host boot time info"):
        action_module.get_system_boot_time({'name': 'TestOS', 'version': '1.0', 'family': 'TestFamily'})
