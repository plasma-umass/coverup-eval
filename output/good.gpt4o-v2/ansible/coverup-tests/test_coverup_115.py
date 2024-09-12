# file: lib/ansible/plugins/action/reboot.py:211-233
# asked: {"lines": [211, 212, 213, 214, 216, 217, 218, 219, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233], "branches": [[213, 214], [213, 221], [224, 225], [224, 232]]}
# gained: {"lines": [211, 212, 213, 214, 216, 217, 218, 219, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233], "branches": [[213, 214], [213, 221], [224, 225], [224, 232]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils.common.validation import check_type_str
from ansible.plugins.action.reboot import ActionModule

class MockTask:
    def __init__(self, args):
        self.args = args
        self.action = 'reboot'

class MockConnection:
    pass

class MockPlayContext:
    pass

class MockLoader:
    pass

class MockTemplar:
    pass

class MockSharedLoaderObj:
    pass

@pytest.fixture
def action_module():
    task = MockTask(args={})
    connection = MockConnection()
    play_context = MockPlayContext()
    loader = MockLoader()
    templar = MockTemplar()
    shared_loader_obj = MockSharedLoaderObj()
    module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    module.BOOT_TIME_COMMANDS = {
        'some_distribution': 'default_boot_time_command'
    }
    module.DEFAULT_BOOT_TIME_COMMAND = 'default_boot_time_command'
    return module

def test_get_system_boot_time_default_command(action_module, mocker):
    mocker.patch.object(action_module, '_get_value_from_facts', return_value='default_boot_time_command')
    mocker.patch.object(action_module, '_low_level_execute_command', return_value={'rc': 0, 'stdout': 'boot_time', 'stderr': ''})
    mocker.patch('ansible.plugins.action.reboot.display.debug')

    result = action_module.get_system_boot_time({'name': 'some_distribution', 'version': '', 'family': ''})
    assert result == 'boot_time'

def test_get_system_boot_time_custom_command(action_module, mocker):
    action_module._task.args['boot_time_command'] = 'custom_boot_time_command'
    mocker.patch.object(action_module, '_low_level_execute_command', return_value={'rc': 0, 'stdout': 'boot_time', 'stderr': ''})
    mocker.patch('ansible.plugins.action.reboot.display.debug')

    result = action_module.get_system_boot_time({'name': 'some_distribution', 'version': '', 'family': ''})
    assert result == 'boot_time'

def test_get_system_boot_time_invalid_command(action_module, mocker):
    action_module._task.args['boot_time_command'] = 123  # Invalid type
    mocker.patch('ansible.plugins.action.reboot.display.debug')

    with pytest.raises(AnsibleError, match="Invalid value given for 'boot_time_command'"):
        action_module.get_system_boot_time({'name': 'some_distribution', 'version': '', 'family': ''})

def test_get_system_boot_time_command_failure(action_module, mocker):
    mocker.patch.object(action_module, '_get_value_from_facts', return_value='default_boot_time_command')
    mocker.patch.object(action_module, '_low_level_execute_command', return_value={'rc': 1, 'stdout': 'error_output', 'stderr': 'error_message'})
    mocker.patch('ansible.plugins.action.reboot.display.debug')

    with pytest.raises(AnsibleError, match="failed to get host boot time info"):
        action_module.get_system_boot_time({'name': 'some_distribution', 'version': '', 'family': ''})
