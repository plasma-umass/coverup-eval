# file lib/ansible/plugins/action/validate_argument_spec.py:20-37
# lines []
# branches ['34->33']

import pytest
from ansible.plugins.action.validate_argument_spec import ActionModule
from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader
from ansible.executor.task_queue_manager import TaskQueueManager

@pytest.fixture
def action_module():
    loader = DataLoader()
    templar = Templar(loader=loader)
    shared_loader_obj = TaskQueueManager(loader=loader, inventory=None, variable_manager=None, passwords=None)
    return ActionModule(task=None, connection=None, play_context=None, loader=loader, templar=templar, shared_loader_obj=shared_loader_obj)

def test_get_args_from_task_vars_with_task_vars(action_module):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'},
    }
    task_vars = {
        'arg1': 'value1',
        'arg2': 42,
    }

    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert result == {
        'arg1': 'value1',
        'arg2': 42,
    }

def test_get_args_from_task_vars_without_task_vars(action_module):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'},
    }
    task_vars = {
        'arg3': 'value3',
    }

    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert result == {}
