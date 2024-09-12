# file: lib/ansible/plugins/action/group_by.py:24-51
# asked: {"lines": [24, 25, 28, 29, 31, 32, 33, 35, 36, 38, 39, 40, 41, 43, 44, 45, 46, 48, 49, 50, 51], "branches": [[32, 33], [32, 35], [38, 39], [38, 43], [45, 46], [45, 48]]}
# gained: {"lines": [24, 25, 28, 29, 31, 32, 33, 35, 36, 38, 39, 40, 41, 43, 44, 45, 46, 48, 49, 50, 51], "branches": [[32, 33], [38, 39], [38, 43], [45, 46], [45, 48]]}

import pytest
from ansible.plugins.action.group_by import ActionModule
from ansible.playbook.task import Task
from ansible.utils.vars import load_extra_vars
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.task_result import TaskResult
from ansible.executor.stats import AggregateStats
from ansible import context
from ansible.cli import CLI
from ansible.module_utils.six import string_types
from unittest.mock import MagicMock

@pytest.fixture
def action_module():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=())
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    task = Task()
    task.args = {}
    play_context = MagicMock()
    play_context.check_mode = False
    connection = MagicMock()
    connection._shell.tmpdir = None
    return ActionModule(task, connection, play_context, loader, variable_manager, variable_manager)

def test_run_no_key(action_module):
    result = action_module.run()
    assert result['failed'] is True
    assert result['msg'] == "the 'key' param is required when using group_by"

def test_run_with_key(action_module):
    action_module._task.args = {'key': 'test_group'}
    result = action_module.run()
    assert result['changed'] is False
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['all']

def test_run_with_key_and_parents(action_module):
    action_module._task.args = {'key': 'test_group', 'parents': 'parent_group'}
    result = action_module.run()
    assert result['changed'] is False
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['parent_group']

def test_run_with_key_and_multiple_parents(action_module):
    action_module._task.args = {'key': 'test_group', 'parents': ['parent_group1', 'parent_group2']}
    result = action_module.run()
    assert result['changed'] is False
    assert result['add_group'] == 'test_group'
    assert result['parent_groups'] == ['parent_group1', 'parent_group2']
