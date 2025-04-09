# file: lib/ansible/plugins/callback/default.py:161-162
# asked: {"lines": [161, 162], "branches": []}
# gained: {"lines": [161, 162], "branches": []}

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.display import Display
from ansible import constants as C

@pytest.fixture
def callback_module(monkeypatch):
    display = Display()
    messages = []
    monkeypatch.setattr(display, 'display', lambda msg, color=None: messages.append((msg, color)))
    callback = CallbackModule()
    callback._display = display
    callback._messages = messages
    return callback

def test_v2_playbook_on_no_hosts_matched(callback_module):
    callback_module.v2_playbook_on_no_hosts_matched()
    assert callback_module._messages == [("skipping: no hosts matched", C.COLOR_SKIP)]
