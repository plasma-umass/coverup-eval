# file: lib/ansible/inventory/manager.py:184-185
# asked: {"lines": [184, 185], "branches": []}
# gained: {"lines": [184, 185], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData
from unittest.mock import MagicMock

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    return InventoryManager(loader)

def test_add_group(inventory_manager, mocker):
    group = MagicMock()
    mock_add_group = mocker.patch.object(InventoryData, 'add_group', return_value=None)
    
    inventory_manager.add_group(group)
    
    mock_add_group.assert_called_once_with(group)
