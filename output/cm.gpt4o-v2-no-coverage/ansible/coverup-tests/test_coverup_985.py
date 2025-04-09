# file: lib/ansible/plugins/callback/default.py:164-165
# asked: {"lines": [164, 165], "branches": []}
# gained: {"lines": [164, 165], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._display = MagicMock()
    return module

def test_v2_playbook_on_no_hosts_remaining(callback_module):
    callback_module.v2_playbook_on_no_hosts_remaining()
    callback_module._display.banner.assert_called_once_with("NO MORE HOSTS LEFT")
