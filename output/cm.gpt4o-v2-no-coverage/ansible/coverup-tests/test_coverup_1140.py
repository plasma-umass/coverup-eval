# file: lib/ansible/playbook/task.py:491-497
# asked: {"lines": [492, 493, 494, 495, 496, 497], "branches": [[493, 494], [493, 497], [494, 495], [494, 496]]}
# gained: {"lines": [492, 493, 494, 495, 496, 497], "branches": [[493, 494], [493, 497], [494, 495], [494, 496]]}

import pytest
from ansible.playbook.task import Task
from ansible.playbook.task_include import TaskInclude

class MockParent:
    def get_first_parent_include(self):
        return "parent_include"

@pytest.fixture
def task_with_parent():
    parent = MockParent()
    task = Task(block=None, role=None, task_include=None)
    task._parent = parent
    return task

@pytest.fixture
def task_with_task_include_parent():
    parent = TaskInclude()
    task = Task(block=None, role=None, task_include=parent)
    return task

def test_get_first_parent_include_with_no_parent():
    task = Task(block=None, role=None, task_include=None)
    assert task.get_first_parent_include() is None

def test_get_first_parent_include_with_parent(task_with_parent):
    assert task_with_parent.get_first_parent_include() == "parent_include"

def test_get_first_parent_include_with_task_include_parent(task_with_task_include_parent):
    assert task_with_task_include_parent.get_first_parent_include() == task_with_task_include_parent._parent
