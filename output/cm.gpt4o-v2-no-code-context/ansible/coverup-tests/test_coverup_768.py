# file: lib/ansible/plugins/callback/oneline.py:73-74
# asked: {"lines": [73, 74], "branches": []}
# gained: {"lines": [73, 74], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.oneline import CallbackModule
from ansible.plugins.callback import CallbackBase
from ansible.utils.display import Display
import ansible.constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_unreachable(callback_module, monkeypatch):
    # Mocking the result object
    result = Mock()
    result._host.get_name.return_value = 'test_host'
    result._result.get.return_value = 'test_message'

    # Mocking the display object
    display_mock = Mock(spec=Display)
    monkeypatch.setattr(callback_module, '_display', display_mock)

    # Call the method
    callback_module.v2_runner_on_unreachable(result)

    # Assertions to verify the expected behavior
    display_mock.display.assert_called_once_with("test_host | UNREACHABLE!: test_message", color=C.COLOR_UNREACHABLE)
