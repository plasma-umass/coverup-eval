# file: lib/ansible/plugins/callback/default.py:161-162
# asked: {"lines": [161, 162], "branches": []}
# gained: {"lines": [161, 162], "branches": []}

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.display import Display
from unittest.mock import patch

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_no_hosts_matched(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module, '_display', autospec=True)
    mock_display.display = mocker.Mock()

    callback_module.v2_playbook_on_no_hosts_matched()

    mock_display.display.assert_called_once_with("skipping: no hosts matched", color=mocker.ANY)
