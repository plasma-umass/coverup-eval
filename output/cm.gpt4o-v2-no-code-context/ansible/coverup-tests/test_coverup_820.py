# file: lib/ansible/plugins/callback/default.py:164-165
# asked: {"lines": [164, 165], "branches": []}
# gained: {"lines": [164, 165], "branches": []}

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.display import Display

@pytest.fixture
def callback_module():
    display = Display()
    callback = CallbackModule()
    callback._display = display
    return callback

def test_v2_playbook_on_no_hosts_remaining(callback_module, mocker):
    mock_banner = mocker.patch.object(callback_module._display, 'banner')
    callback_module.v2_playbook_on_no_hosts_remaining()
    mock_banner.assert_called_once_with("NO MORE HOSTS LEFT")
