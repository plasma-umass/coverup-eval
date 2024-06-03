# file lib/ansible/plugins/callback/minimal.py:43-51
# lines [45, 46, 48, 49, 51]
# branches ['48->49', '48->51']

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.minimal import CallbackModule
from ansible import constants as C

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

def test_v2_runner_on_failed_handles_exception_and_warnings(callback_module, result, mocker):
    mock_handle_exception = mocker.patch.object(callback_module, '_handle_exception')
    mock_handle_warnings = mocker.patch.object(callback_module, '_handle_warnings')
    mock_display = mocker.patch.object(callback_module._display, 'display')
    mock_command_generic_msg = mocker.patch.object(callback_module, '_command_generic_msg', return_value='generic message')
    mock_dump_results = mocker.patch.object(callback_module, '_dump_results', return_value='dumped results')

    # Test when action is in MODULE_NO_JSON and 'module_stderr' not in result
    result._task.action = list(C.MODULE_NO_JSON)[0]
    result._result = {}
    callback_module.v2_runner_on_failed(result)
    mock_handle_exception.assert_called_once_with(result._result)
    mock_handle_warnings.assert_called_once_with(result._result)
    mock_display.assert_called_once_with('generic message', color=C.COLOR_ERROR)

    # Reset mocks
    mock_handle_exception.reset_mock()
    mock_handle_warnings.reset_mock()
    mock_display.reset_mock()

    # Test when action is not in MODULE_NO_JSON or 'module_stderr' in result
    result._task.action = 'some_other_action'
    result._result = {'module_stderr': 'some error'}
    callback_module.v2_runner_on_failed(result)
    mock_handle_exception.assert_called_once_with(result._result)
    mock_handle_warnings.assert_called_once_with(result._result)
    mock_display.assert_called_once_with('localhost | FAILED! => dumped results', color=C.COLOR_ERROR)
