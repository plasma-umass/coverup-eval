# file lib/ansible/inventory/data.py:61-70
# lines [61, 62, 63, 64, 65, 66, 67, 68, 70]
# branches []

import pytest
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_data():
    inventory = InventoryData()
    inventory.groups = {'all': {'hosts': ['host1', 'host2'], 'vars': {}}}
    inventory.hosts = {'host1': {}, 'host2': {}}
    inventory.localhost = 'localhost'
    inventory.current_source = 'test_source'
    inventory.processed_sources = ['source1', 'source2']
    return inventory

def test_inventory_data_serialize(inventory_data):
    serialized_data = inventory_data.serialize()
    assert serialized_data['groups'] == inventory_data.groups
    assert serialized_data['hosts'] == inventory_data.hosts
    assert serialized_data['local'] == inventory_data.localhost
    assert serialized_data['source'] == inventory_data.current_source
    assert serialized_data['processed_sources'] == inventory_data.processed_sources
    assert inventory_data._groups_dict_cache is None
