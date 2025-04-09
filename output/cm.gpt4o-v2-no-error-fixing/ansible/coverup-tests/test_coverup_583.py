# file: lib/ansible/inventory/manager.py:184-185
# asked: {"lines": [184, 185], "branches": []}
# gained: {"lines": [184, 185], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.group import Group
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_manager():
    loader = None  # Replace with appropriate loader if needed
    return InventoryManager(loader)

def test_add_group(inventory_manager, mocker):
    group = Group(name='test_group')
    mock_add_group = mocker.patch.object(InventoryData, 'add_group', return_value=None)
    
    result = inventory_manager.add_group(group)
    
    mock_add_group.assert_called_once_with(group)
    assert result is None
