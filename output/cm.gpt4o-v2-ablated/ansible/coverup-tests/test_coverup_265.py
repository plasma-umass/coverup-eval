# file: lib/ansible/plugins/callback/default.py:432-434
# asked: {"lines": [432, 433, 434], "branches": [[433, 0], [433, 434]]}
# gained: {"lines": [432, 433, 434], "branches": [[433, 0], [433, 434]]}

import pytest
from unittest.mock import Mock, patch
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

def test_v2_playbook_on_notify_verbose(callback_module):
    handler = Mock()
    handler.get_name.return_value = "test_handler"
    host = "test_host"
    
    callback_module._display.verbosity = 2
    callback_module.v2_playbook_on_notify(handler, host)
    
    callback_module._display.display.assert_called_once_with(
        "NOTIFIED HANDLER test_handler for test_host", 
        color=C.COLOR_VERBOSE, 
        screen_only=True
    )

def test_v2_playbook_on_notify_non_verbose(callback_module):
    handler = Mock()
    host = "test_host"
    
    callback_module._display.verbosity = 1
    callback_module.v2_playbook_on_notify(handler, host)
    
    callback_module._display.display.assert_not_called()
