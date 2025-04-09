# file: lib/ansible/inventory/manager.py:194-195
# asked: {"lines": [194, 195], "branches": []}
# gained: {"lines": [194, 195], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    inventory_manager = InventoryManager(loader)
    inventory_manager._inventory = MagicMock(spec=InventoryData)
    return inventory_manager

def test_get_host(inventory_manager):
    hostname = "test_host"
    expected_host = MagicMock()
    inventory_manager._inventory.get_host.return_value = expected_host

    result = inventory_manager.get_host(hostname)

    inventory_manager._inventory.get_host.assert_called_once_with(hostname)
    assert result == expected_host
