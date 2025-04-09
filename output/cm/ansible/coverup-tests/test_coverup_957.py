# file lib/ansible/plugins/callback/default.py:164-165
# lines [164, 165]
# branches []

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.display import Display

# Mock the Display class
@pytest.fixture
def mock_display(mocker):
    display_mock = mocker.MagicMock(spec=Display)
    display_mock.banner = mocker.MagicMock()
    return display_mock

# Test function to cover the missing lines/branches
def test_v2_playbook_on_no_hosts_remaining(mock_display):
    callback_module = CallbackModule()
    callback_module._display = mock_display
    callback_module.v2_playbook_on_no_hosts_remaining()
    mock_display.banner.assert_called_once_with("NO MORE HOSTS LEFT")
