# file: lib/ansible/executor/task_result.py:53-63
# asked: {"lines": [53, 55, 56, 59, 60, 63], "branches": [[55, 56], [55, 63], [59, 60], [59, 63]]}
# gained: {"lines": [53, 55, 56, 59, 60, 63], "branches": [[55, 56], [55, 63], [59, 60], [59, 63]]}

import pytest
from ansible.executor.task_result import TaskResult

@pytest.fixture
def task_result_factory():
    def _factory(result):
        return TaskResult(host="localhost", task=None, return_data=result)
    return _factory

def test_is_skipped_with_results_all_skipped(task_result_factory):
    result_data = {
        'results': [
            {'skipped': True},
            {'skipped': True}
        ]
    }
    task_result = task_result_factory(result_data)
    assert task_result.is_skipped() is True

def test_is_skipped_with_results_not_all_skipped(task_result_factory):
    result_data = {
        'results': [
            {'skipped': True},
            {'skipped': False}
        ]
    }
    task_result = task_result_factory(result_data)
    assert task_result.is_skipped() is False

def test_is_skipped_with_no_results_key(task_result_factory):
    result_data = {
        'skipped': True
    }
    task_result = task_result_factory(result_data)
    assert task_result.is_skipped() is True

def test_is_skipped_with_no_skipped_key(task_result_factory):
    result_data = {
        'some_key': 'some_value'
    }
    task_result = task_result_factory(result_data)
    assert task_result.is_skipped() is False
