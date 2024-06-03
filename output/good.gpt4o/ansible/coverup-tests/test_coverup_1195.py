# file lib/ansible/inventory/data.py:72-78
# lines [73, 74, 75, 76, 77, 78]
# branches []

import pytest
from ansible.inventory.data import InventoryData

def test_inventory_data_deserialize():
    data = {
        'hosts': ['host1', 'host2'],
        'groups': ['group1', 'group2'],
        'local': 'localhost',
        'source': 'source1',
        'processed_sources': ['source1', 'source2']
    }
    
    inventory_data = InventoryData()
    inventory_data.deserialize(data)
    
    assert inventory_data._groups_dict_cache == {}
    assert inventory_data.hosts == ['host1', 'host2']
    assert inventory_data.groups == ['group1', 'group2']
    assert inventory_data.localhost == 'localhost'
    assert inventory_data.current_source == 'source1'
    assert inventory_data.processed_sources == ['source1', 'source2']
