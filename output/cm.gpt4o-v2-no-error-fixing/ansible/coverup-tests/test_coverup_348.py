# file: lib/ansible/executor/task_result.py:65-70
# asked: {"lines": [65, 66, 67, 68, 70], "branches": [[66, 68], [66, 70]]}
# gained: {"lines": [65, 66, 67, 68, 70], "branches": [[66, 68], [66, 70]]}

import pytest
from ansible.executor.task_result import TaskResult

class MockHost:
    pass

class MockTask:
    pass

@pytest.fixture
def task_result_factory():
    def _create_task_result(result_data):
        return TaskResult(MockHost(), MockTask(), result_data)
    return _create_task_result

def test_is_failed_with_failed_when_result(task_result_factory):
    result_data = {'failed_when_result': True}
    task_result = task_result_factory(result_data)
    assert task_result.is_failed() == True

def test_is_failed_with_results_containing_failed_when_result(task_result_factory):
    result_data = {'results': [{'failed_when_result': True}]}
    task_result = task_result_factory(result_data)
    assert task_result.is_failed() == True

def test_is_failed_without_failed_when_result(task_result_factory):
    result_data = {'failed': True}
    task_result = task_result_factory(result_data)
    assert task_result.is_failed() == True

def test_is_failed_without_failed_key(task_result_factory):
    result_data = {}
    task_result = task_result_factory(result_data)
    assert task_result.is_failed() == False
