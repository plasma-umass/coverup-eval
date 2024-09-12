# file: lib/ansible/playbook/handler_task_include.py:27-39
# asked: {"lines": [27, 29, 31, 32, 33, 34, 35, 36, 39], "branches": []}
# gained: {"lines": [27, 29, 31, 32, 33, 34, 35, 36, 39], "branches": []}

import pytest
from ansible.playbook.handler_task_include import HandlerTaskInclude
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.handler import Handler

@pytest.fixture
def mock_task_include(mocker):
    mock_task_include = mocker.patch('ansible.playbook.handler_task_include.TaskInclude')
    mock_task_include.VALID_INCLUDE_KEYWORDS = {'include', 'import_tasks'}
    return mock_task_include

@pytest.fixture
def mock_handler(mocker):
    return mocker.patch('ansible.playbook.handler_task_include.Handler')

def test_handler_task_include_valid_keywords(mock_task_include):
    assert 'listen' in HandlerTaskInclude.VALID_INCLUDE_KEYWORDS

def test_handler_task_include_load(mocker, mock_task_include, mock_handler):
    data = {'some': 'data'}
    block = mocker.Mock()
    role = mocker.Mock()
    task_include = mocker.Mock()
    variable_manager = mocker.Mock()
    loader = mocker.Mock()

    mock_check_options = mocker.patch.object(HandlerTaskInclude, 'check_options', return_value='handler')
    mock_load_data = mocker.patch.object(HandlerTaskInclude, 'load_data', return_value='loaded_data')

    handler = HandlerTaskInclude.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)

    mock_load_data.assert_called_once_with(data, variable_manager=variable_manager, loader=loader)
    mock_check_options.assert_called_once_with('loaded_data', data)
    assert handler == 'handler'
