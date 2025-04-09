# file: lib/ansible/inventory/data.py:258-273
# asked: {"lines": [258, 260, 261, 262, 263, 264, 265, 266, 268, 269, 270, 272, 273], "branches": [[261, 262], [261, 272], [263, 264], [263, 265], [265, 266], [265, 268]]}
# gained: {"lines": [258, 260, 261, 262, 263, 264, 265, 266, 268, 269, 270, 272, 273], "branches": [[261, 262], [261, 272], [263, 264], [263, 265], [265, 266], [265, 268]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData

class MockGroup:
    def __init__(self):
        self.child_groups = []
        self.hosts = []

    def add_child_group(self, group):
        self.child_groups.append(group)
        return True

    def add_host(self, host):
        self.hosts.append(host)
        return True

@pytest.fixture
def inventory_data():
    data = InventoryData()
    data.groups = {
        'group1': MockGroup(),
        'group2': MockGroup()
    }
    data.hosts = {
        'host1': 'host1_data',
        'host2': 'host2_data'
    }
    data._groups_dict_cache = {}
    return data

def test_add_child_group_to_group(inventory_data):
    result = inventory_data.add_child('group1', 'group2')
    assert result == True
    assert inventory_data.groups['group1'].child_groups == [inventory_data.groups['group2']]
    assert inventory_data._groups_dict_cache == {}

def test_add_child_host_to_group(inventory_data):
    result = inventory_data.add_child('group1', 'host1')
    assert result == True
    assert inventory_data.groups['group1'].hosts == ['host1_data']
    assert inventory_data._groups_dict_cache == {}

def test_add_child_unknown_child(inventory_data):
    with pytest.raises(AnsibleError, match="unknown_child is not a known host nor group"):
        inventory_data.add_child('group1', 'unknown_child')

def test_add_child_unknown_group(inventory_data):
    with pytest.raises(AnsibleError, match="unknown_group is not a known group"):
        inventory_data.add_child('unknown_group', 'host1')
