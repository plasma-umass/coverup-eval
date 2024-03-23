# file lib/ansible/inventory/manager.py:601-603
# lines [601, 603]
# branches []

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData
from unittest.mock import MagicMock

# Define a fixture for the InventoryManager with a mocked InventoryData
@pytest.fixture
def inventory_manager_with_mocked_data(mocker):
    inventory_data = InventoryData()
    mocker.patch.object(inventory_data, 'groups', {'group1': None, 'group2': None})
    inventory_manager = InventoryManager(loader=None, sources='localhost,')
    inventory_manager._inventory = inventory_data
    return inventory_manager

# Test function to cover list_groups method
def test_list_groups(inventory_manager_with_mocked_data):
    inventory_manager = inventory_manager_with_mocked_data
    groups = inventory_manager.list_groups()
    assert sorted(groups) == ['group1', 'group2'], "The list of groups should be sorted and match the mocked groups"
