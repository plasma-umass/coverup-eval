# file lib/ansible/plugins/callback/junit.py:156-174
# lines [159, 161, 162, 164, 165, 166, 167, 169, 170, 171, 172, 174]
# branches ['161->162', '161->164', '169->170', '169->174', '171->172', '171->174']

import pytest
from ansible.plugins.callback.junit import CallbackModule
from ansible.executor.task_result import TaskResult
from unittest.mock import MagicMock

@pytest.fixture
def callback_module():
    callback = CallbackModule()
    callback._play_name = 'fake_play'
    callback._hide_task_arguments = 'false'
    callback._task_data = {}
    return callback

@pytest.fixture
def task_result():
    fake_task = MagicMock()
    fake_task._uuid = 'fake_uuid'
    fake_task.get_name.return_value = 'fake_name'
    fake_task.get_path.return_value = '/fake/path'
    fake_task.action = 'fake_action'
    fake_task.no_log = False
    fake_task.args = {'arg1': 'value1', 'arg2': 'value2'}
    return TaskResult(host='fake_host', task=fake_task, return_data={})

def test_start_task_with_args(callback_module, task_result):
    callback_module._start_task(task_result._task)

    assert task_result._task._uuid in callback_module._task_data
    task_data = callback_module._task_data[task_result._task._uuid]
    expected_name = 'fake_name arg1=value1, arg2=value2'
    assert task_data.name == expected_name, f"Expected task name to be '{expected_name}', but got '{task_data.name}'"
    assert task_data.path == '/fake/path'
    assert task_data.play == 'fake_play'
    assert task_data.action == 'fake_action'
