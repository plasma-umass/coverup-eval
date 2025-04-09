# file: lib/ansible/plugins/action/validate_argument_spec.py:20-37
# asked: {"lines": [], "branches": [[34, 33]]}
# gained: {"lines": [], "branches": [[34, 33]]}

import pytest
from ansible.plugins.action.validate_argument_spec import ActionModule
from ansible.module_utils.six import iteritems
from unittest.mock import MagicMock

@pytest.fixture
def action_module():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_get_args_from_task_vars_with_argument_in_task_vars(action_module):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'}
    }
    task_vars = {
        'arg1': 'value1',
        'arg2': 2
    }
    action_module._templar.template = MagicMock(return_value=task_vars)
    
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert result == task_vars
    action_module._templar.template.assert_called_once_with(task_vars)

def test_get_args_from_task_vars_without_argument_in_task_vars(action_module):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'}
    }
    task_vars = {
        'arg3': 'value3'
    }
    expected_result = {}
    action_module._templar.template = MagicMock(return_value=expected_result)
    
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert result == expected_result
    action_module._templar.template.assert_called_once_with(expected_result)
