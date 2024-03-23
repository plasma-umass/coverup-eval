# file lib/ansible/inventory/data.py:275-283
# lines [275, 279, 280, 281, 283]
# branches ['279->280', '279->283', '280->281', '280->283']

import pytest
from ansible.inventory.data import InventoryData
from ansible.inventory.group import Group
from ansible.inventory.host import Host
from collections.abc import MutableMapping

# Since iteritems is not defined, we'll create a mock for it
def iteritems_mock(dictionary):
    return dictionary.items()

# Test function to improve coverage
def test_get_groups_dict(mocker):
    # Mock iteritems to return a controlled dictionary
    mocker.patch('ansible.inventory.data.iteritems', side_effect=iteritems_mock)

    # Create an instance of InventoryData
    inventory_data = InventoryData()

    # Initialize the _groups_dict_cache to an empty dict to simulate a cache miss
    inventory_data._groups_dict_cache = {}

    # Create groups with hosts
    group1 = Group(name='group1')
    host1 = Host(name='host1')
    group1.add_host(host1)

    group2 = Group(name='group2')
    host2 = Host(name='host2')
    group2.add_host(host2)

    # Add groups to the inventory_data
    inventory_data.groups = {'group1': group1, 'group2': group2}

    # Call get_groups_dict to populate the cache
    groups_dict = inventory_data.get_groups_dict()

    # Assertions to ensure the cache is populated correctly
    assert isinstance(groups_dict, MutableMapping), "The cache should be a dictionary"
    assert 'group1' in groups_dict, "group1 should be a key in the groups_dict"
    assert 'group2' in groups_dict, "group2 should be a key in the groups_dict"
    assert groups_dict['group1'] == ['host1'], "group1 should have host1"
    assert groups_dict['group2'] == ['host2'], "group2 should have host2"

    # Call get_groups_dict again to hit the cache
    cached_groups_dict = inventory_data.get_groups_dict()

    # Assertions to ensure the cache hit returns the same data
    assert cached_groups_dict is groups_dict, "The cached data should be returned on subsequent calls"
