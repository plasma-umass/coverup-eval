# file: lib/ansible/playbook/task.py:136-139
# asked: {"lines": [136, 137, 138, 139], "branches": []}
# gained: {"lines": [136, 137, 138, 139], "branches": []}

import pytest
from ansible.playbook.task import Task

@pytest.fixture
def mock_task_data():
    return {
        'name': 'test_task',
        'action': 'debug',
        'args': {'msg': 'Hello World'}
    }

def test_task_load(mock_task_data, mocker):
    mock_load_data = mocker.patch.object(Task, 'load_data', return_value='loaded_data')
    
    result = Task.load(mock_task_data)
    
    assert result == 'loaded_data'
    mock_load_data.assert_called_once_with(mock_task_data, variable_manager=None, loader=None)

def test_task_load_with_params(mock_task_data, mocker):
    mock_load_data = mocker.patch.object(Task, 'load_data', return_value='loaded_data')
    mock_block = mocker.Mock()
    mock_role = mocker.Mock()
    mock_task_include = mocker.Mock()
    mock_variable_manager = mocker.Mock()
    mock_loader = mocker.Mock()
    
    result = Task.load(mock_task_data, block=mock_block, role=mock_role, task_include=mock_task_include, variable_manager=mock_variable_manager, loader=mock_loader)
    
    assert result == 'loaded_data'
    mock_load_data.assert_called_once_with(mock_task_data, variable_manager=mock_variable_manager, loader=mock_loader)
