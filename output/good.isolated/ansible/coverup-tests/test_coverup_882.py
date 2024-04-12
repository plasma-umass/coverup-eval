# file lib/ansible/inventory/manager.py:650-651
# lines [650, 651]
# branches []

import pytest
from ansible.inventory.manager import InventoryManager

# Test function to execute the clear_pattern_cache method
def test_clear_pattern_cache():
    # Create an instance of InventoryManager
    inventory_manager = InventoryManager(loader=None, sources='localhost,')

    # Set a value in the _pattern_cache to simulate cache usage
    inventory_manager._pattern_cache = {'some_pattern': 'some_value'}

    # Ensure the _pattern_cache is not empty before calling clear_pattern_cache
    assert inventory_manager._pattern_cache

    # Call the method that we want to test
    inventory_manager.clear_pattern_cache()

    # Assert that the _pattern_cache is empty after calling the method
    assert not inventory_manager._pattern_cache
