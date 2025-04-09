# file lib/ansible/plugins/callback/junit.py:156-174
# lines [162]
# branches ['161->162', '169->174', '171->174']

import pytest
from ansible.plugins.callback.junit import CallbackModule
from ansible.playbook.task import Task
from unittest.mock import MagicMock

class FakeTask(Task):
    def __init__(self, name, path, action, no_log, args, _uuid):
        super(FakeTask, self).__init__()
        self.name = name
        self.path = path
        self.action = action
        self.no_log = no_log
        self.args = args
        self._uuid = _uuid

    def get_name(self):
        return self.name

    def get_path(self):
        return self.path

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def task_data():
    return {
        '_uuid': '1234',
        'name': 'fake_task',
        'path': '/fake/path',
        'action': 'fake_action',
        'no_log': False,
        'args': {'fake_arg': 'fake_value'},
    }

def test_start_task_already_started(callback_module, task_data, mocker):
    task = FakeTask(**task_data)
    callback_module._task_data[task._uuid] = MagicMock()
    callback_module._start_task(task)
    assert task._uuid in callback_module._task_data

def test_start_task_with_args(callback_module, task_data, mocker):
    task_data['no_log'] = False
    task_data['_uuid'] = 'unique_uuid'
    task = FakeTask(**task_data)
    callback_module._hide_task_arguments = 'false'
    callback_module._start_task(task)
    assert task._uuid in callback_module._task_data
    assert 'fake_arg=fake_value' in callback_module._task_data[task._uuid].name

def test_start_task_no_args(callback_module, task_data, mocker):
    task_data['no_log'] = False
    task_data['args'] = {}
    task_data['_uuid'] = 'another_unique_uuid'
    task = FakeTask(**task_data)
    callback_module._hide_task_arguments = 'false'
    callback_module._start_task(task)
    assert task._uuid in callback_module._task_data
    assert 'fake_arg=fake_value' not in callback_module._task_data[task._uuid].name
