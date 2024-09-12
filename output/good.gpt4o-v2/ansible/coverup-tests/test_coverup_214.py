# file: lib/ansible/playbook/task.py:356-368
# asked: {"lines": [356, 357, 358, 359, 361, 363, 364, 365, 366, 368], "branches": [[358, 359], [358, 361], [363, 364], [363, 365], [365, 366], [365, 368]]}
# gained: {"lines": [356, 357, 358, 359, 361, 363, 364, 365, 366, 368], "branches": [[358, 359], [358, 361], [363, 364], [365, 366]]}

import pytest
from ansible.playbook.task import Task

class MockParent:
    def get_vars(self):
        return {'parent_var': 'value', 'tags': 'should be removed', 'when': 'should be removed'}

@pytest.fixture
def task_with_parent():
    parent = MockParent()
    task = Task(block=None, role=None, task_include=parent)
    task.vars = {'task_var': 'value'}
    return task

@pytest.fixture
def task_without_parent():
    task = Task(block=None, role=None, task_include=None)
    task.vars = {'task_var': 'value', 'tags': 'should be removed', 'when': 'should be removed'}
    return task

def test_get_vars_with_parent(task_with_parent):
    result = task_with_parent.get_vars()
    assert 'parent_var' in result
    assert 'task_var' in result
    assert 'tags' not in result
    assert 'when' not in result

def test_get_vars_without_parent(task_without_parent):
    result = task_without_parent.get_vars()
    assert 'task_var' in result
    assert 'tags' not in result
    assert 'when' not in result
