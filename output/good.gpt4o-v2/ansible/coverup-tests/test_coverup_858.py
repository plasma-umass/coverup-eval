# file: lib/ansible/inventory/manager.py:646-648
# asked: {"lines": [646, 648], "branches": []}
# gained: {"lines": [646, 648], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_manager():
    loader = None  # Mock or provide a suitable loader if necessary
    return InventoryManager(loader)

def test_remove_restriction(inventory_manager):
    # Set a restriction first
    inventory_manager._restriction = 'some_restriction'
    assert inventory_manager._restriction == 'some_restriction'
    
    # Now remove the restriction
    inventory_manager.remove_restriction()
    
    # Assert that the restriction has been removed
    assert inventory_manager._restriction is None
