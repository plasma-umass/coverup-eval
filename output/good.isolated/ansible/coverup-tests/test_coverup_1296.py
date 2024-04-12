# file lib/ansible/plugins/action/reboot.py:203-209
# lines [204, 205, 206, 207, 208, 209]
# branches ['204->exit', '204->205', '205->204', '205->206']

import pytest
from ansible.utils.display import Display
from ansible.plugins.action.reboot import ActionModule
from ansible.playbook.task import Task

# Mock the Display class to capture warnings
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'warning')

# Define the test function to cover the missing lines
def test_deprecated_args(mock_display):
    # Create a mock Task with a dict that contains deprecated arguments
    mock_task = Task()
    mock_task.action = 'reboot'
    mock_task.args = {'deprecated_arg': 'value'}

    # Set up the ActionModule with the mock task
    action_module = ActionModule(task=mock_task,
                                 connection=None,
                                 play_context=None,
                                 loader=None,
                                 templar=None,
                                 shared_loader_obj=None)
    # Mock the DEPRECATED_ARGS to include 'deprecated_arg'
    action_module.DEPRECATED_ARGS = {'deprecated_arg': '2.9'}

    # Call the method that should trigger the warning
    action_module.deprecated_args()

    # Assert that the warning was indeed triggered with the correct message
    mock_display.assert_called_once_with(
        "Since Ansible 2.9, deprecated_arg is no longer a valid option for reboot"
    )
