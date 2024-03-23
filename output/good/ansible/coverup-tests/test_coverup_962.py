# file lib/ansible/plugins/callback/default.py:161-162
# lines [161, 162]
# branches []

import pytest
from ansible.plugins.callback import default
from ansible.utils.display import Display

# Mock the Display class to avoid actual print calls during the test
@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.utils.display.Display', return_value=mocker.Mock(spec=Display))

# Test function to cover v2_playbook_on_no_hosts_matched
def test_v2_playbook_on_no_hosts_matched(mock_display):
    callback_module = default.CallbackModule()
    callback_module._display = mock_display

    callback_module.v2_playbook_on_no_hosts_matched()

    # Assert that the display method was called with the expected message and color
    mock_display.display.assert_called_once_with("skipping: no hosts matched", color=default.C.COLOR_SKIP)
