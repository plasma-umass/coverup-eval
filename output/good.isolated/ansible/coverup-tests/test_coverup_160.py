# file lib/ansible/plugins/action/reboot.py:211-233
# lines [211, 212, 213, 214, 216, 217, 218, 219, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233]
# branches ['213->214', '213->221', '224->225', '224->232']

import pytest
from ansible.errors import AnsibleError
from ansible.utils.display import Display
from ansible.module_utils._text import to_native
from ansible.module_utils.common.validation import check_type_str
from ansible.plugins.action.reboot import ActionModule as RebootActionModule

# Mock the Display class to prevent actual printing
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'debug')

# Mock the _low_level_execute_command method to simulate command execution
@pytest.fixture
def mock_low_level_execute_command(mocker):
    return mocker.patch.object(RebootActionModule, '_low_level_execute_command')

# Mock the _get_value_from_facts method to return a default command
@pytest.fixture
def mock_get_value_from_facts(mocker):
    return mocker.patch.object(RebootActionModule, '_get_value_from_facts', return_value='uptime')

# Test function to cover the missing lines/branches
def test_get_system_boot_time_invalid_command(mocker, mock_display, mock_low_level_execute_command, mock_get_value_from_facts):
    action_module = RebootActionModule(None, None, None, None, None, None)
    action_module._task = mocker.MagicMock()
    action_module._task.action = 'reboot'
    action_module._task.args = {'boot_time_command': 123}  # Invalid command type

    with pytest.raises(AnsibleError) as excinfo:
        action_module.get_system_boot_time(distribution='Generic')

    assert "Invalid value given for 'boot_time_command'" in str(excinfo.value)

def test_get_system_boot_time_failed_command(mocker, mock_display, mock_low_level_execute_command, mock_get_value_from_facts):
    action_module = RebootActionModule(None, None, None, None, None, None)
    action_module._task = mocker.MagicMock()
    action_module._task.action = 'reboot'
    action_module._task.args = {'boot_time_command': 'fake_command'}

    # Simulate a failed command execution
    mock_low_level_execute_command.return_value = {'rc': 1, 'stdout': '', 'stderr': 'Command not found'}

    with pytest.raises(AnsibleError) as excinfo:
        action_module.get_system_boot_time(distribution='Generic')

    assert "failed to get host boot time info" in str(excinfo.value)
    assert "rc: 1" in str(excinfo.value)
    assert "stderr: Command not found" in str(excinfo.value)

def test_get_system_boot_time_successful_command(mocker, mock_display, mock_low_level_execute_command, mock_get_value_from_facts):
    action_module = RebootActionModule(None, None, None, None, None, None)
    action_module._task = mocker.MagicMock()
    action_module._task.action = 'reboot'
    action_module._task.args = {'boot_time_command': 'fake_command'}

    # Simulate a successful command execution
    mock_low_level_execute_command.return_value = {'rc': 0, 'stdout': 'Thu 01 Jan 1970 00:00:01 AM UTC', 'stderr': ''}

    boot_time = action_module.get_system_boot_time(distribution='Generic')

    assert boot_time == 'Thu 01 Jan 1970 00:00:01 AM UTC'
    mock_display.assert_called_with("reboot: last boot time: Thu 01 Jan 1970 00:00:01 AM UTC")
