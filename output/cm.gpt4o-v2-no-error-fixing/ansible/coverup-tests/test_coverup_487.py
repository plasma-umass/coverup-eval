# file: lib/ansible/inventory/manager.py:169-171
# asked: {"lines": [169, 170, 171], "branches": []}
# gained: {"lines": [169, 170, 171], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_manager():
    loader = None  # Replace with appropriate loader if needed
    return InventoryManager(loader)

def test_localhost_property(inventory_manager):
    # Setup
    inventory_manager._inventory.localhost = 'localhost_value'
    
    # Test
    assert inventory_manager.localhost == 'localhost_value'
    
    # Cleanup
    inventory_manager._inventory.localhost = None
