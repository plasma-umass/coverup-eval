# file lib/ansible/playbook/task_include.py:53-61
# lines [53, 54, 55, 56, 57, 58, 61]
# branches []

import pytest
from ansible.playbook.task_include import TaskInclude
from unittest.mock import Mock

@pytest.fixture
def mock_task_include(mocker):
    mocker.patch('ansible.playbook.task_include.TaskInclude.__init__', return_value=None)
    mocker.patch('ansible.playbook.task_include.TaskInclude.check_options', return_value='mock_task')
    mocker.patch('ansible.playbook.task_include.TaskInclude.load_data', return_value='mock_data')
    return TaskInclude

def test_task_include_load(mock_task_include):
    data = {'some': 'data'}
    block = Mock()
    role = Mock()
    task_include = Mock()
    variable_manager = Mock()
    loader = Mock()

    result = TaskInclude.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    assert result == 'mock_task'
    mock_task_include.__init__.assert_called_once_with(block=block, role=role, task_include=task_include)
    mock_task_include.load_data.assert_called_once_with(data, variable_manager=variable_manager, loader=loader)
    mock_task_include.check_options.assert_called_once_with('mock_data', data)
