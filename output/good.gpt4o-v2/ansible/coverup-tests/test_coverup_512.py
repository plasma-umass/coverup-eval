# file: lib/ansible/plugins/callback/minimal.py:43-51
# asked: {"lines": [43, 45, 46, 48, 49, 51], "branches": [[48, 49], [48, 51]]}
# gained: {"lines": [43, 45, 46, 48, 49, 51], "branches": [[48, 49], [48, 51]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.minimal import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback():
    return CallbackModule()

def test_v2_runner_on_failed_module_no_json(callback, mocker):
    result = Mock()
    result._result = {}
    result._task.action = 'command'
    result._host.get_name.return_value = 'localhost'
    
    mock_display = mocker.patch.object(callback._display, 'display')
    mock_command_generic_msg = mocker.patch.object(callback, '_command_generic_msg', return_value='command failed')

    callback.v2_runner_on_failed(result)

    mock_display.assert_called_once_with('command failed', color=C.COLOR_ERROR)
    mock_command_generic_msg.assert_called_once_with('localhost', {}, "FAILED")

def test_v2_runner_on_failed_other(callback, mocker):
    result = Mock()
    result._result = {}
    result._task.action = 'other'
    result._host.get_name.return_value = 'localhost'
    
    mock_display = mocker.patch.object(callback._display, 'display')
    mock_dump_results = mocker.patch.object(callback, '_dump_results', return_value='dumped results')

    callback.v2_runner_on_failed(result)

    mock_display.assert_called_once_with('localhost | FAILED! => dumped results', color=C.COLOR_ERROR)
    mock_dump_results.assert_called_once_with({}, indent=4)
