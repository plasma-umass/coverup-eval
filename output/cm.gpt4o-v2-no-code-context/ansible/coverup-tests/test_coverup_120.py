# file: lib/ansible/plugins/action/reboot.py:211-233
# asked: {"lines": [211, 212, 213, 214, 216, 217, 218, 219, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233], "branches": [[213, 214], [213, 221], [224, 225], [224, 232]]}
# gained: {"lines": [211, 212, 213, 214, 216, 217, 218, 219, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233], "branches": [[213, 214], [213, 221], [224, 225], [224, 232]]}

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.errors import AnsibleError
from ansible.utils.display import Display
from ansible.module_utils._text import to_native

@pytest.fixture
def action_module(mocker):
    task = mocker.Mock()
    task.args = {}
    task.action = 'reboot'
    connection = mocker.Mock()
    play_context = mocker.Mock()
    loader = mocker.Mock()
    templar = mocker.Mock()
    shared_loader_obj = mocker.Mock()
    action_module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    return action_module

def test_get_system_boot_time_default_command(mocker, action_module):
    mocker.patch.object(action_module, '_get_value_from_facts', return_value='default_boot_time_command')
    mocker.patch.object(action_module, '_low_level_execute_command', return_value={'rc': 0, 'stdout': 'boot_time', 'stderr': ''})
    mocker.patch.object(Display, 'debug')

    result = action_module.get_system_boot_time({'name': 'some_distribution', 'version': '1.0', 'family': 'some_family'})
    assert result == 'boot_time'
    Display.debug.assert_any_call("reboot: getting boot time with command: 'default_boot_time_command'")
    Display.debug.assert_any_call("reboot: last boot time: boot_time")

def test_get_system_boot_time_custom_command(mocker, action_module):
    action_module._task.args['boot_time_command'] = 'custom_boot_time_command'
    mocker.patch.object(action_module, '_low_level_execute_command', return_value={'rc': 0, 'stdout': 'boot_time', 'stderr': ''})
    mocker.patch.object(Display, 'debug')

    result = action_module.get_system_boot_time({'name': 'some_distribution', 'version': '1.0', 'family': 'some_family'})
    assert result == 'boot_time'
    Display.debug.assert_any_call("reboot: getting boot time with command: 'custom_boot_time_command'")
    Display.debug.assert_any_call("reboot: last boot time: boot_time")

def test_get_system_boot_time_invalid_command(mocker, action_module):
    action_module._task.args['boot_time_command'] = 123  # Invalid type
    mocker.patch('ansible.plugins.action.reboot.check_type_str', side_effect=TypeError('Invalid type'))

    with pytest.raises(AnsibleError, match="Invalid value given for 'boot_time_command'"):
        action_module.get_system_boot_time({'name': 'some_distribution', 'version': '1.0', 'family': 'some_family'})

def test_get_system_boot_time_command_failure(mocker, action_module):
    mocker.patch.object(action_module, '_get_value_from_facts', return_value='default_boot_time_command')
    mocker.patch.object(action_module, '_low_level_execute_command', return_value={'rc': 1, 'stdout': 'error_output', 'stderr': 'error_message'})
    mocker.patch.object(Display, 'debug')

    with pytest.raises(AnsibleError, match="failed to get host boot time info"):
        action_module.get_system_boot_time({'name': 'some_distribution', 'version': '1.0', 'family': 'some_family'})
