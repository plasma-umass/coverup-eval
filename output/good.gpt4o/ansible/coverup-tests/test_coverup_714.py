# file lib/ansible/inventory/manager.py:177-179
# lines [177, 178, 179]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the InventoryManager class is defined in ansible.inventory.manager
from ansible.inventory.manager import InventoryManager

def test_inventory_manager_hosts_property():
    # Mock the _inventory attribute
    mock_inventory = MagicMock()
    mock_inventory.hosts = {'host1': 'details1', 'host2': 'details2'}
    
    # Create an instance of InventoryManager and set the _inventory attribute
    manager = InventoryManager(loader=MagicMock(), sources=[])
    manager._inventory = mock_inventory
    
    # Access the hosts property and assert the expected value
    hosts = manager.hosts
    assert hosts == {'host1': 'details1', 'host2': 'details2'}
    
    # Clean up by deleting the _inventory attribute
    del manager._inventory
