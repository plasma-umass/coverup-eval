# file: lib/ansible/plugins/action/validate_argument_spec.py:20-37
# asked: {"lines": [20, 31, 33, 34, 35, 36, 37], "branches": [[33, 34], [33, 36], [34, 33], [34, 35]]}
# gained: {"lines": [20, 31, 33, 34, 35, 36, 37], "branches": [[33, 34], [33, 36], [34, 33], [34, 35]]}

import pytest
from ansible.plugins.action.validate_argument_spec import ActionModule
from ansible.template import Templar
from ansible.utils.vars import load_extra_vars

@pytest.fixture
def action_module():
    templar = Templar(loader=None)
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=templar, shared_loader_obj=None)

def test_get_args_from_task_vars_with_task_vars(action_module, monkeypatch):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'}
    }
    task_vars = {
        'arg1': 'value1',
        'arg2': 42
    }

    monkeypatch.setattr(action_module._templar, 'template', lambda x: x)
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert result == task_vars

def test_get_args_from_task_vars_without_task_vars(action_module, monkeypatch):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'}
    }
    task_vars = {}

    monkeypatch.setattr(action_module._templar, 'template', lambda x: x)
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert result == {}

def test_get_args_from_task_vars_partial_task_vars(action_module, monkeypatch):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'}
    }
    task_vars = {
        'arg1': 'value1'
    }

    monkeypatch.setattr(action_module._templar, 'template', lambda x: x)
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert result == {'arg1': 'value1'}
