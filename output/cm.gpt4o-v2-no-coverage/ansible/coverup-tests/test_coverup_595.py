# file: lib/ansible/executor/task_result.py:65-70
# asked: {"lines": [65, 66, 67, 68, 70], "branches": [[66, 68], [66, 70]]}
# gained: {"lines": [65, 66, 67, 68, 70], "branches": [[66, 68], [66, 70]]}

import pytest
from unittest.mock import MagicMock
from ansible.executor.task_result import TaskResult

@pytest.fixture
def task_result():
    host = MagicMock()
    task = MagicMock()
    return_data = {}
    return TaskResult(host, task, return_data)

def test_is_failed_with_failed_when_result(task_result, mocker):
    task_result._result = {'failed_when_result': True}
    mock_check_key = mocker.patch.object(task_result, '_check_key', return_value=True)
    
    assert task_result.is_failed() is True
    mock_check_key.assert_called_once_with('failed_when_result')

def test_is_failed_with_results_containing_failed_when_result(task_result, mocker):
    task_result._result = {'results': [{'failed_when_result': True}]}
    mock_check_key = mocker.patch.object(task_result, '_check_key', return_value=True)
    
    assert task_result.is_failed() is True
    mock_check_key.assert_called_once_with('failed_when_result')

def test_is_failed_with_failed_key(task_result, mocker):
    task_result._result = {'failed': True}
    mock_check_key = mocker.patch.object(task_result, '_check_key', return_value=True)
    
    assert task_result.is_failed() is True
    mock_check_key.assert_called_once_with('failed')

def test_is_failed_with_no_failure(task_result, mocker):
    task_result._result = {}
    mock_check_key = mocker.patch.object(task_result, '_check_key', return_value=False)
    
    assert task_result.is_failed() is False
    mock_check_key.assert_called_once_with('failed')
