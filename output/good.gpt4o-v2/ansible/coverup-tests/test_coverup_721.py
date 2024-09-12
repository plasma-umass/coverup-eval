# file: lib/ansible/inventory/manager.py:341-346
# asked: {"lines": [341, 344, 345, 346], "branches": []}
# gained: {"lines": [341, 344, 345, 346], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_manager(mocker):
    loader = MagicMock()
    manager = InventoryManager(loader=loader, sources=[])
    manager._sources = ["dummy_source"]
    return manager

def test_refresh_inventory(inventory_manager, mocker):
    # Mock the methods called within refresh_inventory
    mocker.patch.object(inventory_manager, 'clear_caches')
    mocker.patch.object(inventory_manager, 'parse_sources')
    inventory_data_mock = mocker.patch('ansible.inventory.manager.InventoryData', return_value=MagicMock())

    # Call the method
    inventory_manager.refresh_inventory()

    # Assertions to ensure the methods were called
    inventory_manager.clear_caches.assert_called_once()
    inventory_manager.parse_sources.assert_called_once_with(cache=False)
    inventory_data_mock.assert_called_once()
    assert inventory_manager._inventory == inventory_data_mock.return_value
