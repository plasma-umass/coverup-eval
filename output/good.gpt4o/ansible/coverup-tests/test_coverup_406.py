# file lib/ansible/plugins/action/validate_argument_spec.py:20-37
# lines [20, 31, 33, 34, 35, 36, 37]
# branches ['33->34', '33->36', '34->33', '34->35']

import pytest
from ansible.plugins.action.validate_argument_spec import ActionModule
from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.utils.vars import load_extra_vars
from ansible.utils.vars import load_options_vars

@pytest.fixture
def action_module():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    templar = Templar(loader=loader, variables=variable_manager.get_vars())
    return ActionModule(task=None, connection=None, play_context=None, loader=loader, templar=templar, shared_loader_obj=None)

def test_get_args_from_task_vars(action_module, mocker):
    argument_spec = {
        'arg1': {'type': 'str'},
        'arg2': {'type': 'int'},
        'arg3': {'type': 'list'}
    }
    task_vars = {
        'arg1': 'value1',
        'arg2': 42,
        'arg3': [1, 2, 3],
        'arg4': 'should not be included'
    }

    # Mock the templar.template method to return the input args directly
    mocker.patch.object(action_module._templar, 'template', side_effect=lambda x: x)

    result = action_module.get_args_from_task_vars(argument_spec, task_vars)

    assert result == {
        'arg1': 'value1',
        'arg2': 42,
        'arg3': [1, 2, 3]
    }
