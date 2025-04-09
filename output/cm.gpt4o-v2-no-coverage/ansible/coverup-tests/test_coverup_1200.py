# file: lib/ansible/plugins/callback/default.py:417-420
# asked: {"lines": [418, 419, 420], "branches": []}
# gained: {"lines": [418, 419, 420], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def mock_display():
    return Mock()

@pytest.fixture
def callback_module(mock_display):
    module = CallbackModule()
    module._display = mock_display
    return module

def test_v2_runner_on_async_ok(callback_module, mock_display):
    result = Mock()
    result._host.get_name.return_value = 'test_host'
    result._result.get.return_value = '12345'

    callback_module.v2_runner_on_async_ok(result)

    mock_display.display.assert_called_once_with("ASYNC OK on test_host: jid=12345", color=C.COLOR_DEBUG)
