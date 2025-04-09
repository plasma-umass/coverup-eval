# file lib/ansible/inventory/manager.py:190-192
# lines [191, 192]
# branches []

import pytest
from unittest.mock import MagicMock, patch

# Assuming the InventoryManager class is imported from ansible.inventory.manager
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader = MagicMock()  # Mock the loader argument
    manager = InventoryManager(loader)
    manager.clear_caches = MagicMock()
    manager._inventory = MagicMock()
    return manager

def test_reconcile_inventory(inventory_manager):
    # Mock the return value of _inventory.reconcile_inventory
    inventory_manager._inventory.reconcile_inventory.return_value = "reconciled"

    result = inventory_manager.reconcile_inventory()

    # Assert that clear_caches was called
    inventory_manager.clear_caches.assert_called_once()

    # Assert that _inventory.reconcile_inventory was called
    inventory_manager._inventory.reconcile_inventory.assert_called_once()

    # Assert the result is as expected
    assert result == "reconciled"
