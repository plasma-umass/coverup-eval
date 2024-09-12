# file: lib/ansible/plugins/callback/oneline.py:58-71
# asked: {"lines": [58, 60, 61, 62, 64, 65, 67, 68, 70, 71], "branches": [[60, 61], [60, 64], [67, 68], [67, 70]]}
# gained: {"lines": [58, 60, 61, 62, 64, 65, 67, 68, 70, 71], "branches": [[60, 61], [60, 64], [67, 68], [67, 70]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.oneline import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_ok_changed(callback_module, mocker):
    result = Mock()
    result._result = {'changed': True}
    result._task.action = 'some_action'
    result._host.get_name.return_value = 'localhost'
    
    mock_display = mocker.patch.object(callback_module._display, 'display')
    mock_dump_results = mocker.patch.object(callback_module, '_dump_results', return_value='result_dump')
    
    callback_module.v2_runner_on_ok(result)
    
    mock_display.assert_called_once_with('localhost | CHANGED => result_dump', color=C.COLOR_CHANGED)

def test_v2_runner_on_ok_not_changed(callback_module, mocker):
    result = Mock()
    result._result = {'changed': False}
    result._task.action = 'some_action'
    result._host.get_name.return_value = 'localhost'
    
    mock_display = mocker.patch.object(callback_module._display, 'display')
    mock_dump_results = mocker.patch.object(callback_module, '_dump_results', return_value='result_dump')
    
    callback_module.v2_runner_on_ok(result)
    
    mock_display.assert_called_once_with('localhost | SUCCESS => result_dump', color=C.COLOR_OK)

def test_v2_runner_on_ok_no_json(callback_module, mocker):
    result = Mock()
    result._result = {'changed': True}
    result._task.action = C.MODULE_NO_JSON[0]
    result._host.get_name.return_value = 'localhost'
    
    mock_display = mocker.patch.object(callback_module._display, 'display')
    mock_command_generic_msg = mocker.patch.object(callback_module, '_command_generic_msg', return_value='generic_msg')
    
    callback_module.v2_runner_on_ok(result)
    
    mock_display.assert_called_once_with('generic_msg', color=C.COLOR_CHANGED)
