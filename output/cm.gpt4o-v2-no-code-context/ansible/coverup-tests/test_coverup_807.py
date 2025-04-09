# file: lib/ansible/plugins/action/reboot.py:86-87
# asked: {"lines": [86, 87], "branches": []}
# gained: {"lines": [86, 87], "branches": []}

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.plugins.action import ActionBase
from ansible.playbook.play_context import PlayContext
from ansible.executor.task_executor import TaskExecutor

def test_action_module_init(mocker):
    mock_super = mocker.patch('ansible.plugins.action.reboot.ActionBase.__init__', autospec=True)
    
    # Mocking the required arguments for ActionBase
    task = mocker.Mock()
    connection = mocker.Mock()
    play_context = PlayContext()
    loader = mocker.Mock()
    templar = mocker.Mock()
    shared_loader_obj = mocker.Mock()
    
    action_module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    
    mock_super.assert_called_once_with(action_module, task, connection, play_context, loader, templar, shared_loader_obj)
