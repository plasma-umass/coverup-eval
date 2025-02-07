# file: lib/ansible/inventory/manager.py:650-651
# asked: {"lines": [650, 651], "branches": []}
# gained: {"lines": [650, 651], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def inventory_manager():
    loader = DataLoader()
    return InventoryManager(loader)

def test_clear_pattern_cache(inventory_manager):
    # Set up initial state
    inventory_manager._pattern_cache = {'some_key': 'some_value'}
    
    # Call the method
    inventory_manager.clear_pattern_cache()
    
    # Assert the postcondition
    assert inventory_manager._pattern_cache == {}

    # Clean up
    inventory_manager._pattern_cache = None
