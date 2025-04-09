# file: lib/ansible/inventory/data.py:61-70
# asked: {"lines": [62, 63, 64, 65, 66, 67, 68, 70], "branches": []}
# gained: {"lines": [62, 63, 64, 65, 66, 67, 68, 70], "branches": []}

import pytest
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_data():
    class MockInventoryData(InventoryData):
        def __init__(self):
            self.groups = {'group1': 'data1'}
            self.hosts = {'host1': 'data2'}
            self.localhost = 'localhost_data'
            self.current_source = 'source_data'
            self.processed_sources = ['source1', 'source2']
    return MockInventoryData()

def test_serialize(inventory_data):
    result = inventory_data.serialize()
    
    assert inventory_data._groups_dict_cache is None
    assert result == {
        'groups': {'group1': 'data1'},
        'hosts': {'host1': 'data2'},
        'local': 'localhost_data',
        'source': 'source_data',
        'processed_sources': ['source1', 'source2']
    }
