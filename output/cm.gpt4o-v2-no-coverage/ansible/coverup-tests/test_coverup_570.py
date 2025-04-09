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

def test_v2_runner_on_failed_no_json(callback_module, mocker):
    result = Mock()
    result._result = {}
    result._task.action = 'command'
    result._host.get_name.return_value = 'localhost'

    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module._display, 'display')
    mocker.patch.object(callback_module, '_command_generic_msg', return_value='generic message')

    callback_module.v2_runner_on_failed(result)

    callback_module._handle_exception.assert_called_once_with(result._result)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._display.display.assert_called_once_with('generic message', color=C.COLOR_ERROR)

def test_v2_runner_on_failed_with_json(callback_module, mocker):
    result = Mock()
    result._result = {'module_stderr': 'error'}
    result._task.action = 'command'
    result._host.get_name.return_value = 'localhost'

    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module._display, 'display')
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped results')

    callback_module.v2_runner_on_failed(result)

    callback_module._handle_exception.assert_called_once_with(result._result)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._display.display.assert_called_once_with('localhost | FAILED! => dumped results', color=C.COLOR_ERROR)
