# file: lib/ansible/plugins/callback/oneline.py:41-56
# asked: {"lines": [42, 43, 45, 46, 48, 50, 51, 53, 55, 56], "branches": [[42, 43], [42, 55], [43, 45], [43, 48], [50, 51], [50, 53]]}
# gained: {"lines": [42, 43, 45, 46, 48, 50, 51, 53, 55, 56], "branches": [[42, 43], [43, 45], [43, 48], [50, 51], [50, 53]]}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.oneline import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_failed_with_exception_and_low_verbosity(callback_module, mocker):
    mock_display = Mock()
    mocker.patch.object(callback_module, '_display', mock_display)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_result')
    result = Mock()
    result._result = {'exception': 'Traceback (most recent call last):\nError message'}
    result._task.action = 'some_action'
    result._host.get_name.return_value = 'localhost'
    mock_display.verbosity = 2

    callback_module.v2_runner_on_failed(result)

    mock_display.display.assert_any_call(
        'An exception occurred during task execution. To see the full traceback, use -vvv. The error was: Error message',
        color=C.COLOR_ERROR
    )
    mock_display.display.assert_any_call(
        'localhost | FAILED! => dumped_result',
        color=C.COLOR_ERROR
    )

def test_v2_runner_on_failed_with_exception_and_high_verbosity(callback_module, mocker):
    mock_display = Mock()
    mocker.patch.object(callback_module, '_display', mock_display)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_result')
    result = Mock()
    result._result = {'exception': 'Traceback (most recent call last):\nError message'}
    result._task.action = 'some_action'
    result._host.get_name.return_value = 'localhost'
    mock_display.verbosity = 3

    callback_module.v2_runner_on_failed(result)

    mock_display.display.assert_any_call(
        'An exception occurred during task execution. The full traceback is:\nTraceback (most recent call last):Error message',
        color=C.COLOR_ERROR
    )
    mock_display.display.assert_any_call(
        'localhost | FAILED! => dumped_result',
        color=C.COLOR_ERROR
    )

def test_v2_runner_on_failed_with_module_no_json(callback_module, mocker):
    mock_display = Mock()
    mocker.patch.object(callback_module, '_display', mock_display)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_result')
    mocker.patch('ansible.constants.MODULE_NO_JSON', new_callable=lambda: {'some_action'})
    result = Mock()
    result._result = {'exception': 'Traceback (most recent call last):\nError message'}
    result._task.action = 'some_action'
    result._host.get_name.return_value = 'localhost'
    mock_display.verbosity = 2

    callback_module.v2_runner_on_failed(result)

    mock_display.display.assert_any_call(
        callback_module._command_generic_msg('localhost', result._result, 'FAILED'),
        color=C.COLOR_ERROR
    )
    mock_display.display.assert_any_call(
        'localhost | FAILED! => dumped_result',
        color=C.COLOR_ERROR
    )
