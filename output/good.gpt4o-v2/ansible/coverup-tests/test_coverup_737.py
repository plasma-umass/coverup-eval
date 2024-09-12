# file: lib/ansible/executor/task_result.py:46-48
# asked: {"lines": [46, 47, 48], "branches": []}
# gained: {"lines": [46, 47, 48], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.executor.task_result import TaskResult

@pytest.fixture
def mock_task():
    task = Mock()
    task.get_name = Mock(return_value="default_task_name")
    return task

def test_task_name_with_task_fields(mock_task):
    task_fields = {'name': 'test_task'}
    result = TaskResult(host="localhost", task=mock_task, return_data={}, task_fields=task_fields)
    assert result.task_name == 'test_task'

def test_task_name_without_task_fields(mock_task):
    result = TaskResult(host="localhost", task=mock_task, return_data={}, task_fields={})
    assert result.task_name == 'default_task_name'

def test_task_name_with_none_task_fields(mock_task):
    result = TaskResult(host="localhost", task=mock_task, return_data={}, task_fields=None)
    assert result.task_name == 'default_task_name'
