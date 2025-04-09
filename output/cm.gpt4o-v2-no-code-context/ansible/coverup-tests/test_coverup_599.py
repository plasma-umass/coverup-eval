# file: lib/ansible/playbook/task.py:136-139
# asked: {"lines": [136, 137, 138, 139], "branches": []}
# gained: {"lines": [136, 137, 138, 139], "branches": []}

import pytest
from ansible.playbook.task import Task

@pytest.fixture
def mock_task(mocker):
    mocker.patch('ansible.playbook.task.Task.load_data', return_value='mocked_load_data')
    return Task

def test_task_load(mock_task):
    data = {'some': 'data'}
    block = 'block'
    role = 'role'
    task_include = 'task_include'
    variable_manager = 'variable_manager'
    loader = 'loader'

    result = mock_task.load(data, block, role, task_include, variable_manager, loader)

    assert result == 'mocked_load_data'
    mock_task.load_data.assert_called_once_with(data, variable_manager=variable_manager, loader=loader)
