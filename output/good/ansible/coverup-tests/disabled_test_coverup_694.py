# file lib/ansible/playbook/task_include.py:104-107
# lines [104, 105, 106, 107]
# branches []

import pytest
from ansible.playbook.task_include import TaskInclude

class MockTask:
    def copy(self, exclude_parent=False, exclude_tasks=False):
        # Mock copy method to return a simple object with the same attributes
        mock_copy = MockTask()
        return mock_copy

@pytest.fixture
def mock_task(mocker):
    # Mock the Task class and its copy method
    mocker.patch('ansible.playbook.task_include.Task', MockTask)

def test_task_include_copy(mock_task):
    task_include = TaskInclude()
    task_include.statically_loaded = True

    # Perform the copy
    new_task_include = task_include.copy(exclude_parent=True, exclude_tasks=True)

    # Assertions to ensure the copy has the correct attributes
    assert new_task_include.statically_loaded == task_include.statically_loaded
