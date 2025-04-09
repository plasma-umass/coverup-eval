# file: lib/ansible/playbook/task_include.py:104-107
# asked: {"lines": [104, 105, 106, 107], "branches": []}
# gained: {"lines": [104, 105, 106, 107], "branches": []}

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task

class MockTask(Task):
    def __init__(self, block=None, role=None, task_include=None):
        super(MockTask, self).__init__(block=block, role=role, task_include=task_include)
        self.statically_loaded = False

    def copy(self, exclude_parent=False, exclude_tasks=False):
        new_me = super(MockTask, self).copy(exclude_parent=exclude_parent, exclude_tasks=exclude_tasks)
        new_me.statically_loaded = self.statically_loaded
        return new_me

@pytest.fixture
def mock_task():
    return MockTask()

@pytest.fixture
def task_include(mock_task):
    return TaskInclude(task_include=mock_task)

def test_copy_method(task_include):
    # Test without excluding parent and tasks
    copied_task = task_include.copy()
    assert copied_task.statically_loaded == task_include.statically_loaded

    # Test with excluding parent
    copied_task_exclude_parent = task_include.copy(exclude_parent=True)
    assert copied_task_exclude_parent.statically_loaded == task_include.statically_loaded

    # Test with excluding tasks
    copied_task_exclude_tasks = task_include.copy(exclude_tasks=True)
    assert copied_task_exclude_tasks.statically_loaded == task_include.statically_loaded

    # Test with excluding both parent and tasks
    copied_task_exclude_both = task_include.copy(exclude_parent=True, exclude_tasks=True)
    assert copied_task_exclude_both.statically_loaded == task_include.statically_loaded
