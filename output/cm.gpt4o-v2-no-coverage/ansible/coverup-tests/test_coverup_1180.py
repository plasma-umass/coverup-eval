# file: lib/ansible/playbook/handler_task_include.py:27-39
# asked: {"lines": [33, 34, 35, 36, 39], "branches": []}
# gained: {"lines": [33, 34, 35, 36, 39], "branches": []}

import pytest
from ansible.playbook.handler_task_include import HandlerTaskInclude
from ansible.playbook.handler import Handler
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def mock_handler_task_include(mocker):
    mocker.patch('ansible.playbook.handler_task_include.HandlerTaskInclude.load_data', return_value={'some': 'data'})
    mocker.patch('ansible.playbook.handler_task_include.HandlerTaskInclude.check_options', return_value='handler')
    return HandlerTaskInclude

def test_handler_task_include_load(mock_handler_task_include):
    data = {'key': 'value'}
    block = 'block'
    role = 'role'
    task_include = 'task_include'
    variable_manager = 'variable_manager'
    loader = 'loader'

    result = mock_handler_task_include.load(data, block, role, task_include, variable_manager, loader)

    assert result == 'handler'
    mock_handler_task_include.load_data.assert_called_once_with(data, variable_manager=variable_manager, loader=loader)
    mock_handler_task_include.check_options.assert_called_once_with({'some': 'data'}, data)
