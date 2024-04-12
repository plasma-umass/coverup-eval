# file lib/ansible/executor/task_result.py:65-70
# lines [65, 66, 67, 68, 70]
# branches ['66->68', '66->70']

import pytest
from ansible.executor.task_result import TaskResult

# Mock class to represent the TaskResult with a _result attribute
class MockTaskResult(TaskResult):
    def __init__(self, result):
        self._result = result

    def _check_key(self, key):
        if key == 'failed_when_result':
            if 'results' in self._result:
                return any('failed_when_result' in x for x in self._result['results'])
            return self._result.get(key, False)
        return self._result.get(key, False)

# No need for a fixture to mock TaskResult since we are using a subclass

def test_is_failed_with_failed_when_result():
    # Test case where 'failed_when_result' is in the result
    result = {'failed_when_result': True}
    task_result = MockTaskResult(result)
    assert task_result.is_failed() == True

def test_is_failed_with_results_containing_failed_when_result():
    # Test case where 'results' contains an item with 'failed_when_result'
    result = {'results': [{'failed_when_result': True}]}
    task_result = MockTaskResult(result)
    assert task_result.is_failed() == True

def test_is_failed_without_failed_when_result():
    # Test case where neither 'failed_when_result' nor 'results' are in the result
    result = {'failed': True}
    task_result = MockTaskResult(result)
    assert task_result.is_failed() == True

def test_is_failed_with_empty_results():
    # Test case where 'results' is empty
    result = {'results': []}
    task_result = MockTaskResult(result)
    assert task_result.is_failed() == False

def test_is_failed_with_results_not_containing_failed_when_result():
    # Test case where 'results' does not contain any item with 'failed_when_result'
    result = {'results': [{'some_other_key': True}]}
    task_result = MockTaskResult(result)
    assert task_result.is_failed() == False
