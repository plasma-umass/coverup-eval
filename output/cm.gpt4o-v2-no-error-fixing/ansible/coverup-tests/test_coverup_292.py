# file: lib/ansible/inventory/data.py:61-70
# asked: {"lines": [61, 62, 63, 64, 65, 66, 67, 68, 70], "branches": []}
# gained: {"lines": [61, 62, 63, 64, 65, 66, 67, 68, 70], "branches": []}

import pytest
from ansible.inventory.data import InventoryData

def test_serialize():
    inventory = InventoryData()
    inventory.groups = {'group1': 'data1'}
    inventory.hosts = {'host1': 'data2'}
    inventory.localhost = 'localhost_data'
    inventory.current_source = 'source_data'
    inventory.processed_sources = ['source1', 'source2']

    expected_data = {
        'groups': {'group1': 'data1'},
        'hosts': {'host1': 'data2'},
        'local': 'localhost_data',
        'source': 'source_data',
        'processed_sources': ['source1', 'source2']
    }

    assert inventory.serialize() == expected_data
    assert inventory._groups_dict_cache is None
