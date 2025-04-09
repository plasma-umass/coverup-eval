# file: lib/ansible/plugins/callback/minimal.py:73-74
# asked: {"lines": [73, 74], "branches": []}
# gained: {"lines": [73, 74], "branches": []}

import pytest
from ansible.plugins.callback.minimal import CallbackModule
from ansible.utils.display import Display
from unittest.mock import Mock, MagicMock

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._display = Display()
    return module

def test_v2_runner_on_unreachable(callback_module, mocker):
    # Mock the result object
    result = Mock()
    result._host.get_name.return_value = 'test_host'
    result._result = {'msg': 'Host unreachable'}

    # Mock the display object
    mock_display = mocker.patch.object(callback_module, '_display', autospec=True)
    mock_display.display = Mock()
    mock_display.verbosity = 1  # Set verbosity to a valid integer

    # Call the method
    callback_module.v2_runner_on_unreachable(result)

    # Assert the display method was called with the expected arguments
    mock_display.display.assert_called_once_with(
        "test_host | UNREACHABLE! => {\n    \"msg\": \"Host unreachable\"\n}",
        color=mocker.ANY
    )
