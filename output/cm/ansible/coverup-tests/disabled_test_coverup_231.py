# file lib/ansible/plugins/callback/junit.py:156-174
# lines [156, 159, 161, 162, 164, 165, 166, 167, 169, 170, 171, 172, 174]
# branches ['161->162', '161->164', '169->170', '169->174', '171->172', '171->174']

import pytest
from ansible.plugins.callback.junit import CallbackModule
from ansible.executor.task_result import TaskResult
from ansible.playbook.task import Task
from unittest.mock import MagicMock

class FakeTask(Task):
    def __init__(self, name, path, action, no_log, args):
        super(FakeTask, self).__init__()
        self._uuid = 'fake_uuid'
        self._name = name
        self._path = path
        self.action = action
        self.no_log = no_log
        self.args = args

    def get_name(self):
        return self._name

    def get_path(self):
        return self._path

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def task_data():
    return {
        'name': 'fake_task',
        'path': '/fake/path',
        'action': 'fake_action',
        'no_log': False,
        'args': {'arg1': 'value1', 'arg2': 'value2'}
    }

def test_start_task_with_args(callback_module, task_data, mocker):
    task = FakeTask(**task_data)
    callback_module._play_name = 'fake_play'
    callback_module._hide_task_arguments = 'false'
    callback_module._task_data = {}

    callback_module._start_task(task)

    assert task._uuid in callback_module._task_data
    task_record = callback_module._task_data[task._uuid]
    assert task_record.uuid == task._uuid
    assert task_record.name == 'fake_task arg1=value1, arg2=value2'
    assert task_record.path == '/fake/path'
    assert task_record.play == 'fake_play'
    assert task_record.action == 'fake_action'

def test_start_task_no_args(callback_module, task_data, mocker):
    task_data['args'] = {}
    task = FakeTask(**task_data)
    callback_module._play_name = 'fake_play'
    callback_module._hide_task_arguments = 'false'
    callback_module._task_data = {}

    callback_module._start_task(task)

    assert task._uuid in callback_module._task_data
    task_record = callback_module._task_data[task._uuid]
    assert task_record.uuid == task._uuid
    assert task_record.name == 'fake_task'
    assert task_record.path == '/fake/path'
    assert task_record.play == 'fake_play'
    assert task_record.action == 'fake_action'

def test_start_task_already_started(callback_module, task_data, mocker):
    task = FakeTask(**task_data)
    callback_module._play_name = 'fake_play'
    callback_module._hide_task_arguments = 'false'
    callback_module._task_data = {task._uuid: 'existing_task_data'}

    callback_module._start_task(task)

    assert callback_module._task_data[task._uuid] == 'existing_task_data'
