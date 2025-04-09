# file: lib/ansible/playbook/task_include.py:104-107
# asked: {"lines": [105, 106, 107], "branches": []}
# gained: {"lines": [105, 106, 107], "branches": []}

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task

class MockTask(Task):
    def __init__(self):
        self.statically_loaded = False

@pytest.fixture
def mock_task():
    return MockTask()

def test_task_include_copy(mock_task, monkeypatch):
    # Mock the super().copy method to return a new instance of TaskInclude
    def mock_copy(self, exclude_parent=False, exclude_tasks=False):
        new_instance = TaskInclude()
        new_instance.statically_loaded = self.statically_loaded
        return new_instance

    monkeypatch.setattr(Task, 'copy', mock_copy)

    task_include = TaskInclude()
    task_include.statically_loaded = True

    # Perform the copy
    new_task_include = task_include.copy()

    # Assertions to verify the postconditions
    assert isinstance(new_task_include, TaskInclude)
    assert new_task_include.statically_loaded == task_include.statically_loaded
