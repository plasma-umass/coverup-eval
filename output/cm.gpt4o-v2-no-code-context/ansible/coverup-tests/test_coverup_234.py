# file: lib/ansible/plugins/callback/minimal.py:53-68
# asked: {"lines": [53, 54, 56, 58, 59, 60, 62, 63, 65, 66, 68], "branches": [[58, 59], [58, 62], [65, 66], [65, 68]]}
# gained: {"lines": [53, 54, 56, 58, 59, 60, 62, 63, 65, 66, 68], "branches": [[58, 59], [58, 62], [65, 66], [65, 68]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.minimal import CallbackModule
from ansible.plugins.callback import CallbackBase
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

def test_v2_runner_on_ok_changed(callback_module, result, mocker):
    result._result['changed'] = True
    mock_display = mocker.patch.object(callback_module._display, 'display')
    mock_clean_results = mocker.patch.object(callback_module, '_clean_results')
    mock_handle_warnings = mocker.patch.object(callback_module, '_handle_warnings')
    mock_dump_results = mocker.patch.object(callback_module, '_dump_results', return_value='dumped_results')

    callback_module.v2_runner_on_ok(result)

    mock_clean_results.assert_called_once_with(result._result, result._task.action)
    mock_handle_warnings.assert_called_once_with(result._result)
    mock_display.assert_called_once_with("localhost | CHANGED => dumped_results", color=C.COLOR_CHANGED)

def test_v2_runner_on_ok_success(callback_module, result, mocker):
    result._result['changed'] = False
    mock_display = mocker.patch.object(callback_module._display, 'display')
    mock_clean_results = mocker.patch.object(callback_module, '_clean_results')
    mock_handle_warnings = mocker.patch.object(callback_module, '_handle_warnings')
    mock_dump_results = mocker.patch.object(callback_module, '_dump_results', return_value='dumped_results')

    callback_module.v2_runner_on_ok(result)

    mock_clean_results.assert_called_once_with(result._result, result._task.action)
    mock_handle_warnings.assert_called_once_with(result._result)
    mock_display.assert_called_once_with("localhost | SUCCESS => dumped_results", color=C.COLOR_OK)

def test_v2_runner_on_ok_no_json(callback_module, result, mocker):
    result._result['changed'] = False
    result._task.action = C.MODULE_NO_JSON[0]
    mock_display = mocker.patch.object(callback_module._display, 'display')
    mock_clean_results = mocker.patch.object(callback_module, '_clean_results')
    mock_handle_warnings = mocker.patch.object(callback_module, '_handle_warnings')
    mock_command_generic_msg = mocker.patch.object(callback_module, '_command_generic_msg', return_value='generic_msg')

    callback_module.v2_runner_on_ok(result)

    mock_clean_results.assert_called_once_with(result._result, result._task.action)
    mock_handle_warnings.assert_called_once_with(result._result)
    mock_display.assert_called_once_with('generic_msg', color=C.COLOR_OK)
