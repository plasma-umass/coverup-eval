# file: lib/ansible/plugins/callback/default.py:432-434
# asked: {"lines": [], "branches": [[433, 0]]}
# gained: {"lines": [], "branches": [[433, 0]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_notify_high_verbosity(callback_module, monkeypatch):
    mock_display = Mock()
    mock_handler = Mock()
    mock_handler.get_name.return_value = "test_handler"
    mock_host = "test_host"

    monkeypatch.setattr(callback_module, '_display', mock_display)
    mock_display.verbosity = 2

    callback_module.v2_playbook_on_notify(mock_handler, mock_host)

    mock_display.display.assert_called_once_with(
        "NOTIFIED HANDLER test_handler for test_host",
        color=C.COLOR_VERBOSE,
        screen_only=True
    )

def test_v2_playbook_on_notify_low_verbosity(callback_module, monkeypatch):
    mock_display = Mock()
    mock_handler = Mock()
    mock_host = "test_host"

    monkeypatch.setattr(callback_module, '_display', mock_display)
    mock_display.verbosity = 1

    callback_module.v2_playbook_on_notify(mock_handler, mock_host)

    mock_display.display.assert_not_called()
