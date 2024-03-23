# file lib/ansible/cli/inventory.py:233-235
# lines [233, 234, 235]
# branches []

import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

# Mocking the InventoryManager to simulate the behavior of groups
@pytest.fixture
def inventory_manager(mocker):
    inventory_manager = mocker.MagicMock(spec=InventoryManager)
    inventory_manager.groups = {
        'test_group': mocker.MagicMock(),
        'empty_group': None
    }
    return inventory_manager

# Mocking the DataLoader
@pytest.fixture
def data_loader(mocker):
    return mocker.MagicMock(spec=DataLoader)

# Test function to cover _get_group method
def test_get_group_existing_group(inventory_manager, data_loader):
    cli = InventoryCLI(args=['ansible-inventory'])
    cli.inventory = inventory_manager
    cli.loader = data_loader

    group = cli._get_group('test_group')
    assert group is not None
    assert inventory_manager.groups['test_group'] == group

def test_get_group_non_existing_group(inventory_manager, data_loader):
    cli = InventoryCLI(args=['ansible-inventory'])
    cli.inventory = inventory_manager
    cli.loader = data_loader

    group = cli._get_group('non_existing_group')
    assert group is None

def test_get_group_empty_group(inventory_manager, data_loader):
    cli = InventoryCLI(args=['ansible-inventory'])
    cli.inventory = inventory_manager
    cli.loader = data_loader

    group = cli._get_group('empty_group')
    assert group is None
