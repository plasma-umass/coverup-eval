# file lib/ansible/plugins/action/fail.py:24-43
# lines [24, 25, 27, 28, 30, 31, 32, 34, 35, 37, 38, 39, 41, 42, 43]
# branches ['31->32', '31->34', '38->39', '38->41']

import pytest
from ansible.plugins.action.fail import ActionModule
from ansible.playbook.task import Task
from ansible.playbook.play_context import PlayContext
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from unittest.mock import MagicMock

@pytest.fixture
def mock_task():
    return Task.load(dict(action='fail', args=dict(msg='Custom failure message')))

@pytest.fixture
def mock_task_no_msg():
    return Task.load(dict(action='fail'))

@pytest.fixture
def mock_task_vars():
    return dict()

@pytest.fixture
def mock_play_context():
    play_context = PlayContext()
    play_context.check_mode = False
    return play_context

@pytest.fixture
def mock_connection():
    connection = MagicMock()
    connection._shell = MagicMock()
    connection._shell.tmpdir = "/tmp"
    return connection

@pytest.fixture
def action_module(mock_task, mock_play_context, mock_connection):
    return ActionModule(task=mock_task, connection=mock_connection, play_context=mock_play_context, loader=None, templar=None, shared_loader_obj=None)

@pytest.fixture
def action_module_no_msg(mock_task_no_msg, mock_play_context, mock_connection):
    return ActionModule(task=mock_task_no_msg, connection=mock_connection, play_context=mock_play_context, loader=None, templar=None, shared_loader_obj=None)

def test_action_module_with_custom_message(action_module, mock_task_vars):
    result = action_module.run(task_vars=mock_task_vars)
    assert result['failed'] is True
    assert result['msg'] == 'Custom failure message'

def test_action_module_with_default_message(action_module_no_msg, mock_task_vars):
    result = action_module_no_msg.run(task_vars=mock_task_vars)
    assert result['failed'] is True
    assert result['msg'] == 'Failed as requested from task'
