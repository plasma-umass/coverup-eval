# file: lib/ansible/inventory/manager.py:601-603
# asked: {"lines": [601, 603], "branches": []}
# gained: {"lines": [601, 603], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_manager():
    loader = None  # Replace with appropriate loader if needed
    return InventoryManager(loader)

def test_list_groups(inventory_manager, mocker):
    mock_groups = {'group1': {}, 'group2': {}, 'group3': {}}
    mocker.patch.object(inventory_manager._inventory, 'groups', mock_groups)
    
    result = inventory_manager.list_groups()
    
    assert result == sorted(mock_groups.keys())
