# file: lib/ansible/inventory/data.py:275-283
# asked: {"lines": [279, 280, 281, 283], "branches": [[279, 280], [279, 283], [280, 281], [280, 283]]}
# gained: {"lines": [279, 280, 281, 283], "branches": [[279, 280], [279, 283], [280, 281], [280, 283]]}

import pytest
from ansible.inventory.data import InventoryData
from unittest.mock import MagicMock

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_get_groups_dict_cache_empty(inventory_data):
    # Setup
    host1 = MagicMock()
    host1.name = 'host1'
    host2 = MagicMock()
    host2.name = 'host2'
    group_mock = MagicMock()
    group_mock.get_hosts.return_value = [host1, host2]
    inventory_data.groups = {'group1': group_mock}
    inventory_data._groups_dict_cache = {}

    # Execute
    result = inventory_data.get_groups_dict()

    # Verify
    assert result == {'group1': ['host1', 'host2']}
    assert inventory_data._groups_dict_cache == {'group1': ['host1', 'host2']}

def test_get_groups_dict_cache_not_empty(inventory_data):
    # Setup
    inventory_data._groups_dict_cache = {'group1': ['host1', 'host2']}

    # Execute
    result = inventory_data.get_groups_dict()

    # Verify
    assert result == {'group1': ['host1', 'host2']}
    assert inventory_data._groups_dict_cache == {'group1': ['host1', 'host2']}
