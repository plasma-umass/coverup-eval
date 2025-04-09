# file: lib/ansible/playbook/task.py:486-489
# asked: {"lines": [486, 487, 488, 489], "branches": [[487, 488], [487, 489]]}
# gained: {"lines": [486, 487, 488, 489], "branches": [[487, 488], [487, 489]]}

import pytest
from unittest.mock import Mock

from ansible.playbook.task import Task

@pytest.fixture
def task_with_parent():
    parent_task = Mock(spec=Task)
    parent_task.all_parents_static.return_value = True
    task = Task()
    task._parent = parent_task
    return task

@pytest.fixture
def task_without_parent():
    task = Task()
    task._parent = None
    return task

def test_all_parents_static_with_parent(task_with_parent):
    assert task_with_parent.all_parents_static() is True
    task_with_parent._parent.all_parents_static.assert_called_once()

def test_all_parents_static_without_parent(task_without_parent):
    assert task_without_parent.all_parents_static() is True
