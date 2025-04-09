# file: lib/ansible/inventory/manager.py:173-175
# asked: {"lines": [173, 174, 175], "branches": []}
# gained: {"lines": [173, 174, 175], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    return InventoryManager(loader)

def test_groups_property(inventory_manager):
    mock_groups = MagicMock()
    inventory_manager._inventory = MagicMock(groups=mock_groups)
    
    assert inventory_manager.groups == mock_groups
