# file: lib/ansible/playbook/handler_task_include.py:27-39
# asked: {"lines": [27, 29, 31, 32, 33, 34, 35, 36, 39], "branches": []}
# gained: {"lines": [27, 29, 31, 32, 33, 34, 35, 36, 39], "branches": []}

import pytest
from ansible.playbook.handler_task_include import HandlerTaskInclude
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.handler import Handler

@pytest.fixture
def mock_handler_task_include(mocker):
    mocker.patch('ansible.playbook.handler_task_include.HandlerTaskInclude.__init__', return_value=None)
    mocker.patch('ansible.playbook.handler_task_include.HandlerTaskInclude.check_options', return_value='mock_handler')
    mocker.patch('ansible.playbook.handler_task_include.HandlerTaskInclude.load_data', return_value='mock_data')
    return HandlerTaskInclude

def test_handler_task_include_class():
    assert issubclass(HandlerTaskInclude, (Handler, TaskInclude))

def test_valid_include_keywords():
    assert 'listen' in HandlerTaskInclude.VALID_INCLUDE_KEYWORDS

def test_load_method(mock_handler_task_include):
    data = {'some': 'data'}
    block = 'mock_block'
    role = 'mock_role'
    task_include = 'mock_task_include'
    variable_manager = 'mock_variable_manager'
    loader = 'mock_loader'

    handler = HandlerTaskInclude.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)
    
    assert handler == 'mock_handler'
    mock_handler_task_include.__init__.assert_called_once_with(block=block, role=role, task_include=task_include)
    mock_handler_task_include.load_data.assert_called_once_with(data, variable_manager=variable_manager, loader=loader)
    mock_handler_task_include.check_options.assert_called_once_with('mock_data', data)
