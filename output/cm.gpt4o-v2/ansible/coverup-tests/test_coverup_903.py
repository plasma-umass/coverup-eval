# file: lib/ansible/plugins/callback/minimal.py:70-71
# asked: {"lines": [70, 71], "branches": []}
# gained: {"lines": [70, 71], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.minimal import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_skipped(callback_module, mocker):
    mock_display = mocker.patch.object(callback_module._display, 'display')
    mock_host = Mock()
    mock_host.get_name.return_value = 'test_host'
    mock_result = Mock()
    mock_result._host = mock_host

    callback_module.v2_runner_on_skipped(mock_result)

    mock_display.assert_called_once_with('test_host | SKIPPED', color=C.COLOR_SKIP)
