# file: lib/ansible/inventory/data.py:275-283
# asked: {"lines": [279, 280, 281, 283], "branches": [[279, 280], [279, 283], [280, 281], [280, 283]]}
# gained: {"lines": [279, 280, 281, 283], "branches": [[279, 280], [279, 283], [280, 281], [280, 283]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.six import iteritems
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_data():
    inventory = InventoryData()
    inventory.groups = {
        'group1': MagicMock(get_hosts=MagicMock(return_value=[MagicMock(name='host1'), MagicMock(name='host2')])),
        'group2': MagicMock(get_hosts=MagicMock(return_value=[MagicMock(name='host3')])),
    }
    inventory._groups_dict_cache = {}
    return inventory

def test_get_groups_dict(inventory_data):
    # Mock the host names to return actual strings
    inventory_data.groups['group1'].get_hosts.return_value[0].name = 'host1'
    inventory_data.groups['group1'].get_hosts.return_value[1].name = 'host2'
    inventory_data.groups['group2'].get_hosts.return_value[0].name = 'host3'

    result = inventory_data.get_groups_dict()
    expected = {
        'group1': ['host1', 'host2'],
        'group2': ['host3']
    }
    assert result == expected

    # Ensure cache is used on subsequent calls
    inventory_data.groups['group1'].get_hosts.assert_called_once()
    result_cached = inventory_data.get_groups_dict()
    assert result_cached == expected
    inventory_data.groups['group1'].get_hosts.assert_called_once()  # No additional calls
