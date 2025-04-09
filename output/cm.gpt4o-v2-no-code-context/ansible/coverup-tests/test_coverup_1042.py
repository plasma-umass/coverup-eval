# file: lib/ansible/plugins/callback/default.py:432-434
# asked: {"lines": [433, 434], "branches": [[433, 0], [433, 434]]}
# gained: {"lines": [433, 434], "branches": [[433, 0], [433, 434]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming CallbackBase and C are imported from ansible.plugins.callback.default
from ansible.plugins.callback.default import CallbackModule, CallbackBase, C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_notify_verbose(callback_module, monkeypatch):
    # Mocking the display object and its verbosity
    mock_display = MagicMock()
    mock_display.verbosity = 2  # Set verbosity > 1 to trigger the condition
    monkeypatch.setattr(callback_module, '_display', mock_display)

    # Mocking handler and host
    mock_handler = MagicMock()
    mock_handler.get_name.return_value = 'test_handler'
    mock_host = 'test_host'

    # Call the method
    callback_module.v2_playbook_on_notify(mock_handler, mock_host)

    # Assertions to verify the display method was called with correct parameters
    mock_display.display.assert_called_once_with(
        "NOTIFIED HANDLER test_handler for test_host",
        color=C.COLOR_VERBOSE,
        screen_only=True
    )

def test_v2_playbook_on_notify_non_verbose(callback_module, monkeypatch):
    # Mocking the display object and its verbosity
    mock_display = MagicMock()
    mock_display.verbosity = 1  # Set verbosity <= 1 to not trigger the condition
    monkeypatch.setattr(callback_module, '_display', mock_display)

    # Mocking handler and host
    mock_handler = MagicMock()
    mock_handler.get_name.return_value = 'test_handler'
    mock_host = 'test_host'

    # Call the method
    callback_module.v2_playbook_on_notify(mock_handler, mock_host)

    # Assertions to verify the display method was not called
    mock_display.display.assert_not_called()
