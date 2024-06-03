# file lib/ansible/plugins/callback/minimal.py:70-71
# lines [71]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.minimal import CallbackModule
from ansible.utils.display import Display
import ansible.constants as C

@pytest.fixture
def mock_display(mocker):
    display_instance = Display()
    mocker.patch.object(display_instance, 'display')
    return display_instance

@pytest.fixture
def callback_module(mock_display):
    module = CallbackModule()
    module._display = mock_display
    return module

def test_v2_runner_on_skipped(callback_module, mock_display):
    # Arrange
    mock_host = Mock()
    mock_host.get_name.return_value = 'test_host'
    mock_result = Mock()
    mock_result._host = mock_host

    # Act
    callback_module.v2_runner_on_skipped(mock_result)

    # Assert
    mock_display.display.assert_called_once_with("test_host | SKIPPED", color=C.COLOR_SKIP)
