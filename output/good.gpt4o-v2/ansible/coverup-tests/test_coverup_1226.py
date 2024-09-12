# file: lib/ansible/playbook/handler_task_include.py:27-39
# asked: {"lines": [33, 34, 35, 36, 39], "branches": []}
# gained: {"lines": [33, 34, 35, 36, 39], "branches": []}

import pytest
from ansible.playbook.handler_task_include import HandlerTaskInclude
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.handler import Handler

@pytest.fixture
def mock_task_data():
    return {
        'name': 'Mock Task',
        'action': 'debug',
        'args': {'msg': 'Hello World'}
    }

def test_handler_task_include_load(mock_task_data, mocker):
    mock_block = mocker.Mock()
    mock_role = mocker.Mock()
    mock_task_include = mocker.Mock()
    mock_variable_manager = mocker.Mock()
    mock_loader = mocker.Mock()

    # Mock the methods from Handler and TaskInclude
    mocker.patch.object(HandlerTaskInclude, 'load_data', return_value=mock_task_data)
    mocker.patch.object(HandlerTaskInclude, 'check_options', return_value='handler_checked')

    handler_task_include = HandlerTaskInclude.load(
        data=mock_task_data,
        block=mock_block,
        role=mock_role,
        task_include=mock_task_include,
        variable_manager=mock_variable_manager,
        loader=mock_loader
    )

    assert handler_task_include == 'handler_checked'
    HandlerTaskInclude.load_data.assert_called_once_with(mock_task_data, variable_manager=mock_variable_manager, loader=mock_loader)
    HandlerTaskInclude.check_options.assert_called_once_with(mock_task_data, mock_task_data)
