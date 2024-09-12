# file: lib/ansible/plugins/callback/oneline.py:73-74
# asked: {"lines": [73, 74], "branches": []}
# gained: {"lines": [73, 74], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.oneline import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_unreachable(callback_module, mocker):
    # Mock the result object
    result = Mock()
    result._host.get_name.return_value = 'localhost'
    result._result.get.return_value = 'Host unreachable'

    # Mock the display object
    mock_display = mocker.patch.object(callback_module._display, 'display')

    # Call the method
    callback_module.v2_runner_on_unreachable(result)

    # Assert the display method was called with the correct parameters
    mock_display.assert_called_once_with('localhost | UNREACHABLE!: Host unreachable', color=C.COLOR_UNREACHABLE)
