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

def test_task_include_copy(mock_task):
    task_include = TaskInclude()
    task_include.statically_loaded = True

    new_task_include = task_include.copy()

    assert new_task_include.statically_loaded == task_include.statically_loaded
    assert isinstance(new_task_include, TaskInclude)
