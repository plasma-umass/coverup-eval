# file: lib/ansible/executor/task_result.py:32-44
# asked: {"lines": [32, 33, 34, 36, 37, 39, 41, 42, 44], "branches": [[36, 37], [36, 39], [41, 42], [41, 44]]}
# gained: {"lines": [32, 33, 34, 36, 37, 39, 41, 42, 44], "branches": [[36, 37], [36, 39], [41, 42], [41, 44]]}

import pytest
from ansible.executor.task_result import TaskResult
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def mock_dataloader_load(mocker):
    return mocker.patch.object(DataLoader, 'load', return_value={'mocked_key': 'mocked_value'})

def test_task_result_with_dict_return_data():
    host = 'localhost'
    task = 'dummy_task'
    return_data = {'key': 'value'}
    task_result = TaskResult(host, task, return_data)
    
    assert task_result._host == host
    assert task_result._task == task
    assert task_result._result == return_data
    assert task_result._task_fields == {}

def test_task_result_with_non_dict_return_data(mock_dataloader_load):
    host = 'localhost'
    task = 'dummy_task'
    return_data = 'key: value'
    task_result = TaskResult(host, task, return_data)
    
    assert task_result._host == host
    assert task_result._task == task
    assert task_result._result == {'mocked_key': 'mocked_value'}
    assert task_result._task_fields == {}

def test_task_result_with_task_fields():
    host = 'localhost'
    task = 'dummy_task'
    return_data = {'key': 'value'}
    task_fields = {'field_key': 'field_value'}
    task_result = TaskResult(host, task, return_data, task_fields)
    
    assert task_result._host == host
    assert task_result._task == task
    assert task_result._result == return_data
    assert task_result._task_fields == task_fields
