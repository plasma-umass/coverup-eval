# file: lib/ansible/plugins/callback/minimal.py:70-71
# asked: {"lines": [70, 71], "branches": []}
# gained: {"lines": [70, 71], "branches": []}

import pytest
from ansible.plugins.callback.minimal import CallbackModule
from ansible.utils.display import Display
from unittest.mock import Mock

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_skipped(callback_module, mocker):
    # Mock the result object
    mock_result = Mock()
    mock_host = Mock()
    mock_host.get_name.return_value = "test_host"
    mock_result._host = mock_host

    # Mock the display object
    mock_display = Mock()
    mocker.patch.object(callback_module, '_display', mock_display)

    # Define the color constant manually since Display.COLOR_SKIP is not available
    COLOR_SKIP = 'cyan'

    # Call the method
    callback_module.v2_runner_on_skipped(mock_result)

    # Assert the display method was called with the correct parameters
    mock_display.display.assert_called_once_with("test_host | SKIPPED", color=COLOR_SKIP)
