# file: lib/ansible/executor/task_result.py:65-70
# asked: {"lines": [65, 66, 67, 68, 70], "branches": [[66, 68], [66, 70]]}
# gained: {"lines": [65, 66, 67, 68, 70], "branches": [[66, 68], [66, 70]]}

import pytest
from ansible.executor.task_result import TaskResult

class MockTask:
    pass

class MockHost:
    pass

@pytest.fixture
def task_result_factory():
    def _factory(result_data):
        return TaskResult(MockHost(), MockTask(), result_data)
    return _factory

def test_is_failed_with_failed_when_result(task_result_factory, mocker):
    result_data = {
        'failed_when_result': True,
        'failed': False
    }
    task_result = task_result_factory(result_data)
    mock_check_key = mocker.patch.object(task_result, '_check_key', return_value=True)
    
    assert task_result.is_failed() is True
    mock_check_key.assert_called_once_with('failed_when_result')

def test_is_failed_with_results_containing_failed_when_result(task_result_factory, mocker):
    result_data = {
        'results': [{'failed_when_result': True}],
        'failed': False
    }
    task_result = task_result_factory(result_data)
    mock_check_key = mocker.patch.object(task_result, '_check_key', return_value=True)
    
    assert task_result.is_failed() is True
    mock_check_key.assert_called_once_with('failed_when_result')

def test_is_failed_without_failed_when_result(task_result_factory, mocker):
    result_data = {
        'failed': True
    }
    task_result = task_result_factory(result_data)
    mock_check_key = mocker.patch.object(task_result, '_check_key', return_value=True)
    
    assert task_result.is_failed() is True
    mock_check_key.assert_called_once_with('failed')
