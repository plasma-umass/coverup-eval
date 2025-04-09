# file: lib/ansible/plugins/callback/oneline.py:41-56
# asked: {"lines": [41, 42, 43, 45, 46, 48, 50, 51, 53, 55, 56], "branches": [[42, 43], [42, 55], [43, 45], [43, 48], [50, 51], [50, 53]]}
# gained: {"lines": [41, 42, 43, 45, 46, 48, 50, 51, 53, 55, 56], "branches": [[42, 43], [42, 55], [43, 45], [43, 48], [50, 51], [50, 53]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.oneline import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    display = Mock()
    display.verbosity = 2
    return CallbackModule(display=display)

def test_v2_runner_on_failed_with_exception_low_verbosity(callback_module):
    result = Mock()
    result._result = {'exception': 'Traceback (most recent call last):\nError: Something went wrong'}
    result._task.action = 'some_action'
    result._host.get_name.return_value = 'localhost'

    callback_module.v2_runner_on_failed(result)

    callback_module._display.display.assert_any_call(
        "An exception occurred during task execution. To see the full traceback, use -vvv. The error was: Error: Something went wrong",
        color=C.COLOR_ERROR
    )
    callback_module._display.display.assert_any_call(
        "localhost | FAILED! => %s" % callback_module._dump_results(result._result, indent=0).replace('\n', ''),
        color=C.COLOR_ERROR
    )

def test_v2_runner_on_failed_with_exception_high_verbosity(callback_module):
    callback_module._display.verbosity = 3
    result = Mock()
    result._result = {'exception': 'Traceback (most recent call last):\nError: Something went wrong'}
    result._task.action = 'some_action'
    result._host.get_name.return_value = 'localhost'

    callback_module.v2_runner_on_failed(result)

    callback_module._display.display.assert_any_call(
        "An exception occurred during task execution. The full traceback is:\nTraceback (most recent call last):Error: Something went wrong",
        color=C.COLOR_ERROR
    )
    callback_module._display.display.assert_any_call(
        "localhost | FAILED! => %s" % callback_module._dump_results(result._result, indent=0).replace('\n', ''),
        color=C.COLOR_ERROR
    )

def test_v2_runner_on_failed_with_module_no_json(callback_module):
    result = Mock()
    result._result = {'exception': 'Traceback (most recent call last):\nError: Something went wrong'}
    result._task.action = 'command'
    result._host.get_name.return_value = 'localhost'

    with patch('ansible.constants.MODULE_NO_JSON', ('command',)):
        callback_module.v2_runner_on_failed(result)

    callback_module._display.display.assert_any_call(
        callback_module._command_generic_msg(result._host.get_name(), result._result, 'FAILED'),
        color=C.COLOR_ERROR
    )
    callback_module._display.display.assert_any_call(
        "localhost | FAILED! => %s" % callback_module._dump_results(result._result, indent=0).replace('\n', ''),
        color=C.COLOR_ERROR
    )

def test_v2_runner_on_failed_without_exception(callback_module):
    result = Mock()
    result._result = {}
    result._task.action = 'some_action'
    result._host.get_name.return_value = 'localhost'

    callback_module.v2_runner_on_failed(result)

    callback_module._display.display.assert_called_once_with(
        "localhost | FAILED! => %s" % callback_module._dump_results(result._result, indent=0).replace('\n', ''),
        color=C.COLOR_ERROR
    )
