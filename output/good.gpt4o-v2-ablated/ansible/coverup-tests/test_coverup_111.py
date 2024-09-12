# file: lib/ansible/executor/task_result.py:32-44
# asked: {"lines": [32, 33, 34, 36, 37, 39, 41, 42, 44], "branches": [[36, 37], [36, 39], [41, 42], [41, 44]]}
# gained: {"lines": [32, 33, 34, 36, 37, 39, 41, 42, 44], "branches": [[36, 37], [36, 39], [41, 42], [41, 44]]}

import pytest
from ansible.executor.task_result import TaskResult
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def mock_dataloader(mocker):
    return mocker.patch('ansible.executor.task_result.DataLoader')

def test_task_result_with_dict_return_data():
    host = 'localhost'
    task = 'dummy_task'
    return_data = {'key': 'value'}
    task_fields = {'field': 'value'}

    result = TaskResult(host, task, return_data, task_fields)

    assert result._host == host
    assert result._task == task
    assert result._result == return_data
    assert result._task_fields == task_fields

def test_task_result_with_non_dict_return_data(mock_dataloader):
    host = 'localhost'
    task = 'dummy_task'
    return_data = 'some_data'
    task_fields = {'field': 'value'}

    mock_dataloader.return_value.load.return_value = {'loaded_key': 'loaded_value'}

    result = TaskResult(host, task, return_data, task_fields)

    mock_dataloader.return_value.load.assert_called_once_with(return_data)
    assert result._host == host
    assert result._task == task
    assert result._result == {'loaded_key': 'loaded_value'}
    assert result._task_fields == task_fields

def test_task_result_with_none_task_fields():
    host = 'localhost'
    task = 'dummy_task'
    return_data = {'key': 'value'}

    result = TaskResult(host, task, return_data)

    assert result._host == host
    assert result._task == task
    assert result._result == return_data
    assert result._task_fields == {}
