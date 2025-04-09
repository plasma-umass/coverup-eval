# file: lib/ansible/plugins/inventory/ini.py:249-254
# asked: {"lines": [249, 250, 251, 252, 253, 254], "branches": [[250, 251], [250, 254], [252, 250], [252, 253]]}
# gained: {"lines": [249, 250, 251, 252, 253, 254], "branches": [[250, 251], [250, 254], [252, 253]]}

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

@pytest.fixture
def inventory_module():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    return InventoryModule()

def test_add_pending_children(inventory_module, mocker):
    mocker.patch.object(inventory_module, 'inventory', create=True)
    mocker.patch.object(inventory_module.inventory, 'add_child', create=True)

    pending = {
        'group1': {'parents': ['parent1'], 'state': 'children'},
        'parent1': {'parents': [], 'state': 'children'}
    }

    inventory_module._add_pending_children('group1', pending)

    inventory_module.inventory.add_child.assert_called_with('parent1', 'group1')
    assert 'group1' not in pending

    # Ensure recursive call
    inventory_module.inventory.add_child.reset_mock()
    pending = {
        'group1': {'parents': ['parent1'], 'state': 'children'},
        'parent1': {'parents': ['grandparent1'], 'state': 'children'},
        'grandparent1': {'parents': [], 'state': 'children'}
    }

    inventory_module._add_pending_children('group1', pending)

    inventory_module.inventory.add_child.assert_any_call('parent1', 'group1')
    inventory_module.inventory.add_child.assert_any_call('grandparent1', 'parent1')
    assert 'group1' not in pending
    assert 'parent1' not in pending
