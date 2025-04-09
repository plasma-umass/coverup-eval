# file: lib/ansible/plugins/callback/oneline.py:41-56
# asked: {"lines": [41, 42, 43, 45, 46, 48, 50, 51, 53, 55, 56], "branches": [[42, 43], [42, 55], [43, 45], [43, 48], [50, 51], [50, 53]]}
# gained: {"lines": [41, 42, 43, 45, 46, 48, 50, 51, 53, 55, 56], "branches": [[42, 43], [42, 55], [43, 45], [43, 48], [50, 51], [50, 53]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.oneline import CallbackModule
from ansible.plugins.callback import CallbackBase
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def mock_display():
    return Mock()

@pytest.fixture
def mock_result():
    result = Mock()
    result._result = {}
    result._task = Mock()
    result._host = Mock()
    return result

def test_v2_runner_on_failed_with_exception_low_verbosity(callback_module, mock_display, mock_result):
    mock_result._result = {'exception': 'Traceback (most recent call last):\nError: Something went wrong'}
    mock_result._task.action = 'some_action'
    mock_result._host.get_name.return_value = 'localhost'
    callback_module._display = mock_display
    callback_module._display.verbosity = 2

    callback_module.v2_runner_on_failed(mock_result)

    mock_display.display.assert_any_call(
        "An exception occurred during task execution. To see the full traceback, use -vvv. The error was: Error: Something went wrong",
        color=C.COLOR_ERROR
    )
    mock_display.display.assert_any_call(
        "localhost | FAILED! => {}",
        color=C.COLOR_ERROR
    )

def test_v2_runner_on_failed_with_exception_high_verbosity(callback_module, mock_display, mock_result):
    mock_result._result = {'exception': 'Traceback (most recent call last):\nError: Something went wrong'}
    mock_result._task.action = 'some_action'
    mock_result._host.get_name.return_value = 'localhost'
    callback_module._display = mock_display
    callback_module._display.verbosity = 3

    callback_module.v2_runner_on_failed(mock_result)

    mock_display.display.assert_any_call(
        "An exception occurred during task execution. The full traceback is:\nTraceback (most recent call last):Error: Something went wrong",
        color=C.COLOR_ERROR
    )
    mock_display.display.assert_any_call(
        "localhost | FAILED! => {}",
        color=C.COLOR_ERROR
    )

def test_v2_runner_on_failed_with_module_no_json(callback_module, mock_display, mock_result):
    mock_result._result = {'exception': 'Traceback (most recent call last):\nError: Something went wrong'}
    mock_result._task.action = 'setup'
    mock_result._host.get_name.return_value = 'localhost'
    callback_module._display = mock_display
    callback_module._display.verbosity = 2

    with patch('ansible.constants.MODULE_NO_JSON', new=['setup']):
        callback_module.v2_runner_on_failed(mock_result)

    mock_display.display.assert_any_call(
        callback_module._command_generic_msg('localhost', mock_result._result, 'FAILED'),
        color=C.COLOR_ERROR
    )
    mock_display.display.assert_any_call(
        "localhost | FAILED! => {}",
        color=C.COLOR_ERROR
    )

def test_v2_runner_on_failed_without_exception(callback_module, mock_display, mock_result):
    mock_result._result = {}
    mock_result._task.action = 'some_action'
    mock_result._host.get_name.return_value = 'localhost'
    callback_module._display = mock_display
    callback_module._display.verbosity = 2

    callback_module.v2_runner_on_failed(mock_result)

    mock_display.display.assert_any_call(
        "localhost | FAILED! => {}",
        color=C.COLOR_ERROR
    )
