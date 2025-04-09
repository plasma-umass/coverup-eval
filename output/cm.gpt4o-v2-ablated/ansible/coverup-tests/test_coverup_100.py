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
def mock_result():
    mock = Mock()
    mock._result = {}
    mock._task.action = 'some_action'
    mock._host.get_name.return_value = 'localhost'
    return mock

def test_v2_runner_on_ok_changed(callback_module, mock_result, mocker):
    mock_result._result = {'changed': True}
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module._display, 'display')

    callback_module.v2_runner_on_ok(mock_result)

    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._handle_warnings.assert_called_once_with(mock_result._result)
    callback_module._display.display.assert_called_once()
    assert callback_module._display.display.call_args[1]['color'] == C.COLOR_CHANGED

def test_v2_runner_on_ok_success(callback_module, mock_result, mocker):
    mock_result._result = {'changed': False}
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module._display, 'display')

    callback_module.v2_runner_on_ok(mock_result)

    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._handle_warnings.assert_called_once_with(mock_result._result)
    callback_module._display.display.assert_called_once()
    assert callback_module._display.display.call_args[1]['color'] == C.COLOR_OK

def test_v2_runner_on_ok_no_json(callback_module, mock_result, mocker):
    mock_result._result = {'changed': True}
    mock_result._task.action = 'some_no_json_action'
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module._display, 'display')
    mocker.patch.object(C, 'MODULE_NO_JSON', new_callable=lambda: ['some_no_json_action'])

    callback_module.v2_runner_on_ok(mock_result)

    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._handle_warnings.assert_called_once_with(mock_result._result)
    callback_module._display.display.assert_called_once()
    assert 'localhost' in callback_module._display.display.call_args[0][0]
    assert 'CHANGED' in callback_module._display.display.call_args[0][0]

def test_v2_runner_on_ok_with_json(callback_module, mock_result, mocker):
    mock_result._result = {'changed': True, 'ansible_job_id': '12345'}
    mock_result._task.action = 'some_action'
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_results')
    mocker.patch.object(callback_module._display, 'display')

    callback_module.v2_runner_on_ok(mock_result)

    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._handle_warnings.assert_called_once_with(mock_result._result)
    callback_module._dump_results.assert_called_once_with(mock_result._result, indent=4)
    callback_module._display.display.assert_called_once()
    assert 'localhost' in callback_module._display.display.call_args[0][0]
    assert 'CHANGED' in callback_module._display.display.call_args[0][0]
    assert 'dumped_results' in callback_module._display.display.call_args[0][0]
