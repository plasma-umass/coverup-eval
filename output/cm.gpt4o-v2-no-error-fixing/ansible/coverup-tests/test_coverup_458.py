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

def test_task_include_copy():
    original_task = MockTask()
    original_task.statically_loaded = True

    task_include = TaskInclude()
    task_include.statically_loaded = original_task.statically_loaded

    copied_task = task_include.copy()

    assert copied_task.statically_loaded == original_task.statically_loaded
    assert copied_task is not task_include
