# file lib/ansible/plugins/callback/oneline.py:73-74
# lines [73, 74]
# branches []

import pytest
from ansible.plugins.callback.oneline import CallbackModule
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the Display class to prevent actual printing to stdout
@pytest.fixture
def mock_display(mocker):
    display_class = mocker.patch('ansible.utils.display.Display')
    display_instance = display_class.return_value
    return display_instance

# Test function to cover v2_runner_on_unreachable method
def test_v2_runner_on_unreachable(mock_display):
    callback = CallbackModule()
    callback._display = mock_display

    fake_result = MagicMock()
    fake_result._host.get_name.return_value = 'test_host'
    fake_result._result = {'msg': 'test unreachable message'}

    callback.v2_runner_on_unreachable(fake_result)

    # Assert that the display method was called with the expected message and color
    mock_display.display.assert_called_once_with(
        'test_host | UNREACHABLE!: test unreachable message',
        color='bright red'
    )
