# file lib/ansible/inventory/manager.py:601-603
# lines [603]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the InventoryManager class is imported from ansible.inventory.manager
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    sources = MagicMock()
    manager = InventoryManager(loader, sources)
    manager._inventory = MagicMock()
    return manager

def test_list_groups(inventory_manager):
    # Mock the groups attribute to ensure line 603 is executed
    inventory_manager._inventory.groups = {
        'group1': MagicMock(),
        'group2': MagicMock(),
        'group3': MagicMock()
    }
    
    result = inventory_manager.list_groups()
    
    # Verify the result is sorted
    assert result == ['group1', 'group2', 'group3']

    # Clean up
    inventory_manager._inventory.groups = {}
