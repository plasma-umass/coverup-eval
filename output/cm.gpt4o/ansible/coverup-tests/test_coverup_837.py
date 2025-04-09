# file lib/ansible/inventory/manager.py:646-648
# lines [646, 648]
# branches []

import pytest
from unittest.mock import Mock
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader_mock = Mock()
    manager = InventoryManager(loader=loader_mock)
    manager._restriction = 'some_restriction'
    yield manager
    # Clean up if necessary
    manager._restriction = None

def test_remove_restriction(inventory_manager):
    # Ensure the restriction is initially set
    assert inventory_manager._restriction == 'some_restriction'
    
    # Call the method to remove the restriction
    inventory_manager.remove_restriction()
    
    # Verify the restriction has been removed
    assert inventory_manager._restriction is None
