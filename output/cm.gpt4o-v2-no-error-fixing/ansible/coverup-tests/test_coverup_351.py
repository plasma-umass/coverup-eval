# file: lib/ansible/playbook/task_include.py:53-61
# asked: {"lines": [53, 54, 55, 56, 57, 58, 61], "branches": []}
# gained: {"lines": [53, 54, 55, 56, 57, 58, 61], "branches": []}

import pytest
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task

@pytest.fixture
def mock_task(mocker):
    mock_task = mocker.patch('ansible.playbook.task_include.TaskInclude.check_options')
    mock_task.return_value = 'mocked_task'
    return mock_task

@pytest.fixture
def mock_load_data(mocker):
    mock_load_data = mocker.patch('ansible.playbook.task_include.TaskInclude.load_data')
    mock_load_data.return_value = 'mocked_data'
    return mock_load_data

def test_task_include_load(mock_task, mock_load_data):
    data = {'some': 'data'}
    block = 'block'
    role = 'role'
    task_include = 'task_include'
    variable_manager = 'variable_manager'
    loader = 'loader'

    result = TaskInclude.load(data, block, role, task_include, variable_manager, loader)

    assert result == 'mocked_task'
    mock_load_data.assert_called_once_with(data, variable_manager=variable_manager, loader=loader)
    mock_task.assert_called_once_with('mocked_data', data)
