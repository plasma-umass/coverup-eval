# file lib/ansible/plugins/action/validate_argument_spec.py:20-37
# lines []
# branches ['34->33']

import pytest
from ansible.plugins.action.validate_argument_spec import ActionModule
from ansible.template import Templar
from ansible.utils.vars import combine_vars
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager

# Mock classes and functions
class MockLoader(DataLoader):
    pass

class MockInventory(InventoryManager):
    def __init__(self, loader):
        pass

class MockVariableManager(VariableManager):
    def __init__(self, loader, inventory):
        pass

@pytest.fixture
def action_module(mocker):
    loader = MockLoader()
    inventory = MockInventory(loader)
    variable_manager = MockVariableManager(loader, inventory)
    templar = Templar(loader=loader)
    mocker.patch('ansible.plugins.action.ActionBase._templar', templar, create=True)
    return ActionModule(task={}, connection=None, play_context=None, loader=loader, templar=templar, shared_loader_obj=None)

def test_get_args_from_task_vars_with_missing_argument_name(action_module):
    argument_spec = {'arg1': {'type': 'str'}, 'arg2': {'type': 'str'}}
    task_vars = {'arg1': 'value1', 'extra_arg': 'value2'}
    expected_args = {'arg1': 'value1'}
    
    args = action_module.get_args_from_task_vars(argument_spec, task_vars)
    
    assert args == expected_args
