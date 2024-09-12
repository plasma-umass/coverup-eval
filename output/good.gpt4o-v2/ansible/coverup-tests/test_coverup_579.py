# file: lib/ansible/playbook/task.py:486-489
# asked: {"lines": [486, 487, 488, 489], "branches": [[487, 488], [487, 489]]}
# gained: {"lines": [486, 487, 488, 489], "branches": [[487, 488], [487, 489]]}

import pytest
from ansible.playbook.task import Task

def test_all_parents_static_no_parent():
    task = Task()
    assert task.all_parents_static() == True

def test_all_parents_static_with_parent(mocker):
    parent_task = Task()
    mocker.patch.object(parent_task, 'all_parents_static', return_value=True)
    task = Task(task_include=parent_task)
    assert task.all_parents_static() == True
    parent_task.all_parents_static.assert_called_once()

def test_all_parents_static_with_parent_false(mocker):
    parent_task = Task()
    mocker.patch.object(parent_task, 'all_parents_static', return_value=False)
    task = Task(task_include=parent_task)
    assert task.all_parents_static() == False
    parent_task.all_parents_static.assert_called_once()
