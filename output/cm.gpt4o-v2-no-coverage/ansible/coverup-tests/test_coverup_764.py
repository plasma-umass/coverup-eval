# file: lib/ansible/inventory/manager.py:341-346
# asked: {"lines": [341, 344, 345, 346], "branches": []}
# gained: {"lines": [341, 344, 345, 346], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    sources = ['source1', 'source2']
    manager = InventoryManager(loader, sources, parse=False)
    return manager

def test_refresh_inventory(inventory_manager, mocker):
    mocker.patch.object(inventory_manager, 'clear_caches')
    mocker.patch.object(inventory_manager, 'parse_sources')
    mocker.patch('ansible.inventory.data.InventoryData', return_value=MagicMock())

    inventory_manager.refresh_inventory()

    inventory_manager.clear_caches.assert_called_once()
    inventory_manager.parse_sources.assert_called_once_with(cache=False)
    assert isinstance(inventory_manager._inventory, InventoryData)
