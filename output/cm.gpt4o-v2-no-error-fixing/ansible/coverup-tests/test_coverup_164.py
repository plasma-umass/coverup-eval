# file: lib/ansible/playbook/task.py:378-392
# asked: {"lines": [378, 379, 381, 382, 383, 385, 386, 387, 389, 390, 392], "branches": [[382, 383], [382, 385], [386, 387], [386, 389]]}
# gained: {"lines": [378, 379, 381, 382, 383, 385, 386, 387, 389, 390, 392], "branches": [[382, 383], [382, 385], [386, 387], [386, 389]]}

import pytest
from ansible.playbook.task import Task
from unittest.mock import MagicMock

@pytest.fixture
def task_instance():
    task = Task()
    task._parent = MagicMock()
    task._role = MagicMock()
    task.implicit = MagicMock()
    task.resolved_action = MagicMock()
    return task

def test_task_copy_with_parent_and_role(task_instance):
    task_instance._parent.copy.return_value = MagicMock()
    new_task = task_instance.copy()
    
    assert new_task._parent is not None
    assert new_task._role is not None
    assert new_task.implicit == task_instance.implicit
    assert new_task.resolved_action == task_instance.resolved_action

def test_task_copy_exclude_parent(task_instance):
    new_task = task_instance.copy(exclude_parent=True)
    
    assert new_task._parent is None
    assert new_task._role is not None
    assert new_task.implicit == task_instance.implicit
    assert new_task.resolved_action == task_instance.resolved_action

def test_task_copy_without_role(task_instance):
    task_instance._role = None
    new_task = task_instance.copy()
    
    assert new_task._parent is not None
    assert new_task._role is None
    assert new_task.implicit == task_instance.implicit
    assert new_task.resolved_action == task_instance.resolved_action
