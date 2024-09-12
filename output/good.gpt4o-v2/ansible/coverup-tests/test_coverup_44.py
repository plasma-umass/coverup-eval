# file: lib/ansible/plugins/action/set_stats.py:33-77
# asked: {"lines": [33, 34, 35, 37, 38, 40, 42, 43, 45, 46, 48, 49, 50, 51, 54, 55, 56, 57, 58, 60, 62, 64, 66, 67, 68, 69, 70, 72, 74, 75, 77], "branches": [[34, 35], [34, 37], [42, 43], [42, 74], [45, 46], [45, 48], [48, 49], [48, 54], [54, 55], [54, 62], [56, 54], [56, 57], [57, 58], [57, 60], [62, 64], [62, 74], [66, 67], [66, 72]]}
# gained: {"lines": [33, 34, 35, 37, 38, 40, 42, 43, 45, 46, 48, 49, 50, 51, 54, 55, 56, 57, 58, 62, 64, 66, 67, 68, 69, 70, 72, 74, 75, 77], "branches": [[34, 35], [42, 43], [42, 74], [45, 46], [45, 48], [48, 49], [48, 54], [54, 55], [54, 62], [56, 54], [56, 57], [57, 58], [62, 64], [62, 74], [66, 67], [66, 72]]}

import pytest
from ansible.plugins.action.set_stats import ActionModule
from ansible.module_utils.six import iteritems
from ansible.module_utils.parsing.convert_bool import boolean
from ansible.utils.vars import isidentifier
from ansible.playbook.task import Task
from ansible.template import Templar
from ansible.executor.task_result import TaskResult
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play_context import PlayContext
from unittest.mock import MagicMock

@pytest.fixture
def action_module():
    task = Task()
    task.args = {}
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=())
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    templar = Templar(loader=loader)
    play_context = PlayContext()
    connection = MagicMock()
    connection._shell = MagicMock()
    connection._shell.tmpdir = "/tmp"
    return ActionModule(task=task, connection=connection, play_context=play_context, loader=loader, templar=templar, shared_loader_obj=None)

def test_run_no_task_vars(action_module):
    result = action_module.run()
    assert result['changed'] is False
    assert 'ansible_stats' in result

def test_run_with_data_as_string(action_module):
    action_module._task.args = {'data': 'key: value'}
    result = action_module.run()
    assert result['failed'] is True
    assert result['msg'] == "The 'data' option needs to be a dictionary/hash"

def test_run_with_invalid_data_type(action_module):
    action_module._templar.template = lambda x, **kwargs: x
    action_module._task.args = {'data': 'invalid_data'}
    result = action_module.run()
    assert result['failed'] is True
    assert result['msg'] == "The 'data' option needs to be a dictionary/hash"

def test_run_with_valid_data(action_module):
    action_module._templar.template = lambda x, **kwargs: x
    action_module._task.args = {'data': {'valid_key': 'value'}}
    result = action_module.run()
    assert result['changed'] is False
    assert 'ansible_stats' in result
    assert result['ansible_stats']['data']['valid_key'] == 'value'

def test_run_with_invalid_identifier(action_module):
    action_module._templar.template = lambda x, **kwargs: x
    action_module._task.args = {'data': {'invalid-key': 'value'}}
    result = action_module.run()
    assert result['failed'] is True
    assert result['msg'] == "The variable name 'invalid-key' is not valid. Variables must start with a letter or underscore character, and contain only letters, numbers and underscores."

def test_run_with_boolean_options(action_module):
    action_module._templar.template = lambda x, **kwargs: x
    action_module._task.args = {'data': {'key': 'value'}, 'per_host': 'yes', 'aggregate': 'no'}
    result = action_module.run()
    assert result['changed'] is False
    assert 'ansible_stats' in result
    assert result['ansible_stats']['per_host'] is True
    assert result['ansible_stats']['aggregate'] is False
