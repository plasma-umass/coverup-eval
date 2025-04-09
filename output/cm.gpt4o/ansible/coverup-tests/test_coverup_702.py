# file lib/ansible/inventory/manager.py:173-175
# lines [173, 174, 175]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the InventoryManager class is imported from ansible.inventory.manager
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def mock_inventory_manager(mocker):
    mock_inventory = mocker.MagicMock()
    mock_inventory.groups = {'group1': 'value1', 'group2': 'value2'}
    manager = InventoryManager(loader=MagicMock())
    manager._inventory = mock_inventory
    return manager

def test_inventory_manager_groups(mock_inventory_manager):
    groups = mock_inventory_manager.groups
    assert groups == {'group1': 'value1', 'group2': 'value2'}
