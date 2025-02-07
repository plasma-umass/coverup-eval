# file: lib/ansible/playbook/task.py:370-376
# asked: {"lines": [370, 371, 372, 373, 374, 375, 376], "branches": [[372, 373], [372, 374], [374, 375], [374, 376]]}
# gained: {"lines": [370, 371, 372, 373, 374, 375, 376], "branches": [[372, 373], [372, 374], [374, 375], [374, 376]]}

import pytest
from ansible.playbook.task import Task
from ansible import constants as C

class MockParent:
    def get_include_params(self):
        return {'parent_key': 'parent_value'}

@pytest.fixture
def task_with_parent():
    parent = MockParent()
    task = Task(task_include=parent)
    task.action = 'include'
    task.vars = {'task_key': 'task_value'}
    return task

@pytest.fixture
def task_without_parent():
    task = Task()
    task.action = 'include'
    task.vars = {'task_key': 'task_value'}
    return task

@pytest.fixture
def task_with_non_include_action():
    task = Task()
    task.action = 'non_include'
    task.vars = {'task_key': 'task_value'}
    return task

def test_get_include_params_with_parent(task_with_parent):
    result = task_with_parent.get_include_params()
    assert result == {'parent_key': 'parent_value', 'task_key': 'task_value'}

def test_get_include_params_without_parent(task_without_parent):
    result = task_without_parent.get_include_params()
    assert result == {'task_key': 'task_value'}

def test_get_include_params_non_include_action(task_with_non_include_action):
    result = task_with_non_include_action.get_include_params()
    assert result == {}
