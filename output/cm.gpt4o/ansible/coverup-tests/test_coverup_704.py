# file lib/ansible/inventory/manager.py:335-338
# lines [335, 337, 338]
# branches []

import pytest
from unittest import mock
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader_mock = mock.Mock()
    return InventoryManager(loader=loader_mock)

def test_clear_caches(inventory_manager):
    # Set up initial state
    inventory_manager._hosts_patterns_cache = {'some_key': 'some_value'}
    inventory_manager._pattern_cache = {'another_key': 'another_value'}
    
    # Call the method to test
    inventory_manager.clear_caches()
    
    # Assertions to verify postconditions
    assert inventory_manager._hosts_patterns_cache == {}
    assert inventory_manager._pattern_cache == {}
