# file: lib/ansible/plugins/action/validate_argument_spec.py:20-37
# asked: {"lines": [20, 31, 33, 34, 35, 36, 37], "branches": [[33, 34], [33, 36], [34, 33], [34, 35]]}
# gained: {"lines": [20, 31, 33, 34, 35, 36, 37], "branches": [[33, 34], [33, 36], [34, 33], [34, 35]]}

import pytest
from ansible.plugins.action.validate_argument_spec import ActionModule
from ansible.template import Templar
from ansible.utils.vars import load_extra_vars
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils.six import iteritems

class MockTemplar:
    def __init__(self, *args, **kwargs):
        pass

    def template(self, args):
        return args

@pytest.fixture
def action_module(monkeypatch):
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    monkeypatch.setattr(action_module, '_templar', MockTemplar())
    return action_module

def test_get_args_from_task_vars_with_task_vars(action_module):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'}
    }
    task_vars = {
        'arg1': 'value1',
        'arg2': 2
    }
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    assert result == task_vars

def test_get_args_from_task_vars_without_task_vars(action_module):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'}
    }
    task_vars = {
        'arg3': 'value3'
    }
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    assert result == {}

def test_get_args_from_task_vars_with_partial_task_vars(action_module):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'}
    }
    task_vars = {
        'arg1': 'value1'
    }
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    assert result == {'arg1': 'value1'}
