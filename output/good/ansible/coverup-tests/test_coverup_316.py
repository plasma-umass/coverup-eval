# file lib/ansible/executor/task_result.py:32-44
# lines [32, 33, 34, 36, 37, 39, 41, 42, 44]
# branches ['36->37', '36->39', '41->42', '41->44']

import pytest
from ansible.executor.task_result import TaskResult
from ansible.parsing.dataloader import DataLoader

# Mock classes to simulate the host and task objects
class MockHost:
    pass

class MockTask:
    pass

@pytest.fixture
def mock_host():
    return MockHost()

@pytest.fixture
def mock_task():
    return MockTask()

@pytest.fixture
def data_loader(mocker):
    return mocker.patch.object(DataLoader, 'load', return_value={'loaded': True})

def test_task_result_with_dict_return_data(mock_host, mock_task):
    return_data = {'key': 'value'}
    task_result = TaskResult(mock_host, mock_task, return_data)
    assert task_result._result == return_data
    assert task_result._task_fields == {}

def test_task_result_with_non_dict_return_data(mock_host, mock_task, data_loader):
    return_data = '{"key": "value"}'
    task_result = TaskResult(mock_host, mock_task, return_data)
    assert task_result._result == {'loaded': True}
    assert task_result._task_fields == {}
    data_loader.assert_called_once_with(return_data)

def test_task_result_with_task_fields(mock_host, mock_task):
    return_data = {'key': 'value'}
    task_fields = {'extra': 'info'}
    task_result = TaskResult(mock_host, mock_task, return_data, task_fields)
    assert task_result._result == return_data
    assert task_result._task_fields == task_fields
