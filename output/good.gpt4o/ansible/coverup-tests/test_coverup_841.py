# file lib/ansible/inventory/manager.py:650-651
# lines [650, 651]
# branches []

import pytest
from unittest.mock import Mock
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader = Mock()  # Mock the loader dependency
    sources = []  # Provide an empty list for sources
    manager = InventoryManager(loader, sources)
    yield manager
    # Clean up if necessary (though in this case, there's nothing to clean up)

def test_clear_pattern_cache(inventory_manager):
    # Set up initial state
    inventory_manager._pattern_cache = {'some_key': 'some_value'}
    
    # Ensure the cache is not empty before calling the method
    assert inventory_manager._pattern_cache != {}
    
    # Call the method to test
    inventory_manager.clear_pattern_cache()
    
    # Assert the cache is cleared
    assert inventory_manager._pattern_cache == {}
