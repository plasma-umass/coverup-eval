# file lib/ansible/plugins/action/fail.py:24-43
# lines [32]
# branches ['31->32']

import pytest
from ansible.plugins.action.fail import ActionModule
from ansible.playbook.task import Task
from ansible.playbook.play_context import PlayContext
from ansible.executor.task_queue_manager import TaskQueueManager
from unittest.mock import MagicMock

@pytest.fixture
def mock_task():
    return Task.load(dict(action='fail', args=dict(msg='Test failure message')))

@pytest.fixture
def mock_task_vars():
    return None

@pytest.fixture
def action_module(mock_task):
    play_context = PlayContext()
    connection = MagicMock()
    connection._shell = MagicMock()
    connection._shell.tmpdir = None
    return ActionModule(task=mock_task, connection=connection, play_context=play_context, loader=None, templar=None, shared_loader_obj=None)

def test_action_module_run_with_none_task_vars(action_module, mock_task_vars):
    result = action_module.run(task_vars=mock_task_vars)
    assert result['failed'] is True
    assert result['msg'] == 'Test failure message'
