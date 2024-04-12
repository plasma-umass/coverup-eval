# file lib/ansible/playbook/task_include.py:104-107
# lines [105, 106, 107]
# branches []

import pytest
from ansible.playbook.task_include import TaskInclude

# Assuming the Task class has a copy method that we need to mock
class MockTask:
    def __init__(self, *args, **kwargs):
        pass

    def copy(self, exclude_parent=False, exclude_tasks=False):
        return MockTask()

@pytest.fixture
def mock_super(mocker):
    mocker.patch('ansible.playbook.task_include.super', return_value=MockTask())

def test_task_include_copy(mock_super):
    task_include = TaskInclude()
    task_include.statically_loaded = True

    # Perform the copy
    new_task_include = task_include.copy()

    # Assertions to check if the copy has the same statically_loaded value
    assert new_task_include.statically_loaded == task_include.statically_loaded

    # Clean up is handled by pytest-mock through the mocker fixture
