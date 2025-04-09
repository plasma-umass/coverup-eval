# file lib/ansible/plugins/action/reboot.py:203-209
# lines [204, 205, 206, 207, 208, 209]
# branches ['204->exit', '204->205', '205->204', '205->206']

import pytest
from unittest.mock import MagicMock
from ansible.utils.display import Display
from ansible.plugins.action.reboot import ActionModule

# Mock the Display class to capture warnings
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'warning')

# Define the test function to cover the missing lines
def test_deprecated_args_warning(mock_display, mocker):
    # Create a mock task with deprecated arguments
    mock_task = MagicMock()
    mock_task.args = {'deprecated_arg': 'value'}
    mock_task.action = 'reboot'
    
    # Set the DEPRECATED_ARGS for the ActionModule
    ActionModule.DEPRECATED_ARGS = {'deprecated_arg': '2.9'}
    
    # Create an instance of the ActionModule with the mock task
    action_module = ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    
    # Call the deprecated_args method to trigger the warning
    action_module.deprecated_args()
    
    # Assert that the warning was displayed with the correct message
    mock_display.assert_called_once_with("Since Ansible 2.9, deprecated_arg is no longer a valid option for reboot")
