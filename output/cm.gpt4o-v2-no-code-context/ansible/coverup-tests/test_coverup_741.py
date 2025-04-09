# file: lib/ansible/inventory/manager.py:646-648
# asked: {"lines": [646, 648], "branches": []}
# gained: {"lines": [646, 648], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import Mock

@pytest.fixture
def inventory_manager():
    loader_mock = Mock()
    sources = []
    return InventoryManager(loader=loader_mock, sources=sources)

def test_remove_restriction(inventory_manager):
    # Set a restriction to ensure it gets removed
    inventory_manager._restriction = 'some_restriction'
    
    # Call the method to remove the restriction
    inventory_manager.remove_restriction()
    
    # Assert that the restriction has been removed
    assert inventory_manager._restriction is None
