# file: lib/ansible/executor/task_result.py:53-63
# asked: {"lines": [53, 55, 56, 59, 60, 63], "branches": [[55, 56], [55, 63], [59, 60], [59, 63]]}
# gained: {"lines": [53, 55, 56, 59, 60, 63], "branches": [[55, 56], [55, 63], [59, 60], [59, 63]]}

import pytest
from ansible.executor.task_result import TaskResult

@pytest.fixture
def task_result_factory():
    def _factory(result_data):
        return TaskResult(host="localhost", task="dummy_task", return_data=result_data)
    return _factory

def test_is_skipped_with_all_skipped_results(task_result_factory):
    result_data = {
        'results': [
            {'skipped': True},
            {'skipped': True}
        ]
    }
    task_result = task_result_factory(result_data)
    assert task_result.is_skipped() is True

def test_is_skipped_with_some_skipped_results(task_result_factory):
    result_data = {
        'results': [
            {'skipped': True},
            {'skipped': False}
        ]
    }
    task_result = task_result_factory(result_data)
    assert task_result.is_skipped() is False

def test_is_skipped_with_non_dict_results(task_result_factory):
    result_data = {
        'results': [
            'non_dict_result',
            'another_non_dict_result'
        ]
    }
    task_result = task_result_factory(result_data)
    assert task_result.is_skipped() is False

def test_is_skipped_with_regular_task_skipped(task_result_factory):
    result_data = {
        'skipped': True
    }
    task_result = task_result_factory(result_data)
    assert task_result.is_skipped() is True

def test_is_skipped_with_regular_task_not_skipped(task_result_factory):
    result_data = {
        'skipped': False
    }
    task_result = task_result_factory(result_data)
    assert task_result.is_skipped() is False
