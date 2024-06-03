# file lib/ansible/plugins/callback/default.py:417-420
# lines [417, 418, 419, 420]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.plugins.callback import CallbackBase
from ansible.utils.display import Display
import ansible.constants as C

@pytest.fixture
def mock_display(mocker):
    display_instance = Display()
    mocker.patch.object(display_instance, 'display')
    return display_instance

@pytest.fixture
def callback_module(mock_display):
    module = CallbackModule()
    module._display = mock_display
    return module

def test_v2_runner_on_async_ok(callback_module, mock_display):
    # Mocking the result object
    mock_result = Mock()
    mock_result._host.get_name.return_value = 'test_host'
    mock_result._result.get.return_value = '12345'

    # Call the method
    callback_module.v2_runner_on_async_ok(mock_result)

    # Assertions to verify the expected behavior
    mock_display.display.assert_called_once_with("ASYNC OK on test_host: jid=12345", color=C.COLOR_DEBUG)
