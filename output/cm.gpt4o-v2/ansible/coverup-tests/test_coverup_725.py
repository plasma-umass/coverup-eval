# file: lib/ansible/inventory/manager.py:177-179
# asked: {"lines": [177, 178, 179], "branches": []}
# gained: {"lines": [177, 178, 179], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    inventory_data = InventoryData()
    inventory_manager = InventoryManager(loader)
    inventory_manager._inventory = inventory_data
    return inventory_manager

def test_hosts_property(inventory_manager):
    mock_hosts = {'host1': 'details1', 'host2': 'details2'}
    inventory_manager._inventory.hosts = mock_hosts
    assert inventory_manager.hosts == mock_hosts
