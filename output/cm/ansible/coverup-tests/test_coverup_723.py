# file lib/ansible/plugins/callback/default.py:417-420
# lines [417, 418, 419, 420]
# branches []

import pytest
from ansible.plugins.callback import default
from ansible.executor.task_result import TaskResult
from ansible.utils.color import stringc
from unittest.mock import MagicMock, Mock

# Define a custom class to mock the CallbackBase methods and attributes
class MockCallbackBase:
    def __init__(self):
        self._display = MagicMock()

# Create a test function to cover the missing lines in v2_runner_on_async_ok
@pytest.fixture
def mock_callback_module(mocker):
    mocker.patch('ansible.plugins.callback.default.CallbackBase', new=MockCallbackBase)
    callback_module = default.CallbackModule()
    callback_module._display.display = MagicMock()
    return callback_module

def test_v2_runner_on_async_ok(mock_callback_module):
    # Mock the result object with necessary attributes
    mock_host = MagicMock()
    mock_host.get_name.return_value = 'testhost'
    mock_result = {'ansible_job_id': '12345'}
    
    # Create a Mock TaskResult, since the real TaskResult does not accept 'result' as a keyword argument
    mock_task_result = Mock(TaskResult)
    mock_task_result._host = mock_host
    mock_task_result._result = mock_result

    # Call the method we want to test
    mock_callback_module.v2_runner_on_async_ok(mock_task_result)

    # Assert that the display method was called with the correct message
    expected_message = "ASYNC OK on testhost: jid=12345"
    mock_callback_module._display.display.assert_called_once_with(expected_message, color=default.C.COLOR_DEBUG)
