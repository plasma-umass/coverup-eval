# file lib/ansible/plugins/action/reboot.py:211-233
# lines [212, 213, 214, 216, 217, 218, 219, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233]
# branches ['213->214', '213->221', '224->225', '224->232']

import pytest
from ansible.errors import AnsibleError
from ansible.utils.display import Display
from ansible.plugins.action.reboot import ActionModule
from ansible.module_utils.common.text.converters import to_native

# Mock the Display class to prevent actual printing
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'debug')

# Mock the ActionBase._low_level_execute_command method
@pytest.fixture
def mock_low_level_execute_command(mocker):
    return mocker.patch('ansible.plugins.action.ActionBase._low_level_execute_command')

# Test function to cover lines 212-233
def test_get_system_boot_time_failure(mock_display, mock_low_level_execute_command, mocker):
    fake_task = mocker.MagicMock()
    fake_task.args = {}
    action_module = ActionModule(fake_task, None, None, None, None, None)
    mocker.patch.object(action_module, '_get_value_from_facts', return_value='fake_boot_time_command')
    mock_low_level_execute_command.return_value = {
        'rc': 1,  # Simulate a command failure
        'stdout': 'fake_stdout',
        'stderr': 'fake_stderr'
    }

    with pytest.raises(AnsibleError) as excinfo:
        action_module.get_system_boot_time('fake_distribution')

    assert "failed to get host boot time info" in to_native(excinfo.value)
    mock_low_level_execute_command.assert_called_once_with('fake_boot_time_command', sudoable=ActionModule.DEFAULT_SUDOABLE)
    mock_display.assert_called()
