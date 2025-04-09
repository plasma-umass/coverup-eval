# file: lib/ansible/plugins/callback/minimal.py:43-51
# asked: {"lines": [43, 45, 46, 48, 49, 51], "branches": [[48, 49], [48, 51]]}
# gained: {"lines": [43, 45, 46, 48, 49, 51], "branches": [[48, 49], [48, 51]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.minimal import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_failed_module_no_json(callback_module, mocker):
    result = Mock()
    result._result = {}
    result._task.action = 'some_action'
    result._host.get_name.return_value = 'localhost'
    
    mocker.patch('ansible.plugins.callback.minimal.C.MODULE_NO_JSON', new_callable=set)
    C.MODULE_NO_JSON.add('some_action')
    
    display_mock = mocker.patch.object(callback_module._display, 'display')
    command_generic_msg_mock = mocker.patch.object(callback_module, '_command_generic_msg', return_value='generic message')
    
    callback_module.v2_runner_on_failed(result)
    
    command_generic_msg_mock.assert_called_once_with('localhost', result._result, 'FAILED')
    display_mock.assert_called_once_with('generic message', color=C.COLOR_ERROR)

def test_v2_runner_on_failed_other_action(callback_module, mocker):
    result = Mock()
    result._result = {}
    result._task.action = 'other_action'
    result._host.get_name.return_value = 'localhost'
    
    mocker.patch('ansible.plugins.callback.minimal.C.MODULE_NO_JSON', new_callable=set)
    
    display_mock = mocker.patch.object(callback_module._display, 'display')
    dump_results_mock = mocker.patch.object(callback_module, '_dump_results', return_value='dumped results')
    
    callback_module.v2_runner_on_failed(result)
    
    dump_results_mock.assert_called_once_with(result._result, indent=4)
    display_mock.assert_called_once_with('localhost | FAILED! => dumped results', color=C.COLOR_ERROR)
