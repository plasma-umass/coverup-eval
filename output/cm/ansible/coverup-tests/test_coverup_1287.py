# file lib/ansible/plugins/action/validate_argument_spec.py:20-37
# lines [31, 33, 34, 35, 36, 37]
# branches ['33->34', '33->36', '34->33', '34->35']

import pytest
from ansible.plugins.action.validate_argument_spec import ActionModule
from ansible.template import Templar
from ansible.utils.vars import combine_vars
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager

@pytest.fixture
def action_module(mocker):
    mocker.patch('ansible.plugins.action.ActionBase._execute_module')
    loader = DataLoader()
    inventory = InventoryManager(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    return ActionModule(task={}, connection=None, play_context=None, loader=loader, templar=Templar(loader=loader), shared_loader_obj=None)

def test_get_args_from_task_vars_with_templated_vars(action_module, mocker):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'str'}
    }
    task_vars = {
        'arg1': '{{ templated_var }}',
        'arg2': 'static_value',
        'templated_var': 'dynamic_value'
    }
    mocker.patch.object(action_module._templar, 'template', return_value={'arg1': 'dynamic_value', 'arg2': 'static_value'})
    
    args = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert args == {'arg1': 'dynamic_value', 'arg2': 'static_value'}
    action_module._templar.template.assert_called_once()
