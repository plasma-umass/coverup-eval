# file: lib/ansible/playbook/task.py:378-392
# asked: {"lines": [378, 379, 381, 382, 383, 385, 386, 387, 389, 390, 392], "branches": [[382, 383], [382, 385], [386, 387], [386, 389]]}
# gained: {"lines": [378, 379, 381, 382, 383, 385, 386, 387, 389, 390, 392], "branches": [[382, 383], [382, 385], [386, 387], [386, 389]]}

import pytest
from unittest.mock import MagicMock

# Assuming Task and its dependencies are imported from ansible.playbook.task
from ansible.playbook.task import Task

@pytest.fixture
def task():
    return Task()

def test_task_copy_no_parent_no_role(task):
    task._parent = None
    task._role = None
    task.implicit = True
    task.resolved_action = 'some_action'

    new_task = task.copy()

    assert new_task._parent is None
    assert new_task._role is None
    assert new_task.implicit == task.implicit
    assert new_task.resolved_action == task.resolved_action

def test_task_copy_with_parent_no_exclude(task, monkeypatch):
    parent_task = MagicMock()
    parent_task.copy.return_value = 'copied_parent'
    task._parent = parent_task
    task._role = None
    task.implicit = True
    task.resolved_action = 'some_action'

    new_task = task.copy()

    assert new_task._parent == 'copied_parent'
    assert new_task._role is None
    assert new_task.implicit == task.implicit
    assert new_task.resolved_action == task.resolved_action

def test_task_copy_with_parent_exclude(task, monkeypatch):
    parent_task = MagicMock()
    task._parent = parent_task
    task._role = None
    task.implicit = True
    task.resolved_action = 'some_action'

    new_task = task.copy(exclude_parent=True)

    assert new_task._parent is None
    assert new_task._role is None
    assert new_task.implicit == task.implicit
    assert new_task.resolved_action == task.resolved_action

def test_task_copy_with_role(task):
    task._parent = None
    task._role = 'some_role'
    task.implicit = True
    task.resolved_action = 'some_action'

    new_task = task.copy()

    assert new_task._parent is None
    assert new_task._role == 'some_role'
    assert new_task.implicit == task.implicit
    assert new_task.resolved_action == task.resolved_action
