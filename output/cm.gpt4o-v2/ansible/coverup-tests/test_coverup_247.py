# file: lib/ansible/playbook/task.py:378-392
# asked: {"lines": [378, 379, 381, 382, 383, 385, 386, 387, 389, 390, 392], "branches": [[382, 383], [382, 385], [386, 387], [386, 389]]}
# gained: {"lines": [378, 379, 381, 382, 383, 385, 386, 387, 389, 390, 392], "branches": [[382, 383], [382, 385], [386, 387], [386, 389]]}

import pytest
from ansible.playbook.task import Task

class MockParent:
    def copy(self, exclude_tasks=False):
        return MockParent()

class MockRole:
    pass

@pytest.fixture
def task_with_parent_and_role():
    parent = MockParent()
    role = MockRole()
    task = Task(block=parent, role=role)
    return task

@pytest.fixture
def task_with_parent():
    parent = MockParent()
    task = Task(block=parent)
    return task

@pytest.fixture
def task_with_role():
    role = MockRole()
    task = Task(role=role)
    return task

@pytest.fixture
def task_without_parent_or_role():
    task = Task()
    return task

def test_copy_with_parent_and_role(task_with_parent_and_role):
    new_task = task_with_parent_and_role.copy()
    assert new_task._parent is not None
    assert new_task._role is not None
    assert new_task.implicit == task_with_parent_and_role.implicit
    assert new_task.resolved_action == task_with_parent_and_role.resolved_action

def test_copy_with_parent(task_with_parent):
    new_task = task_with_parent.copy()
    assert new_task._parent is not None
    assert new_task._role is None
    assert new_task.implicit == task_with_parent.implicit
    assert new_task.resolved_action == task_with_parent.resolved_action

def test_copy_with_role(task_with_role):
    new_task = task_with_role.copy()
    assert new_task._parent is None
    assert new_task._role is not None
    assert new_task.implicit == task_with_role.implicit
    assert new_task.resolved_action == task_with_role.resolved_action

def test_copy_without_parent_or_role(task_without_parent_or_role):
    new_task = task_without_parent_or_role.copy()
    assert new_task._parent is None
    assert new_task._role is None
    assert new_task.implicit == task_without_parent_or_role.implicit
    assert new_task.resolved_action == task_without_parent_or_role.resolved_action
