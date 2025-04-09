# file lib/ansible/inventory/manager.py:194-195
# lines [194, 195]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the InventoryManager class is imported from ansible.inventory.manager
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def inventory_manager(mock_inventory, mock_loader):
    manager = InventoryManager(loader=mock_loader, sources=None)
    manager._inventory = mock_inventory
    return manager

def test_get_host(inventory_manager, mock_inventory):
    hostname = 'test_host'
    expected_host = 'mocked_host'
    
    mock_inventory.get_host.return_value = expected_host
    
    result = inventory_manager.get_host(hostname)
    
    mock_inventory.get_host.assert_called_once_with(hostname)
    assert result == expected_host
