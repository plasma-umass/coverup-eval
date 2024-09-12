# file: lib/ansible/inventory/manager.py:187-188
# asked: {"lines": [187, 188], "branches": []}
# gained: {"lines": [187, 188], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    return InventoryManager(loader)

def test_get_groups_dict(inventory_manager, mocker):
    mock_inventory = mocker.patch.object(inventory_manager, '_inventory')
    mock_inventory.get_groups_dict.return_value = {'group1': {}, 'group2': {}}

    result = inventory_manager.get_groups_dict()

    assert result == {'group1': {}, 'group2': {}}
    mock_inventory.get_groups_dict.assert_called_once()
