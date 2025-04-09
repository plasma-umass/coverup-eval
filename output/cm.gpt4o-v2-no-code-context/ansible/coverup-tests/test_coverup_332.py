# file: lib/ansible/playbook/task.py:491-497
# asked: {"lines": [491, 492, 493, 494, 495, 496, 497], "branches": [[493, 494], [493, 497], [494, 495], [494, 496]]}
# gained: {"lines": [491, 492, 493, 494, 495, 496, 497], "branches": [[493, 494], [493, 497], [494, 495], [494, 496]]}

import pytest
from unittest.mock import Mock, patch

# Assuming Task, TaskInclude, and other dependencies are imported correctly
from ansible.playbook.task import Task
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def task_with_parent():
    parent_task = Mock(spec=TaskInclude)
    task = Task()
    task._parent = parent_task
    return task

@pytest.fixture
def task_with_non_include_parent():
    non_include_parent = Mock(spec=Task)
    non_include_parent.get_first_parent_include = Mock(return_value=None)
    task = Task()
    task._parent = non_include_parent
    return task

@pytest.fixture
def task_without_parent():
    task = Task()
    task._parent = None
    return task

def test_get_first_parent_include_with_include_parent(task_with_parent):
    result = task_with_parent.get_first_parent_include()
    assert result == task_with_parent._parent

def test_get_first_parent_include_with_non_include_parent(task_with_non_include_parent):
    result = task_with_non_include_parent.get_first_parent_include()
    assert result is None
    task_with_non_include_parent._parent.get_first_parent_include.assert_called_once()

def test_get_first_parent_include_without_parent(task_without_parent):
    result = task_without_parent.get_first_parent_include()
    assert result is None
