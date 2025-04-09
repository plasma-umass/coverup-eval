# file: lib/ansible/playbook/task.py:141-146
# asked: {"lines": [143, 144, 146], "branches": [[143, 144], [143, 146]]}
# gained: {"lines": [143, 144, 146], "branches": [[143, 144], [143, 146]]}

import pytest
from ansible.playbook.task import Task
from ansible import constants as C

class MockRole:
    def get_name(self, include_role_fqcn=True):
        return "mock_role"

@pytest.fixture
def task_with_meta_action():
    task = Task()
    task._role = None
    task.name = None
    task.action = 'meta'
    task.args = {'_raw_params': 'some_params'}
    return task

@pytest.fixture
def task_with_regular_action():
    task = Task()
    task._role = None
    task.name = 'regular_task'
    task.action = 'regular_action'
    return task

def test_task_repr_meta_action(task_with_meta_action):
    assert repr(task_with_meta_action) == "TASK: meta (some_params)"

def test_task_repr_regular_action(task_with_regular_action):
    assert repr(task_with_regular_action) == "TASK: regular_task"
