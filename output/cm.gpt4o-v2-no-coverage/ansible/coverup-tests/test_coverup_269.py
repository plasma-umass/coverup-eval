# file: lib/ansible/playbook/task.py:356-368
# asked: {"lines": [356, 357, 358, 359, 361, 363, 364, 365, 366, 368], "branches": [[358, 359], [358, 361], [363, 364], [363, 365], [365, 366], [365, 368]]}
# gained: {"lines": [356, 357, 358, 359, 361, 363, 364, 365, 366, 368], "branches": [[358, 359], [358, 361], [363, 364], [363, 365], [365, 366], [365, 368]]}

import pytest
from ansible.playbook.task import Task
from unittest.mock import Mock

@pytest.fixture
def mock_parent():
    parent = Mock()
    parent.get_vars.return_value = {'parent_var': 'value', 'tags': 'should be removed', 'when': 'should be removed'}
    return parent

@pytest.fixture
def task_with_parent(mock_parent):
    task = Task()
    task._parent = mock_parent
    task.vars = {'task_var': 'value'}
    return task

@pytest.fixture
def task_without_parent():
    task = Task()
    task._parent = None
    task.vars = {'task_var': 'value'}
    return task

def test_get_vars_with_parent(task_with_parent):
    result = task_with_parent.get_vars()
    assert result == {'parent_var': 'value', 'task_var': 'value'}

def test_get_vars_without_parent(task_without_parent):
    result = task_without_parent.get_vars()
    assert result == {'task_var': 'value'}
