# file lib/ansible/plugins/callback/default.py:228-230
# lines [228, 229, 230]
# branches ['229->exit', '229->230']

# test_default_callback.py

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.display import Display
from unittest.mock import MagicMock, create_autospec

@pytest.fixture
def callback_module(mocker):
    # Create a mock for the 'C' constant module
    c_mock = mocker.patch('ansible.plugins.callback.default.C', create=True)
    c_mock.COLOR_OK = 'ok'
    
    # Create a mock for the 'CallbackBase' class
    mocker.patch('ansible.plugins.callback.default.CallbackBase', create=True)
    
    # Create a mock for the 'Display' class
    display_mock = create_autospec(Display)
    
    # Instantiate the CallbackModule and set the display mock
    callback = CallbackModule()
    callback._display = display_mock
    return callback, c_mock

def test_v2_runner_on_start_show_per_host_start_enabled(callback_module):
    callback, c_mock = callback_module
    # Setup the test case to enable 'show_per_host_start' option
    callback.get_option = MagicMock(return_value=True)
    host = 'test_host'
    task = 'test_task'

    # Execute the method
    callback.v2_runner_on_start(host, task)

    # Assert that the display method was called with the expected message
    callback._display.display.assert_called_once_with(" [started test_task on test_host]", color=c_mock.COLOR_OK)

def test_v2_runner_on_start_show_per_host_start_disabled(callback_module):
    callback, _ = callback_module
    # Setup the test case to disable 'show_per_host_start' option
    callback.get_option = MagicMock(return_value=False)
    host = 'test_host'
    task = 'test_task'

    # Execute the method
    callback.v2_runner_on_start(host, task)

    # Assert that the display method was not called
    callback._display.display.assert_not_called()
