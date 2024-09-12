# file: lib/ansible/plugins/callback/default.py:164-165
# asked: {"lines": [165], "branches": []}
# gained: {"lines": [165], "branches": []}

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.display import Display
from unittest.mock import patch

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_no_hosts_remaining(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module, '_display', autospec=True)
    callback_module.v2_playbook_on_no_hosts_remaining()
    mock_display.banner.assert_called_once_with("NO MORE HOSTS LEFT")
