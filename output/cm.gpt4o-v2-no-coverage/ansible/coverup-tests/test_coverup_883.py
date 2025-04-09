# file: lib/ansible/inventory/manager.py:601-603
# asked: {"lines": [601, 603], "branches": []}
# gained: {"lines": [601, 603], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    sources = None
    return InventoryManager(loader, sources)

def test_list_groups(inventory_manager, mocker):
    mock_groups = {'group1': MagicMock(), 'group2': MagicMock()}
    mocker.patch.object(inventory_manager._inventory, 'groups', mock_groups)
    
    result = inventory_manager.list_groups()
    
    assert result == ['group1', 'group2']
