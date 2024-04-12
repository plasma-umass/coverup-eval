# file lib/ansible/plugins/callback/oneline.py:76-77
# lines [76, 77]
# branches []

import pytest
from ansible.plugins.callback import oneline
from ansible.utils.display import Display
from unittest.mock import Mock

# Mock the Display class in the ansible.utils.display module
@pytest.fixture
def mock_display(mocker):
    mock = mocker.patch('ansible.utils.display.Display', return_value=Mock(spec=Display))
    mock.display = Mock()
    return mock

# Mock the result object with a _host attribute
@pytest.fixture
def mock_result(mocker):
    mock_result = Mock()
    mock_host = Mock()
    mock_host.get_name.return_value = 'testhost'
    mock_result._host = mock_host
    return mock_result

# Test function to cover v2_runner_on_skipped
def test_v2_runner_on_skipped(mock_display, mock_result):
    callback = oneline.CallbackModule()
    callback._display = mock_display
    callback.v2_runner_on_skipped(mock_result)
    mock_display.display.assert_called_once_with('testhost | SKIPPED', color=oneline.C.COLOR_SKIP)
