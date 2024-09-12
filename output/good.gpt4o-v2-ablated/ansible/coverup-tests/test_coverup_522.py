# file: lib/ansible/plugins/callback/minimal.py:70-71
# asked: {"lines": [71], "branches": []}
# gained: {"lines": [71], "branches": []}

import pytest
from ansible.plugins.callback.minimal import CallbackModule
from ansible.utils.display import Display
from ansible import constants as C
from unittest.mock import Mock

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def mock_result():
    mock_host = Mock()
    mock_host.get_name.return_value = "test_host"
    mock_result = Mock()
    mock_result._host = mock_host
    return mock_result

def test_v2_runner_on_skipped(callback_module, mock_result, monkeypatch):
    mock_display = Mock()
    monkeypatch.setattr(callback_module, '_display', mock_display)
    callback_module.v2_runner_on_skipped(mock_result)
    mock_display.display.assert_called_once_with("test_host | SKIPPED", color=C.COLOR_SKIP)
