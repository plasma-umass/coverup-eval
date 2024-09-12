# file: lib/ansible/plugins/action/validate_argument_spec.py:20-37
# asked: {"lines": [], "branches": [[34, 33]]}
# gained: {"lines": [], "branches": [[34, 33]]}

import pytest
from ansible.plugins.action.validate_argument_spec import ActionModule
from ansible.module_utils.six import iteritems

@pytest.fixture
def action_module():
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

def test_get_args_from_task_vars_with_argument_in_task_vars(action_module, mocker):
    argument_spec = {'arg1': {'type': 'str'}}
    task_vars = {'arg1': 'value1'}
    
    mock_templar = mocker.Mock()
    mock_templar.template = mocker.Mock(return_value=task_vars)
    action_module._templar = mock_templar
    
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert result == task_vars
    mock_templar.template.assert_called_once_with(task_vars)

def test_get_args_from_task_vars_without_argument_in_task_vars(action_module, mocker):
    argument_spec = {'arg1': {'type': 'str'}}
    task_vars = {'arg2': 'value2'}
    
    mock_templar = mocker.Mock()
    mock_templar.template = mocker.Mock(return_value={})
    action_module._templar = mock_templar
    
    result = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert result == {}
    mock_templar.template.assert_called_once_with({})
