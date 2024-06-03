# file lib/ansible/plugins/action/group_by.py:24-51
# lines [24, 25, 28, 29, 31, 32, 33, 35, 36, 38, 39, 40, 41, 43, 44, 45, 46, 48, 49, 50, 51]
# branches ['32->33', '32->35', '38->39', '38->43', '45->46', '45->48']

import pytest
from ansible.plugins.action.group_by import ActionModule
from ansible.playbook.task import Task
from ansible.utils.vars import load_extra_vars
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.playbook.play_context import PlayContext
from unittest.mock import MagicMock

@pytest.fixture
def mock_task():
    return Task.load(dict(action='group_by', args=dict(key='test_group', parents='parent_group')))

@pytest.fixture
def mock_task_no_key():
    return Task.load(dict(action='group_by', args=dict(parents='parent_group')))

@pytest.fixture
def mock_task_vars():
    return dict()

@pytest.fixture
def action_module(mock_task):
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=())
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    connection = MagicMock()
    connection._shell = MagicMock()
    connection._shell.tmpdir = None
    return ActionModule(task=mock_task, connection=connection, play_context=play_context, loader=loader, templar=None, shared_loader_obj=None)

def test_group_by_action_module(action_module, mock_task_vars):
    result = action_module.run(task_vars=mock_task_vars)
    assert result['changed'] is False
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['parent_group']

def test_group_by_action_module_no_key(action_module, mock_task_no_key, mock_task_vars):
    action_module._task = mock_task_no_key
    result = action_module.run(task_vars=mock_task_vars)
    assert result['failed'] is True
    assert result['msg'] == "the 'key' param is required when using group_by"
