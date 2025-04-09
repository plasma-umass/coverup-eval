# file: lib/ansible/plugins/callback/default.py:432-434
# asked: {"lines": [432, 433, 434], "branches": [[433, 0], [433, 434]]}
# gained: {"lines": [432, 433, 434], "branches": [[433, 434]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_notify(callback_module, monkeypatch):
    # Mock the handler and host
    handler = Mock()
    handler.get_name.return_value = "test_handler"
    host = "test_host"

    # Mock the display object and its verbosity
    mock_display = Mock()
    mock_display.verbosity = 2  # Set verbosity > 1 to enter the if condition
    monkeypatch.setattr(callback_module, '_display', mock_display)

    # Call the method
    callback_module.v2_playbook_on_notify(handler, host)

    # Assert the display method was called with the correct parameters
    mock_display.display.assert_called_once_with(
        "NOTIFIED HANDLER test_handler for test_host",
        color=C.COLOR_VERBOSE,
        screen_only=True
    )
