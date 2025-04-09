# file lib/ansible/executor/task_result.py:53-63
# lines [53, 55, 56, 59, 60, 63]
# branches ['55->56', '55->63', '59->60', '59->63']

import pytest
from ansible.executor.task_result import TaskResult

# Mock TaskResult class to add _result attribute
class MockTaskResult(TaskResult):
    def __init__(self, result):
        self._result = result

@pytest.fixture
def task_result():
    # Fixture to create a TaskResult object with empty result
    return MockTaskResult({})

def test_is_skipped_with_empty_results(task_result):
    assert not task_result.is_skipped(), "Task should not be skipped with empty results"

def test_is_skipped_with_non_skipped_results(task_result):
    task_result._result['results'] = [{'skipped': False}]
    assert not task_result.is_skipped(), "Task should not be skipped if any item is not skipped"

def test_is_skipped_with_all_skipped_results(task_result):
    task_result._result['results'] = [{'skipped': True}, {'skipped': True}]
    assert task_result.is_skipped(), "Task should be skipped if all items are skipped"

def test_is_skipped_with_mixed_results(task_result):
    task_result._result['results'] = [{'skipped': True}, {'skipped': False}]
    assert not task_result.is_skipped(), "Task should not be skipped if not all items are skipped"

def test_is_skipped_with_non_dict_results(task_result):
    task_result._result['results'] = ['some string', 'another string']
    assert not task_result.is_skipped(), "Task should not be skipped if results are not dicts"

def test_is_skipped_with_skipped_non_dict_results(task_result):
    task_result._result['skipped'] = True
    assert task_result.is_skipped(), "Task should be skipped if skipped key is True"

def test_is_skipped_with_non_skipped_non_dict_results(task_result):
    task_result._result['skipped'] = False
    assert not task_result.is_skipped(), "Task should not be skipped if skipped key is False"
