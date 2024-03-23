# file lib/ansible/inventory/manager.py:169-171
# lines [169, 170, 171]
# branches []

import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import MagicMock

# Assuming that the InventoryManager is part of a larger Ansible codebase
# and that the Inventory class has a 'localhost' attribute or property.
# Since the actual Inventory class is not importable, we will mock it entirely.

@pytest.fixture
def inventory_manager(mocker):
    # Mock the Inventory to provide a 'localhost' property
    inventory_mock = MagicMock()
    inventory_mock.localhost = '127.0.0.1'
    
    # Mock the _inventory attribute of InventoryManager to use the mocked Inventory
    inv_manager = InventoryManager(loader=None, sources='localhost,')
    inv_manager._inventory = inventory_mock
    return inv_manager

def test_localhost_property(inventory_manager):
    # Test that the localhost property returns the correct value
    assert inventory_manager.localhost == '127.0.0.1', "The localhost property did not return the expected value"

    # Cleanup is handled by the fixture's scope and pytest's garbage collection
