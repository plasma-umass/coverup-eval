# file: lib/ansible/plugins/callback/default.py:161-162
# asked: {"lines": [161, 162], "branches": []}
# gained: {"lines": [161, 162], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._display = MagicMock()
    return module

def test_v2_playbook_on_no_hosts_matched(callback_module):
    callback_module.v2_playbook_on_no_hosts_matched()
    callback_module._display.display.assert_called_once_with("skipping: no hosts matched", color=C.COLOR_SKIP)
