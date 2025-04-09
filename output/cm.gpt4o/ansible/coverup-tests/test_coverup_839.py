# file lib/ansible/inventory/manager.py:187-188
# lines [187, 188]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the InventoryManager class is imported from ansible.inventory.manager
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def mock_inventory():
    mock_inventory = MagicMock()
    mock_inventory.get_groups_dict.return_value = {'group1': ['host1', 'host2'], 'group2': ['host3']}
    return mock_inventory

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def inventory_manager(mock_loader, mock_inventory):
    manager = InventoryManager(mock_loader)
    manager._inventory = mock_inventory
    return manager

def test_get_groups_dict(inventory_manager, mock_inventory):
    result = inventory_manager.get_groups_dict()
    mock_inventory.get_groups_dict.assert_called_once()
    assert result == {'group1': ['host1', 'host2'], 'group2': ['host3']}
