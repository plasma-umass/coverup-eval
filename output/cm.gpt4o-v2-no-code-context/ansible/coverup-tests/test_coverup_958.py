# file: lib/ansible/plugins/action/group_by.py:24-51
# asked: {"lines": [24, 25, 28, 29, 31, 32, 33, 35, 36, 38, 39, 40, 41, 43, 44, 45, 46, 48, 49, 50, 51], "branches": [[32, 33], [32, 35], [38, 39], [38, 43], [45, 46], [45, 48]]}
# gained: {"lines": [24, 25, 28, 29, 31, 32, 35, 36, 38, 39, 40, 41, 43, 44, 45, 46, 48, 49, 50, 51], "branches": [[32, 35], [38, 39], [38, 43], [45, 46], [45, 48]]}

import pytest
from ansible.plugins.action.group_by import ActionModule
from ansible.playbook.task import Task
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.utils.display import Display
from ansible import context
from ansible.module_utils.common.collections import ImmutableDict
from unittest.mock import MagicMock

@pytest.fixture
def mock_task():
    return Task()

@pytest.fixture
def mock_task_vars():
    return {
        'group_names': ['all'],
        'inventory_hostname': 'localhost',
    }

@pytest.fixture
def action_module(mock_task):
    play_context = MagicMock()
    play_context.check_mode = False
    connection = MagicMock()
    connection._shell = MagicMock()
    connection._shell.tmpdir = None
    return ActionModule(task=mock_task, connection=connection, play_context=play_context, loader=None, templar=None, shared_loader_obj=None)

def test_run_no_key(action_module, mock_task_vars):
    action_module._task.args = {}
    result = action_module.run(task_vars=mock_task_vars)
    assert result['failed'] is True
    assert result['msg'] == "the 'key' param is required when using group_by"

def test_run_with_key(action_module, mock_task_vars):
    action_module._task.args = {'key': 'test_group'}
    result = action_module.run(task_vars=mock_task_vars)
    assert result['changed'] is False
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['all']

def test_run_with_key_and_parents(action_module, mock_task_vars):
    action_module._task.args = {'key': 'test_group', 'parents': 'parent_group'}
    result = action_module.run(task_vars=mock_task_vars)
    assert result['changed'] is False
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['parent_group']

def test_run_with_key_and_multiple_parents(action_module, mock_task_vars):
    action_module._task.args = {'key': 'test_group', 'parents': ['parent_group1', 'parent_group2']}
    result = action_module.run(task_vars=mock_task_vars)
    assert result['changed'] is False
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['parent_group1', 'parent_group2']
