# file lib/ansible/playbook/task.py:136-139
# lines [136, 137, 138, 139]
# branches []

import pytest
from ansible.playbook.task import Task

def test_task_load(mocker):
    # Mock the dependencies
    mock_block = mocker.Mock()
    mock_role = mocker.Mock()
    mock_task_include = mocker.Mock()
    mock_variable_manager = mocker.Mock()
    mock_loader = mocker.Mock()
    
    # Mock the data to be loaded
    data = {'some_key': 'some_value'}
    
    # Mock the load_data method to ensure it is called
    mock_load_data = mocker.patch.object(Task, 'load_data', return_value='mocked_result')
    
    # Call the static method
    result = Task.load(data, block=mock_block, role=mock_role, task_include=mock_task_include, variable_manager=mock_variable_manager, loader=mock_loader)
    
    # Assertions to verify the behavior
    assert result == 'mocked_result'
    mock_load_data.assert_called_once_with(data, variable_manager=mock_variable_manager, loader=mock_loader)
    
    # Clean up
    mocker.stopall()
