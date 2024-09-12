# file: lib/ansible/plugins/callback/oneline.py:41-56
# asked: {"lines": [41, 42, 43, 45, 46, 48, 50, 51, 53, 55, 56], "branches": [[42, 43], [42, 55], [43, 45], [43, 48], [50, 51], [50, 53]]}
# gained: {"lines": [41, 42, 43, 45, 46, 48, 50, 51, 53, 55, 56], "branches": [[42, 43], [42, 55], [43, 45], [43, 48], [50, 51], [50, 53]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.oneline import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback():
    return CallbackModule()

def test_v2_runner_on_failed_with_exception_and_low_verbosity(callback, mocker):
    mock_display = Mock()
    mock_display.verbosity = 2
    callback._display = mock_display

    result = Mock()
    result._result = {'exception': 'Traceback (most recent call last):\nError: Something went wrong'}
    result._task.action = 'some_action'
    result._host.get_name.return_value = 'localhost'

    callback.v2_runner_on_failed(result)

    mock_display.display.assert_any_call(
        "An exception occurred during task execution. To see the full traceback, use -vvv. The error was: Error: Something went wrong",
        color=C.COLOR_ERROR
    )

def test_v2_runner_on_failed_with_exception_and_high_verbosity(callback, mocker):
    mock_display = Mock()
    mock_display.verbosity = 3
    callback._display = mock_display

    result = Mock()
    result._result = {'exception': 'Traceback (most recent call last):\nError: Something went wrong'}
    result._task.action = 'some_action'
    result._host.get_name.return_value = 'localhost'

    callback.v2_runner_on_failed(result)

    mock_display.display.assert_any_call(
        "An exception occurred during task execution. The full traceback is:\nTraceback (most recent call last):Error: Something went wrong",
        color=C.COLOR_ERROR
    )

def test_v2_runner_on_failed_with_module_no_json(callback, mocker):
    mock_display = Mock()
    mock_display.verbosity = 2
    callback._display = mock_display

    result = Mock()
    result._result = {'exception': 'Traceback (most recent call last):\nError: Something went wrong'}
    result._task.action = 'command'
    result._host.get_name.return_value = 'localhost'

    callback.v2_runner_on_failed(result)

    mock_display.display.assert_any_call(
        callback._command_generic_msg(result._host.get_name(), result._result, 'FAILED'),
        color=C.COLOR_ERROR
    )

def test_v2_runner_on_failed_without_exception(callback, mocker):
    mock_display = Mock()
    mock_display.verbosity = 2
    callback._display = mock_display

    result = Mock()
    result._result = {}
    result._task.action = 'some_action'
    result._host.get_name.return_value = 'localhost'

    callback.v2_runner_on_failed(result)

    mock_display.display.assert_any_call(
        "localhost | FAILED! => {}".format(callback._dump_results(result._result, indent=0).replace('\n', '')),
        color=C.COLOR_ERROR
    )
