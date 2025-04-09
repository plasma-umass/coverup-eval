# file: lib/ansible/plugins/callback/default.py:432-434
# asked: {"lines": [432, 433, 434], "branches": [[433, 0], [433, 434]]}
# gained: {"lines": [432, 433, 434], "branches": [[433, 0], [433, 434]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_notify_verbose(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_display.verbosity = 2
    mock_handler = Mock()
    mock_handler.get_name.return_value = 'handler_name'
    mock_host = 'host_name'

    callback_module.v2_playbook_on_notify(mock_handler, mock_host)

    mock_display.display.assert_called_once_with(
        "NOTIFIED HANDLER handler_name for host_name",
        color=C.COLOR_VERBOSE,
        screen_only=True
    )

def test_v2_playbook_on_notify_non_verbose(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_display.verbosity = 1
    mock_handler = Mock()
    mock_host = 'host_name'

    callback_module.v2_playbook_on_notify(mock_handler, mock_host)

    mock_display.display.assert_not_called()
