# file lib/ansible/plugins/action/reboot.py:158-201
# lines [163, 164]
# branches []

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'debug')

# Mock the _execute_module method to prevent actual module execution
@pytest.fixture
def mock_execute_module(mocker):
    return mocker.patch.object(ActionModule, '_execute_module', return_value={'files': []})

# Mock the check_type_str method to raise a TypeError
@pytest.fixture
def mock_check_type_str(mocker):
    return mocker.patch('ansible.plugins.action.reboot.check_type_str', side_effect=TypeError('Mocked TypeError'))

def test_invalid_reboot_command_raises_ansible_error(mock_display, mock_execute_module, mock_check_type_str):
    fake_task = MagicMock()
    fake_task.args = {'reboot_command': 'invalid_command'}
    action_module = ActionModule(task=fake_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    with pytest.raises(AnsibleError) as excinfo:
        action_module.get_shutdown_command(task_vars={}, distribution='SomeOS')
    assert "Invalid value given for 'reboot_command'" in str(excinfo.value)
