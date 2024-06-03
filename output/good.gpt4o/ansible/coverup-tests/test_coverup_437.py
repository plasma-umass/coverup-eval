# file lib/ansible/executor/task_result.py:53-63
# lines [53, 55, 56, 59, 60, 63]
# branches ['55->56', '55->63', '59->60', '59->63']

import pytest
from unittest.mock import MagicMock

# Assuming the TaskResult class is imported from ansible.executor.task_result
from ansible.executor.task_result import TaskResult

@pytest.fixture
def task_result():
    # Mocking the required arguments for TaskResult
    host = MagicMock()
    task = MagicMock()
    return_data = "{}"  # Providing a valid JSON string
    return TaskResult(host, task, return_data)

def test_is_skipped_with_loop_results_all_skipped(task_result):
    task_result._result = {
        'results': [
            {'skipped': True},
            {'skipped': True},
            {'skipped': True}
        ]
    }
    assert task_result.is_skipped() is True

def test_is_skipped_with_loop_results_not_all_skipped(task_result):
    task_result._result = {
        'results': [
            {'skipped': True},
            {'skipped': False},
            {'skipped': True}
        ]
    }
    assert task_result.is_skipped() is False

def test_is_skipped_with_non_dict_results(task_result):
    task_result._result = {
        'results': [
            'non-dict-result',
            'another-non-dict-result'
        ]
    }
    assert task_result.is_skipped() is False

def test_is_skipped_with_regular_task_skipped(task_result):
    task_result._result = {
        'skipped': True
    }
    assert task_result.is_skipped() is True

def test_is_skipped_with_regular_task_not_skipped(task_result):
    task_result._result = {
        'skipped': False
    }
    assert task_result.is_skipped() is False
