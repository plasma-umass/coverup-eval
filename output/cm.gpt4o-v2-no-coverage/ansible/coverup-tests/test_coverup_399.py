# file: lib/ansible/inventory/data.py:180-189
# asked: {"lines": [180, 182, 183, 184, 185, 187, 188, 189], "branches": [[182, 183], [182, 187], [187, 0], [187, 188]]}
# gained: {"lines": [180, 182, 183, 184, 185, 187, 188, 189], "branches": [[182, 183], [182, 187], [187, 0], [187, 188]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_remove_group_existing_group(inventory_data):
    group = 'test_group'
    inventory_data.groups[group] = MagicMock()
    inventory_data.hosts = {
        'host1': MagicMock(),
        'host2': MagicMock()
    }

    with patch('ansible.inventory.data.display.debug') as mock_debug:
        inventory_data.remove_group(group)
        mock_debug.assert_called_once_with("Removed group %s from inventory" % group)

    assert group not in inventory_data.groups
    assert inventory_data._groups_dict_cache == {}
    for host in inventory_data.hosts.values():
        host.remove_group.assert_called_once_with(group)

def test_remove_group_non_existing_group(inventory_data):
    group = 'non_existing_group'
    inventory_data.hosts = {
        'host1': MagicMock(),
        'host2': MagicMock()
    }

    inventory_data.remove_group(group)

    for host in inventory_data.hosts.values():
        host.remove_group.assert_called_once_with(group)
