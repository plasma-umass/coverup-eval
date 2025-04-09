# file: lib/ansible/plugins/callback/oneline.py:73-74
# asked: {"lines": [73, 74], "branches": []}
# gained: {"lines": [73, 74], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.oneline import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_unreachable(callback_module):
    mock_display = Mock()
    callback_module._display = mock_display

    mock_host = Mock()
    mock_host.get_name.return_value = 'test_host'

    result = Mock()
    result._host = mock_host
    result._result = {'msg': 'Host unreachable'}

    callback_module.v2_runner_on_unreachable(result)

    mock_display.display.assert_called_once_with('test_host | UNREACHABLE!: Host unreachable', color=C.COLOR_UNREACHABLE)

def test_v2_runner_on_unreachable_no_msg(callback_module):
    mock_display = Mock()
    callback_module._display = mock_display

    mock_host = Mock()
    mock_host.get_name.return_value = 'test_host'

    result = Mock()
    result._host = mock_host
    result._result = {}

    callback_module.v2_runner_on_unreachable(result)

    mock_display.display.assert_called_once_with('test_host | UNREACHABLE!: ', color=C.COLOR_UNREACHABLE)
