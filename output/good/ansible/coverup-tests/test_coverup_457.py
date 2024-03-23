# file lib/ansible/plugins/callback/default.py:399-405
# lines [399, 400, 401, 402, 403, 404, 405]
# branches ['403->404', '403->405']

import pytest
from ansible.plugins.callback import default
from ansible.executor.task_result import TaskResult
from ansible.playbook.task import Task
from unittest.mock import MagicMock, patch

class FakeResult:
    def __init__(self, task_name=None, retries=3, attempts=1):
        self.task_name = task_name
        self._task = Task()
        self._result = {'retries': retries, 'attempts': attempts}

@pytest.fixture
def fake_result():
    return FakeResult(task_name="Test Task")

@pytest.fixture
def callback_module():
    return default.CallbackModule()

def test_v2_runner_retry(callback_module, fake_result, mocker):
    mocker.patch.object(callback_module._display, 'display')
    mocker.patch.object(callback_module, 'host_label', return_value='localhost')
    mocker.patch.object(callback_module, '_run_is_verbose', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value='{}')

    callback_module.v2_runner_retry(fake_result)

    expected_msg = "FAILED - RETRYING: [localhost]: Test Task (2 retries left).Result was: {}"
    callback_module._display.display.assert_called_once_with(expected_msg, color=default.C.COLOR_DEBUG)
