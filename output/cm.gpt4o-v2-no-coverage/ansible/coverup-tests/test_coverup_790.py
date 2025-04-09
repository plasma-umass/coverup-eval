# file: lib/ansible/inventory/manager.py:190-192
# asked: {"lines": [190, 191, 192], "branches": []}
# gained: {"lines": [190, 191, 192], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

def test_reconcile_inventory(monkeypatch):
    # Arrange
    loader = MagicMock()
    inventory_manager = InventoryManager(loader)
    mock_inventory = MagicMock()
    monkeypatch.setattr(inventory_manager, '_inventory', mock_inventory)
    
    # Act
    result = inventory_manager.reconcile_inventory()
    
    # Assert
    assert inventory_manager._hosts_patterns_cache == {}
    assert inventory_manager._pattern_cache == {}
    mock_inventory.reconcile_inventory.assert_called_once()
    assert result == mock_inventory.reconcile_inventory.return_value
