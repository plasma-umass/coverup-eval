# file lib/ansible/plugins/callback/default.py:153-159
# lines [154, 155, 157, 158, 159]
# branches ['154->155', '154->157']

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.executor.task_result import TaskResult
from ansible.playbook.task import Task
from unittest.mock import MagicMock, PropertyMock

@pytest.fixture
def callback_module(mocker):
    mocker.patch('ansible.plugins.callback.default.CallbackBase._dump_results', return_value="result dump")
    mocker.patch('ansible.plugins.callback.default.CallbackBase.host_label', return_value="test_host")
    mocker.patch('ansible.plugins.callback.default.C.COLOR_UNREACHABLE', "red")
    callback = CallbackModule()
    callback._display = MagicMock()
    callback._last_task_banner = None
    callback._print_task_banner = MagicMock()
    callback.display_failed_stderr = False
    return callback

def test_v2_runner_on_unreachable(callback_module):
    fake_task = MagicMock(Task)
    fake_task._uuid = "unique_id"
    fake_result = MagicMock(TaskResult)
    fake_result._task = fake_task
    fake_result._result = {}

    callback_module.v2_runner_on_unreachable(fake_result)

    expected_msg = "fatal: [test_host]: UNREACHABLE! => result dump"
    callback_module._display.display.assert_called_once_with(expected_msg, color="red", stderr=False)
