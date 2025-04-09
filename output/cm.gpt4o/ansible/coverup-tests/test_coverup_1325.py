# file lib/ansible/plugins/callback/default.py:161-162
# lines [162]
# branches []

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.display import Display
from unittest.mock import patch

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_no_hosts_matched(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module._display, 'display')
    callback_module.v2_playbook_on_no_hosts_matched()
    mock_display.assert_called_once_with("skipping: no hosts matched", color=mocker.ANY)
