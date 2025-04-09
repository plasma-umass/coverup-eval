# file lib/ansible/inventory/manager.py:335-338
# lines [335, 337, 338]
# branches []

# test_inventory_manager.py

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def inventory_manager():
    # Mock DataLoader as it is required by InventoryManager
    loader = DataLoader()
    return InventoryManager(loader=loader)

def test_clear_caches(inventory_manager):
    # Setup: populate the caches with some dummy data
    inventory_manager._hosts_patterns_cache = {'dummy_key': 'dummy_value'}
    inventory_manager._pattern_cache = {'dummy_key': 'dummy_value'}

    # Pre-assertions to ensure caches are populated
    assert inventory_manager._hosts_patterns_cache == {'dummy_key': 'dummy_value'}
    assert inventory_manager._pattern_cache == {'dummy_key': 'dummy_value'}

    # Call the method under test
    inventory_manager.clear_caches()

    # Assertions to ensure caches are cleared
    assert inventory_manager._hosts_patterns_cache == {}
    assert inventory_manager._pattern_cache == {}
