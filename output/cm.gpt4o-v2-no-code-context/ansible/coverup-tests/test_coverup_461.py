# file: lib/ansible/plugins/callback/minimal.py:43-51
# asked: {"lines": [43, 45, 46, 48, 49, 51], "branches": [[48, 49], [48, 51]]}
# gained: {"lines": [43, 45, 46, 48, 49, 51], "branches": [[48, 49], [48, 51]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.minimal import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def result():
    mock_result = Mock()
    mock_result._result = {}
    mock_result._task.action = 'some_action'
    mock_result._host.get_name.return_value = 'localhost'
    return mock_result

def test_v2_runner_on_failed_handle_exception(callback_module, result, mocker):
    mock_handle_exception = mocker.patch.object(callback_module, '_handle_exception')
    mock_handle_warnings = mocker.patch.object(callback_module, '_handle_warnings')
    mock_display = mocker.patch.object(callback_module._display, 'display')

    callback_module.v2_runner_on_failed(result)

    mock_handle_exception.assert_called_once_with(result._result)
    mock_handle_warnings.assert_called_once_with(result._result)
    mock_display.assert_called_once()

def test_v2_runner_on_failed_no_json(callback_module, result, mocker):
    result._task.action = 'some_no_json_action'
    mock_handle_exception = mocker.patch.object(callback_module, '_handle_exception')
    mock_handle_warnings = mocker.patch.object(callback_module, '_handle_warnings')
    mock_display = mocker.patch.object(callback_module._display, 'display')
    mock_command_generic_msg = mocker.patch.object(callback_module, '_command_generic_msg', return_value='generic_msg')

    with patch('ansible.plugins.callback.minimal.C.MODULE_NO_JSON', new_callable=lambda: ['some_no_json_action']):
        callback_module.v2_runner_on_failed(result)

    mock_handle_exception.assert_called_once_with(result._result)
    mock_handle_warnings.assert_called_once_with(result._result)
    mock_command_generic_msg.assert_called_once_with('localhost', result._result, "FAILED")
    mock_display.assert_called_once_with('generic_msg', color='red')

def test_v2_runner_on_failed_with_json(callback_module, result, mocker):
    result._task.action = 'some_action'
    result._result = {'module_stderr': 'some error'}
    mock_handle_exception = mocker.patch.object(callback_module, '_handle_exception')
    mock_handle_warnings = mocker.patch.object(callback_module, '_handle_warnings')
    mock_display = mocker.patch.object(callback_module._display, 'display')
    mock_dump_results = mocker.patch.object(callback_module, '_dump_results', return_value='dumped_results')

    callback_module.v2_runner_on_failed(result)

    mock_handle_exception.assert_called_once_with(result._result)
    mock_handle_warnings.assert_called_once_with(result._result)
    mock_dump_results.assert_called_once_with(result._result, indent=4)
    mock_display.assert_called_once_with("localhost | FAILED! => dumped_results", color='red')
