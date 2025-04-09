# file: lib/ansible/inventory/manager.py:177-179
# asked: {"lines": [177, 178, 179], "branches": []}
# gained: {"lines": [177, 178, 179], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager

def test_inventory_manager_hosts():
    # Arrange
    inventory_mock = MagicMock()
    inventory_mock.hosts = {'host1': 'details1', 'host2': 'details2'}
    
    inventory_manager = InventoryManager(loader=None)
    inventory_manager._inventory = inventory_mock
    
    # Act
    hosts = inventory_manager.hosts
    
    # Assert
    assert hosts == {'host1': 'details1', 'host2': 'details2'}
