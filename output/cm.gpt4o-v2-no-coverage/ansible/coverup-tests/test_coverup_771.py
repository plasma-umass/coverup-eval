# file: lib/ansible/inventory/manager.py:335-338
# asked: {"lines": [335, 337, 338], "branches": []}
# gained: {"lines": [335, 337, 338], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    return InventoryManager(loader=None)

def test_clear_caches(inventory_manager):
    # Set some initial values in the caches
    inventory_manager._hosts_patterns_cache = {'some_key': 'some_value'}
    inventory_manager._pattern_cache = {'another_key': 'another_value'}
    
    # Ensure the caches are not empty before calling clear_caches
    assert inventory_manager._hosts_patterns_cache
    assert inventory_manager._pattern_cache
    
    # Call the method to clear caches
    inventory_manager.clear_caches()
    
    # Verify that the caches are cleared
    assert inventory_manager._hosts_patterns_cache == {}
    assert inventory_manager._pattern_cache == {}
