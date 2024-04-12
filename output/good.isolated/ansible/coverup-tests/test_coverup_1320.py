# file lib/ansible/plugins/action/reboot.py:323-350
# lines [342, 343, 344, 345, 346, 347]
# branches ['341->342']

import pytest
from ansible.errors import AnsibleConnectionFailure
from ansible.utils.display import Display
from ansible.plugins.action.reboot import ActionModule
from datetime import datetime
from unittest.mock import MagicMock

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch('ansible.utils.display.Display.vvv')
    mocker.patch('ansible.utils.display.Display.debug')

# Test function to cover lines 342-347
def test_perform_reboot_failure(mock_display, mocker):
    # Create a mock Task and ActionBase
    mock_task = MagicMock()
    mock_task.action = 'test_action'
    mock_connection = MagicMock()
    mock_play_context = MagicMock()
    mock_loader = MagicMock()
    mock_shared_loader_obj = MagicMock()
    mock_new_stdin = MagicMock()

    action_module = ActionModule(mock_task, mock_connection, mock_play_context, mock_loader, mock_shared_loader_obj, mock_new_stdin)

    mocker.patch.object(action_module, 'get_shutdown_command', return_value='shutdown')
    mocker.patch.object(action_module, 'get_shutdown_command_args', return_value='-r now')

    # Mock the _low_level_execute_command to simulate a non-zero return code
    mocker.patch.object(action_module, '_low_level_execute_command', return_value={'rc': 1, 'stdout': 'error', 'stderr': 'error'})

    task_vars = {}
    distribution = 'generic'

    result = action_module.perform_reboot(task_vars, distribution)

    # Assertions to verify the postconditions
    assert result['failed'] is True
    assert result['rebooted'] is False
    assert 'Reboot command failed. Error was: \'error, error\'' in result['msg']
