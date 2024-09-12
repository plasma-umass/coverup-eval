# file: lib/ansible/inventory/data.py:72-78
# asked: {"lines": [72, 73, 74, 75, 76, 77, 78], "branches": []}
# gained: {"lines": [72, 73, 74, 75, 76, 77, 78], "branches": []}

import pytest
from ansible.inventory.data import InventoryData

def test_deserialize():
    data = {
        'hosts': {'host1': {}, 'host2': {}},
        'groups': {'group1': {}, 'group2': {}},
        'local': 'localhost',
        'source': 'source1',
        'processed_sources': ['source1', 'source2']
    }
    
    inventory = InventoryData()
    inventory.deserialize(data)
    
    assert inventory.hosts == data['hosts']
    assert inventory.groups == data['groups']
    assert inventory.localhost == data['local']
    assert inventory.current_source == data['source']
    assert inventory.processed_sources == data['processed_sources']
    assert inventory._groups_dict_cache == {}

