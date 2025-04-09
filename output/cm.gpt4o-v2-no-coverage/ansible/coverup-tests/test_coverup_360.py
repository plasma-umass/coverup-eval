# file: lib/ansible/plugins/action/shell.py:10-27
# asked: {"lines": [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 25, 27], "branches": []}
# gained: {"lines": [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 25, 27], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.shell import ActionModule
from ansible.plugins.action import ActionBase

@pytest.fixture
def mock_task():
    return MagicMock()

@pytest.fixture
def mock_connection():
    return MagicMock()

@pytest.fixture
def mock_play_context():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_templar():
    return MagicMock()

@pytest.fixture
def mock_shared_loader_obj():
    return MagicMock()

@pytest.fixture
def action_module(mock_task, mock_connection, mock_play_context, mock_loader, mock_templar, mock_shared_loader_obj):
    return ActionModule(task=mock_task, connection=mock_connection, play_context=mock_play_context, loader=mock_loader, templar=mock_templar, shared_loader_obj=mock_shared_loader_obj)

def test_run(action_module, mock_task, mock_shared_loader_obj):
    mock_task.args = {}
    mock_command_action = MagicMock()
    mock_command_action.run.return_value = {'changed': True}
    
    with patch.object(mock_shared_loader_obj.action_loader, 'get', return_value=mock_command_action):
        result = action_module.run(task_vars={})
    
    assert result == {'changed': True}
    assert mock_task.args['_uses_shell'] == True
    mock_command_action.run.assert_called_once_with(task_vars={})
