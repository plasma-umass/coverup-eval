# file lib/ansible/plugins/callback/default.py:164-165
# lines [164, 165]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_no_hosts_remaining(callback_module, mocker):
    mock_display = MagicMock()
    callback_module._display = mock_display

    callback_module.v2_playbook_on_no_hosts_remaining()

    mock_display.banner.assert_called_once_with("NO MORE HOSTS LEFT")
