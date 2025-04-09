# file lib/ansible/plugins/callback/default.py:407-415
# lines [407, 408, 409, 410, 411, 412, 413, 414]
# branches []

import pytest
from ansible.plugins.callback import default
from ansible.executor.task_result import TaskResult
from unittest.mock import MagicMock

@pytest.fixture
def callback_module():
    return default.CallbackModule()

@pytest.fixture
def task_result(mocker):
    fake_result = {
        'ansible_job_id': '12345',
        'started': 1,
        'finished': 0
    }
    fake_host = MagicMock()
    fake_host.get_name.return_value = 'testhost'
    task_result = TaskResult(host=fake_host, task=None, return_data=fake_result)
    return task_result

def test_v2_runner_on_async_poll(callback_module, task_result, mocker):
    display_mock = mocker.patch.object(callback_module._display, 'display')
    callback_module.v2_runner_on_async_poll(task_result)
    display_mock.assert_called_once_with(
        'ASYNC POLL on testhost: jid=12345 started=1 finished=0',
        color=default.C.COLOR_DEBUG
    )
