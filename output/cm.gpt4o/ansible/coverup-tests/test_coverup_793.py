# file lib/ansible/executor/task_result.py:50-51
# lines [50, 51]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the TaskResult class is defined in ansible.executor.task_result
from ansible.executor.task_result import TaskResult

@pytest.fixture
def task_result():
    # Create a mock TaskResult object with required arguments
    task_result = TaskResult(host='localhost', task='dummy_task', return_data={})
    task_result._check_key = MagicMock()
    return task_result

def test_is_changed(task_result):
    # Test when _check_key returns True
    task_result._check_key.return_value = True
    assert task_result.is_changed() == True
    task_result._check_key.assert_called_once_with('changed')

    # Reset mock
    task_result._check_key.reset_mock()

    # Test when _check_key returns False
    task_result._check_key.return_value = False
    assert task_result.is_changed() == False
    task_result._check_key.assert_called_once_with('changed')
