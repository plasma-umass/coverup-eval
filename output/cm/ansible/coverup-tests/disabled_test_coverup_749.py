# file lib/ansible/playbook/task_include.py:49-51
# lines [49, 50, 51]
# branches []

import pytest
from ansible.playbook.task_include import TaskInclude

# Assuming the existence of the Task class in the same module or imported appropriately
# If not, the Task class needs to be imported or mocked

# Mocking the Task class if it's not available
class MockTask:
    def __init__(self, block=None, role=None, task_include=None):
        self.block = block
        self.role = role
        self.task_include = task_include

# Replace the following line with an actual import if the Task class is available
# from ansible.playbook.task import Task

@pytest.fixture
def mock_task(mocker):
    mocker.patch('ansible.playbook.task_include.Task', new=MockTask)

def test_task_include_initialization(mock_task):
    block = object()
    role = object()
    task_include = object()

    task_include_instance = TaskInclude(block=block, role=role, task_include=task_include)

    assert task_include_instance.statically_loaded is False
    # The following assertions are removed because the TaskInclude class does not have these attributes
    # Instead, we should assert the attributes of the MockTask if necessary
