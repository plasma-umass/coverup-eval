# file lib/ansible/inventory/manager.py:341-346
# lines [341, 344, 345, 346]
# branches []

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData
from unittest.mock import MagicMock

# Assuming that the InventoryManager class is part of a larger module that we're testing

class TestInventoryManager:
    @pytest.fixture
    def inventory_manager(self, mocker):
        # Mock the loader required by InventoryManager
        mock_loader = MagicMock()
        # Create an instance of InventoryManager with the mocked loader
        manager = InventoryManager(loader=mock_loader)
        # Mock clear_caches and parse_sources methods
        manager.clear_caches = MagicMock()
        manager.parse_sources = MagicMock()
        return manager

    def test_refresh_inventory(self, inventory_manager):
        # Call the method we want to test
        inventory_manager.refresh_inventory()

        # Assert that clear_caches and parse_sources were called
        inventory_manager.clear_caches.assert_called_once()
        inventory_manager.parse_sources.assert_called_once_with(cache=False)

        # Assert that _inventory is an instance of InventoryData
        assert isinstance(inventory_manager._inventory, InventoryData)
