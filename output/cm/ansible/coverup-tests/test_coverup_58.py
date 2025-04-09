# file lib/ansible/plugins/action/reboot.py:158-201
# lines [158, 159, 160, 161, 162, 163, 164, 165, 167, 169, 170, 172, 173, 175, 177, 178, 179, 180, 182, 183, 184, 185, 187, 188, 190, 191, 192, 193, 194, 198, 199, 200, 201]
# branches ['160->161', '160->167', '169->170', '169->172', '199->200', '199->201']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'debug')

# Mock the _execute_module method to simulate find module behavior
@pytest.fixture
def mock_execute_module(mocker):
    def execute_module_side_effect(*args, **kwargs):
        module_args = kwargs.get('module_args', {})
        paths = module_args.get('paths', [])
        patterns = module_args.get('patterns', [])
        # Simulate find module result
        if '/sbin' in paths and 'shutdown' in patterns:
            return {'files': [{'path': '/sbin/shutdown'}]}
        else:
            return {'files': []}
    return mocker.patch.object(ActionModule, '_execute_module', side_effect=execute_module_side_effect)

# Mock the _get_value_from_facts method to return a default shutdown command
@pytest.fixture
def mock_get_value_from_facts(mocker):
    return mocker.patch.object(ActionModule, '_get_value_from_facts', return_value='shutdown')

# Test function to cover missing lines/branches
def test_get_shutdown_command_with_custom_search_paths(mock_display, mock_execute_module, mock_get_value_from_facts, mocker):
    fake_task = MagicMock()
    fake_task.args = {}
    action_module = ActionModule(fake_task, None, None, None, None, None)
    task_vars = {}
    distribution = 'SomeOS'

    # Test with custom reboot_command
    custom_reboot_command = '/custom/sbin/reboot'
    action_module._task.args = {'reboot_command': custom_reboot_command}
    assert action_module.get_shutdown_command(task_vars, distribution) == custom_reboot_command

    # Test with custom search_paths and no reboot_command
    action_module._task.args = {'search_paths': ['/custom/sbin']}
    with pytest.raises(AnsibleError) as excinfo:
        action_module.get_shutdown_command(task_vars, distribution)
    assert 'Unable to find command "shutdown" in search paths: ' in str(excinfo.value)

    # Test with invalid search_paths type
    action_module._task.args = {'search_paths': {'invalid': 'type'}}
    with pytest.raises(AnsibleError) as excinfo:
        action_module.get_shutdown_command(task_vars, distribution)
    assert "'search_paths' must be a string or flat list of strings, got " in str(excinfo.value)

    # Test with valid search_paths and find module finding the command
    action_module._task.args = {'search_paths': ['/sbin']}
    assert action_module.get_shutdown_command(task_vars, distribution) == '/sbin/shutdown'
