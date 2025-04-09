# file: lib/ansible/executor/task_result.py:32-44
# asked: {"lines": [32, 33, 34, 36, 37, 39, 41, 42, 44], "branches": [[36, 37], [36, 39], [41, 42], [41, 44]]}
# gained: {"lines": [32, 33, 34, 36, 37, 39, 41, 42, 44], "branches": [[36, 37], [36, 39], [41, 42], [41, 44]]}

import pytest
from ansible.executor.task_result import TaskResult
from ansible.parsing.dataloader import DataLoader

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

def test_task_result_with_non_dict_return_data(monkeypatch):
    host = 'localhost'
    task = 'dummy_task'
    return_data = 'some_non_dict_data'
    task_fields = {'field': 'value'}

    class MockDataLoader:
        def load(self, data):
            return {'loaded_key': 'loaded_value'}

    monkeypatch.setattr('ansible.executor.task_result.DataLoader', MockDataLoader)

    result = TaskResult(host, task, return_data, task_fields)

    assert result._host == host
    assert result._task == task
    assert result._result == {'loaded_key': 'loaded_value'}
    assert result._task_fields == task_fields

def test_task_result_with_default_task_fields():
    host = 'localhost'
    task = 'dummy_task'
    return_data = {'key': 'value'}

    result = TaskResult(host, task, return_data)

    assert result._host == host
    assert result._task == task
    assert result._result == return_data
    assert result._task_fields == {}
