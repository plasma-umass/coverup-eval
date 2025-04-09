# file: lib/ansible/plugins/callback/default.py:417-420
# asked: {"lines": [417, 418, 419, 420], "branches": []}
# gained: {"lines": [417, 418, 419, 420], "branches": []}

import pytest
from unittest.mock import Mock, MagicMock
from ansible.plugins.callback.default import CallbackModule
from ansible.plugins.callback import CallbackBase
from ansible.utils.display import Display
import ansible.constants as C

@pytest.fixture
def callback_module():
    display = Mock(spec=Display)
    callback = CallbackModule()
    callback._display = display
    return callback

def test_v2_runner_on_async_ok(callback_module):
    result = Mock()
    result._host.get_name.return_value = 'test_host'
    result._result.get.return_value = '12345'

    callback_module.v2_runner_on_async_ok(result)

    callback_module._display.display.assert_called_once_with(
        "ASYNC OK on test_host: jid=12345", color=C.COLOR_DEBUG
    )
