# file: lib/ansible/plugins/callback/default.py:164-165
# asked: {"lines": [164, 165], "branches": []}
# gained: {"lines": [164, 165], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_no_hosts_remaining(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module, '_display', autospec=True)
    callback_module.v2_playbook_on_no_hosts_remaining()
    mock_display.banner.assert_called_once_with("NO MORE HOSTS LEFT")
