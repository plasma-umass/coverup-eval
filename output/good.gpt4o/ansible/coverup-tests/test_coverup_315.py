# file lib/ansible/executor/task_result.py:32-44
# lines [32, 33, 34, 36, 37, 39, 41, 42, 44]
# branches ['36->37', '36->39', '41->42', '41->44']

import pytest
from unittest.mock import Mock, patch
from ansible.executor.task_result import TaskResult

@pytest.fixture
def mock_dataloader():
    with patch('ansible.executor.task_result.DataLoader') as MockDataLoader:
        yield MockDataLoader

def test_task_result_with_dict():
    host = Mock()
    task = Mock()
    return_data = {'key': 'value'}
    task_fields = {'field': 'value'}

    result = TaskResult(host, task, return_data, task_fields)

    assert result._host == host
    assert result._task == task
    assert result._result == return_data
    assert result._task_fields == task_fields

def test_task_result_with_non_dict(mock_dataloader):
    host = Mock()
    task = Mock()
    return_data = 'some_non_dict_data'
    task_fields = None

    mock_dataloader_instance = mock_dataloader.return_value
    mock_dataloader_instance.load.return_value = {'loaded_key': 'loaded_value'}

    result = TaskResult(host, task, return_data, task_fields)

    mock_dataloader_instance.load.assert_called_once_with(return_data)
    assert result._host == host
    assert result._task == task
    assert result._result == {'loaded_key': 'loaded_value'}
    assert result._task_fields == {}
