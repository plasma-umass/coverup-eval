# file lib/ansible/plugins/callback/minimal.py:70-71
# lines [71]
# branches []

import pytest
from ansible.plugins.callback import minimal
from ansible.utils.display import Display
from unittest.mock import MagicMock, patch

# Mock the Display class in the minimal module
@pytest.fixture
def mock_display(mocker):
    with patch('ansible.utils.display.Display', autospec=True) as mock:
        yield mock

# Mock the result object with a _host property
@pytest.fixture
def mock_result(mocker):
    mock_host = MagicMock()
    mock_host.get_name.return_value = 'testhost'
    mock_result = MagicMock(_host=mock_host)
    return mock_result

# Test function to cover the missing line 71
def test_v2_runner_on_skipped(mock_display, mock_result):
    callback = minimal.CallbackModule()
    callback._display = mock_display

    callback.v2_runner_on_skipped(mock_result)

    # Verify that the display method was called with the correct arguments
    # The color should match the constant defined in minimal.C.COLOR_SKIP
    mock_display.display.assert_called_once_with('testhost | SKIPPED', color=minimal.C.COLOR_SKIP)
