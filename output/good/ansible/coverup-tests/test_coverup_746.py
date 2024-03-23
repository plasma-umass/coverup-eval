# file lib/ansible/executor/task_result.py:46-48
# lines [46, 47, 48]
# branches []

import pytest
from ansible.executor.task_result import TaskResult

# Mocking the Task and TaskFields classes
class MockTask:
    def get_name(self):
        return "mock_task_name"

@pytest.fixture
def task_result(mocker):
    # Create a TaskResult instance with a mock task and task_fields
    mock_task = MockTask()
    mock_host = mocker.MagicMock()
    # Mock return_data should be a string that can be loaded as JSON/YAML
    mock_return_data = '{}'
    task_result = TaskResult(mock_host, mock_task, mock_return_data)
    task_result._task_fields = {}
    return task_result

def test_task_name_with_no_name_field(task_result):
    # Test the branch where 'name' is not in _task_fields
    assert task_result.task_name == "mock_task_name"

def test_task_name_with_name_field(task_result):
    # Test the branch where 'name' is in _task_fields
    task_result._task_fields['name'] = 'explicit_name'
    assert task_result.task_name == 'explicit_name'
