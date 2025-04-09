# file: lib/ansible/inventory/manager.py:190-192
# asked: {"lines": [190, 191, 192], "branches": []}
# gained: {"lines": [190, 191, 192], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager(mocker):
    mock_loader = mocker.Mock()
    mock_inventory_data = mocker.patch('ansible.inventory.manager.InventoryData')
    manager = InventoryManager(mock_loader)
    manager._inventory = mock_inventory_data.return_value
    return manager

def test_reconcile_inventory(inventory_manager):
    # Arrange
    inventory_manager._inventory.reconcile_inventory.return_value = 'reconciled'

    # Act
    result = inventory_manager.reconcile_inventory()

    # Assert
    inventory_manager._inventory.reconcile_inventory.assert_called_once()
    assert result == 'reconciled'
    assert inventory_manager._hosts_patterns_cache == {}
    assert inventory_manager._pattern_cache == {}
