# file lib/ansible/plugins/action/reboot.py:211-233
# lines [212, 213, 214, 216, 217, 218, 219, 221, 222, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233]
# branches ['213->214', '213->221', '224->225', '224->232']

import pytest
from ansible.errors import AnsibleError
from ansible.utils.display import Display
from ansible.plugins.action.reboot import ActionModule

# Mock the Display class to prevent actual printing
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'debug')

# Mock the ActionModule's _low_level_execute_command method
@pytest.fixture
def mock_low_level_execute_command(mocker):
    return mocker.patch.object(ActionModule, '_low_level_execute_command')

# Mock the ActionModule's _get_value_from_facts method
@pytest.fixture
def mock_get_value_from_facts(mocker):
    return mocker.patch.object(ActionModule, '_get_value_from_facts', return_value='fake_boot_time_command')

@pytest.fixture
def mock_task(mocker):
    task = mocker.MagicMock()
    task.args = {'boot_time_command': 'custom_boot_time_command'}
    return task

def test_get_system_boot_time_with_custom_command_and_failure(mock_display, mock_low_level_execute_command, mock_get_value_from_facts, mock_task):
    # Arrange
    action_module = ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    mock_low_level_execute_command.return_value = {
        'rc': 1,  # Simulate a command failure
        'stdout': 'fake_stdout',
        'stderr': 'fake_stderr'
    }

    # Act & Assert
    with pytest.raises(AnsibleError) as excinfo:
        action_module.get_system_boot_time(distribution='fake_distribution')
    
    # Verify that the error message contains the expected output
    assert "failed to get host boot time info" in str(excinfo.value)
    assert "rc: 1" in str(excinfo.value)
    assert "stdout: fake_stdout" in str(excinfo.value)
    assert "stderr: fake_stderr" in str(excinfo.value)

    # Verify that the custom boot time command was used
    mock_low_level_execute_command.assert_called_with('custom_boot_time_command', sudoable=ActionModule.DEFAULT_SUDOABLE)
