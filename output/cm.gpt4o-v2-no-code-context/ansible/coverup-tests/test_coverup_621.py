# file: lib/ansible/cli/inventory.py:233-235
# asked: {"lines": [233, 234, 235], "branches": []}
# gained: {"lines": [233, 234, 235], "branches": []}

import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

@pytest.fixture
def inventory_cli():
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    cli = InventoryCLI(['inventory'])
    cli.inventory = inventory
    return cli

def test_get_group_existing(inventory_cli):
    group_name = 'testgroup'
    inventory_cli.inventory.add_group(group_name)
    group = inventory_cli._get_group(group_name)
    assert group is not None
    assert group.name == group_name

def test_get_group_non_existing(inventory_cli):
    group_name = 'nonexistentgroup'
    group = inventory_cli._get_group(group_name)
    assert group is None
