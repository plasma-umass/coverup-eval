# file: lib/ansible/plugins/action/shell.py:10-27
# asked: {"lines": [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 25, 27], "branches": []}
# gained: {"lines": [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 25, 27], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.shell import ActionModule
from ansible.plugins.loader import action_loader

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {}
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    shared_loader_obj.action_loader = action_loader
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_run_method(action_module):
    task_vars = {'var1': 'value1'}
    
    with patch.object(action_loader, 'get', return_value=MagicMock()) as mock_get:
        result = action_module.run(tmp='tmp_path', task_vars=task_vars)
    
        # Ensure '_uses_shell' is set to True
        assert action_module._task.args['_uses_shell'] == True
    
        # Ensure the command action is retrieved and run
        mock_get.assert_called_once_with('ansible.legacy.command',
                                         task=action_module._task,
                                         connection=action_module._connection,
                                         play_context=action_module._play_context,
                                         loader=action_module._loader,
                                         templar=action_module._templar,
                                         shared_loader_obj=action_module._shared_loader_obj)
        mock_get.return_value.run.assert_called_once_with(task_vars=task_vars)
    
        # Ensure the result is returned
        assert result == mock_get.return_value.run.return_value
