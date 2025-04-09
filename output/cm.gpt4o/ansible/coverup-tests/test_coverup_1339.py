# file lib/ansible/plugins/callback/oneline.py:76-77
# lines [77]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.oneline import CallbackModule
from ansible.utils.display import Display
import ansible.constants as C

@pytest.fixture
def mock_display(mocker):
    display_instance = mocker.patch('ansible.utils.display.Display').return_value
    return display_instance

@pytest.fixture
def callback_module(mock_display):
    callback = CallbackModule()
    callback._display = mock_display
    return callback

def test_v2_runner_on_skipped(callback_module, mock_display):
    mock_host = Mock()
    mock_host.get_name.return_value = 'test_host'
    mock_result = Mock()
    mock_result._host = mock_host

    callback_module.v2_runner_on_skipped(mock_result)

    mock_display.display.assert_called_once_with("test_host | SKIPPED", color=C.COLOR_SKIP)
