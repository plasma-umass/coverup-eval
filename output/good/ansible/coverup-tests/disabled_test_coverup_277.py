# file lib/ansible/plugins/callback/oneline.py:41-56
# lines [41, 42, 43, 45, 46, 48, 50, 51, 53, 55, 56]
# branches ['42->43', '42->55', '43->45', '43->48', '50->51', '50->53']

import pytest
from ansible.plugins.callback import oneline
from ansible.executor.task_result import TaskResult
from ansible.playbook.task import Task
from ansible.inventory.host import Host
from ansible.vars.manager import VariableManager
from unittest.mock import MagicMock, patch

# Mocking constants
class C:
    MODULE_NO_JSON = []
    COLOR_ERROR = 'red'

@pytest.fixture
def monkeypatch_test():
    mp = MonkeyPatch()
    yield mp
    mp.undo()

def test_v2_runner_on_failed_with_exception_and_verbosity_less_than_3(monkeypatch_test):
    monkeypatch_test.setattr(oneline, 'C', C)
    
    fake_host = Host(name='fake-host')
    fake_task = Task()
    fake_task.action = 'fake_action'
    fake_variable_manager = VariableManager()
    fake_result = {
        'exception': 'Traceback (most recent call last):\nFakeException: An error occurred\n'
    }
    task_result = TaskResult(host=fake_host, task=fake_task, return_data=fake_result)

    display_mock = MagicMock()
    display_mock.verbosity = 2
    callback_module = oneline.CallbackModule()
    callback_module._display = display_mock

    with patch.object(callback_module, '_dump_results', return_value="{}") as dump_results_mock:
        callback_module.v2_runner_on_failed(task_result, ignore_errors=False)

    error_message = "An exception occurred during task execution. To see the full traceback, use -vvv. The error was: FakeException: An error occurred"
    display_mock.display.assert_any_call(error_message, color=C.COLOR_ERROR)
    display_mock.display.assert_any_call("fake-host | FAILED! => {}", color=C.COLOR_ERROR)
    assert dump_results_mock.called

def test_v2_runner_on_failed_with_exception_and_verbosity_at_least_3(monkeypatch_test):
    monkeypatch_test.setattr(oneline, 'C', C)
    
    fake_host = Host(name='fake-host')
    fake_task = Task()
    fake_task.action = 'fake_action'
    fake_variable_manager = VariableManager()
    fake_result = {
        'exception': 'Traceback (most recent call last):\nFakeException: An error occurred\n'
    }
    task_result = TaskResult(host=fake_host, task=fake_task, return_data=fake_result)

    display_mock = MagicMock()
    display_mock.verbosity = 3
    callback_module = oneline.CallbackModule()
    callback_module._display = display_mock

    with patch.object(callback_module, '_dump_results', return_value="{}") as dump_results_mock:
        callback_module.v2_runner_on_failed(task_result, ignore_errors=False)

    full_traceback = "An exception occurred during task execution. The full traceback is:\nTraceback (most recent call last):FakeException: An error occurred"
    display_mock.display.assert_any_call(full_traceback, color=C.COLOR_ERROR)
    display_mock.display.assert_any_call("fake-host | FAILED! => {}", color=C.COLOR_ERROR)
    assert dump_results_mock.called

from _pytest.monkeypatch import MonkeyPatch
