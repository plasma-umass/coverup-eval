# file lib/ansible/playbook/task_include.py:104-107
# lines [104, 105, 106, 107]
# branches []

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task

@pytest.fixture
def mock_task(mocker):
    mock_task = mocker.patch('ansible.playbook.task.Task', autospec=True)
    return mock_task

class MockTask(Task):
    def __init__(self, *args, **kwargs):
        pass

    def copy(self, exclude_parent=False, exclude_tasks=False):
        return MockTask()

def test_task_include_copy(mocker):
    # Patch the Task class with MockTask
    mocker.patch('ansible.playbook.task_include.Task', MockTask)

    # Create an instance of TaskInclude
    task_include = TaskInclude()
    task_include.statically_loaded = True

    # Call the copy method
    new_task_include = task_include.copy()

    # Assertions to verify the postconditions
    assert new_task_include.statically_loaded == task_include.statically_loaded
