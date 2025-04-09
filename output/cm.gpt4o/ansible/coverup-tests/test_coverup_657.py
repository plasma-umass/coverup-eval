# file lib/ansible/inventory/manager.py:341-346
# lines [341, 344, 345, 346]
# branches []

import pytest
from unittest.mock import patch, MagicMock

# Assuming InventoryManager and its dependencies are imported from ansible.inventory.manager
from ansible.inventory.manager import InventoryManager, InventoryData

@pytest.fixture
def inventory_manager():
    loader = MagicMock()  # Mock the loader dependency
    manager = InventoryManager(loader)
    manager.clear_caches = MagicMock()
    manager.parse_sources = MagicMock()
    return manager

def test_refresh_inventory(inventory_manager):
    with patch('ansible.inventory.manager.InventoryData', return_value=MagicMock()) as mock_inventory_data:
        inventory_manager.refresh_inventory()
        
        # Assertions to verify the correct methods were called
        inventory_manager.clear_caches.assert_called_once()
        inventory_manager.parse_sources.assert_called_once_with(cache=False)
        mock_inventory_data.assert_called_once()
        
        # Verify that _inventory is set correctly
        assert inventory_manager._inventory == mock_inventory_data.return_value
