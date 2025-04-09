# file: lib/ansible/inventory/data.py:61-70
# asked: {"lines": [61, 62, 63, 64, 65, 66, 67, 68, 70], "branches": []}
# gained: {"lines": [61, 62, 63, 64, 65, 66, 67, 68, 70], "branches": []}

import pytest
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_serialize(inventory_data):
    inventory_data.groups = {'group1': 'data1'}
    inventory_data.hosts = {'host1': 'data2'}
    inventory_data.localhost = 'localhost_data'
    inventory_data.current_source = 'source_data'
    inventory_data.processed_sources = ['source1', 'source2']

    serialized_data = inventory_data.serialize()

    assert serialized_data == {
        'groups': {'group1': 'data1'},
        'hosts': {'host1': 'data2'},
        'local': 'localhost_data',
        'source': 'source_data',
        'processed_sources': ['source1', 'source2']
    }
    assert inventory_data._groups_dict_cache is None
