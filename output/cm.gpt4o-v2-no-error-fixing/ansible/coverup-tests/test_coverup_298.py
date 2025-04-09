# file: lib/ansible/inventory/data.py:275-283
# asked: {"lines": [275, 279, 280, 281, 283], "branches": [[279, 280], [279, 283], [280, 281], [280, 283]]}
# gained: {"lines": [275, 279, 280, 281, 283], "branches": [[279, 280], [279, 283], [280, 281], [280, 283]]}

import pytest
from ansible.module_utils.six import iteritems
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_get_groups_dict_cache_empty(inventory_data):
    inventory_data.groups = {
        'group1': MockGroup(['host1', 'host2']),
        'group2': MockGroup(['host3'])
    }
    inventory_data._groups_dict_cache = {}
    
    result = inventory_data.get_groups_dict()
    
    assert result == {
        'group1': ['host1', 'host2'],
        'group2': ['host3']
    }

def test_get_groups_dict_cache_not_empty(inventory_data):
    inventory_data._groups_dict_cache = {
        'group1': ['host1', 'host2']
    }
    
    result = inventory_data.get_groups_dict()
    
    assert result == {
        'group1': ['host1', 'host2']
    }

class MockGroup:
    def __init__(self, hosts):
        self.hosts = hosts
    
    def get_hosts(self):
        return [MockHost(name) for name in self.hosts]

class MockHost:
    def __init__(self, name):
        self.name = name
