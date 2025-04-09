# file: lib/ansible/plugins/callback/oneline.py:76-77
# asked: {"lines": [76, 77], "branches": []}
# gained: {"lines": [76, 77], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.oneline import CallbackModule
from ansible.utils.display import Display
import ansible.constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_skipped(callback_module, monkeypatch):
    # Mock the result object
    mock_result = Mock()
    mock_host = Mock()
    mock_host.get_name.return_value = "test_host"
    mock_result._host = mock_host

    # Mock the display object
    mock_display = Mock()
    monkeypatch.setattr(callback_module, '_display', mock_display)

    # Call the method
    callback_module.v2_runner_on_skipped(mock_result)

    # Assert the display method was called with the correct parameters
    mock_display.display.assert_called_once_with("test_host | SKIPPED", color=C.COLOR_SKIP)
