# file lib/ansible/playbook/task.py:378-392
# lines [383, 387]
# branches ['382->383', '386->387']

import pytest
from unittest.mock import Mock
from ansible.playbook.task import Task

def test_task_copy_with_parent_and_role():
    # Create a mock parent and role
    mock_parent = Mock()
    mock_role = Mock()

    # Set up the mock parent to return a copy when copy() is called
    mock_parent.copy.return_value = mock_parent

    # Create a Task instance with the mock parent and role
    task = Task()
    task._parent = mock_parent
    task._role = mock_role

    # Call the copy method with exclude_parent=False and exclude_tasks=False
    new_task = task.copy(exclude_parent=False, exclude_tasks=False)

    # Assert that the new task's parent is a copy of the original task's parent
    assert new_task._parent == mock_parent
    mock_parent.copy.assert_called_once_with(exclude_tasks=False)

    # Assert that the new task's role is the same as the original task's role
    assert new_task._role == mock_role

def test_task_copy_without_parent_and_role():
    # Create a Task instance without parent and role
    task = Task()
    task._parent = None
    task._role = None

    # Call the copy method
    new_task = task.copy()

    # Assert that the new task's parent is None
    assert new_task._parent is None

    # Assert that the new task's role is None
    assert new_task._role is None
