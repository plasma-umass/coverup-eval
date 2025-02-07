# file: lib/ansible/inventory/manager.py:173-175
# asked: {"lines": [173, 174, 175], "branches": []}
# gained: {"lines": [173, 174, 175], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    inventory_manager = InventoryManager(loader)
    inventory_manager._inventory = MagicMock(spec=InventoryData)
    return inventory_manager

def test_groups_property(inventory_manager):
    # Setup the mock to return a specific value
    expected_groups = {'group1': 'data1', 'group2': 'data2'}
    inventory_manager._inventory.groups = expected_groups

    # Access the groups property
    groups = inventory_manager.groups

    # Assert that the groups property returns the expected value
    assert groups == expected_groups
