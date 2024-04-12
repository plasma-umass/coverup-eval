# file lib/ansible/inventory/manager.py:646-648
# lines [646, 648]
# branches []

import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import MagicMock

@pytest.fixture
def inventory_manager():
    # Setup code, create an instance of InventoryManager with a mock loader
    mock_loader = MagicMock()
    manager = InventoryManager(loader=mock_loader)
    yield manager
    # Teardown code, clean up after test
    # No specific cleanup required for this test as per the given code snippet

def test_remove_restriction(inventory_manager):
    # Initially set some restriction
    inventory_manager._restriction = 'some_restriction'
    
    # Call the method under test
    inventory_manager.remove_restriction()
    
    # Assert the postcondition that the restriction is removed (i.e., is None)
    assert inventory_manager._restriction is None
