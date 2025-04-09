# file: lib/ansible/inventory/manager.py:341-346
# asked: {"lines": [341, 344, 345, 346], "branches": []}
# gained: {"lines": [341, 344, 345, 346], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming InventoryManager and InventoryData are imported from ansible/inventory/manager.py
from ansible.inventory.manager import InventoryManager, InventoryData

@pytest.fixture
def inventory_manager(mocker):
    loader = MagicMock()  # Mock the loader argument
    manager = InventoryManager(loader)
    mocker.patch.object(manager, 'clear_caches')
    mocker.patch.object(manager, 'parse_sources')
    return manager

def test_refresh_inventory(inventory_manager):
    inventory_manager.refresh_inventory()
    
    # Assertions to verify the postconditions
    inventory_manager.clear_caches.assert_called_once()
    assert isinstance(inventory_manager._inventory, InventoryData)
    inventory_manager.parse_sources.assert_called_once_with(cache=False)
