# file lib/ansible/inventory/manager.py:190-192
# lines [190, 191, 192]
# branches []

import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import MagicMock, create_autospec

# Assuming that the InventoryManager class is part of a larger module that we're testing

class MockInventory:
    def reconcile_inventory(self):
        # Mock behavior of the reconcile_inventory method
        return True

@pytest.fixture
def inventory_manager(mocker):
    # Mock the loader required by InventoryManager
    mock_loader = mocker.MagicMock()
    manager = InventoryManager(loader=mock_loader)
    manager._inventory = MockInventory()
    manager.clear_caches = MagicMock()
    return manager

def test_reconcile_inventory(inventory_manager):
    result = inventory_manager.reconcile_inventory()
    # Verify that clear_caches was called
    inventory_manager.clear_caches.assert_called_once()
    # Verify that the result of reconcile_inventory is as expected
    assert result == True
