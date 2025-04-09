# file: lib/ansible/inventory/data.py:72-78
# asked: {"lines": [72, 73, 74, 75, 76, 77, 78], "branches": []}
# gained: {"lines": [72, 73, 74, 75, 76, 77, 78], "branches": []}

import pytest
from ansible.inventory.data import InventoryData

@pytest.fixture
def sample_data():
    return {
        'hosts': {'host1': {}, 'host2': {}},
        'groups': {'group1': {}, 'group2': {}},
        'local': 'localhost',
        'source': 'source1',
        'processed_sources': ['source1', 'source2']
    }

def test_deserialize(sample_data):
    inventory = InventoryData()
    inventory.deserialize(sample_data)
    
    assert inventory.hosts == sample_data['hosts']
    assert inventory.groups == sample_data['groups']
    assert inventory.localhost == sample_data['local']
    assert inventory.current_source == sample_data['source']
    assert inventory.processed_sources == sample_data['processed_sources']
    assert inventory._groups_dict_cache == {}
