# file: lib/ansible/plugins/action/reboot.py:211-233
# asked: {"lines": [211, 212, 213, 214, 216, 217, 218, 219, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233], "branches": [[213, 214], [213, 221], [224, 225], [224, 232]]}
# gained: {"lines": [211, 212, 213, 214, 216, 217, 218, 219, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233], "branches": [[213, 214], [213, 221], [224, 225], [224, 232]]}

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
    distribution = {'name': 'Ubuntu', 'version': '20.04', 'family': 'Debian'}
    action_module._get_value_from_facts = MagicMock(return_value='uptime -s')
    action_module._low_level_execute_command = MagicMock(return_value={'rc': 0, 'stdout': '2023-01-01 00:00:00', 'stderr': ''})

    boot_time = action_module.get_system_boot_time(distribution)

    action_module._get_value_from_facts.assert_called_once_with('BOOT_TIME_COMMANDS', distribution, 'DEFAULT_BOOT_TIME_COMMAND')
    action_module._low_level_execute_command.assert_called_once_with('uptime -s', sudoable=action_module.DEFAULT_SUDOABLE)
    assert boot_time == '2023-01-01 00:00:00'

def test_get_system_boot_time_custom_command(action_module):
    distribution = {'name': 'Ubuntu', 'version': '20.04', 'family': 'Debian'}
    action_module._task.args['boot_time_command'] = 'who -b'
    action_module._low_level_execute_command = MagicMock(return_value={'rc': 0, 'stdout': '2023-01-01 00:00:00', 'stderr': ''})

    boot_time = action_module.get_system_boot_time(distribution)

    action_module._low_level_execute_command.assert_called_once_with('who -b', sudoable=action_module.DEFAULT_SUDOABLE)
    assert boot_time == '2023-01-01 00:00:00'

def test_get_system_boot_time_invalid_command(action_module):
    distribution = {'name': 'Ubuntu', 'version': '20.04', 'family': 'Debian'}
    action_module._task.args['boot_time_command'] = 123  # Invalid type

    with pytest.raises(AnsibleError, match="Invalid value given for 'boot_time_command'"):
        action_module.get_system_boot_time(distribution)

def test_get_system_boot_time_command_failure(action_module):
    distribution = {'name': 'Ubuntu', 'version': '20.04', 'family': 'Debian'}
    action_module._get_value_from_facts = MagicMock(return_value='uptime -s')
    action_module._low_level_execute_command = MagicMock(return_value={'rc': 1, 'stdout': '', 'stderr': 'error'})

    with pytest.raises(AnsibleError, match="failed to get host boot time info"):
        action_module.get_system_boot_time(distribution)
