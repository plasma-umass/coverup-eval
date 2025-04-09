# file lib/ansible/inventory/data.py:258-273
# lines [265, 266, 268, 272]
# branches ['261->272', '263->265', '265->266', '265->268']

import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError

@pytest.fixture
def inventory_data():
    inv_data = InventoryData()
    inv_data.groups = {
        'group1': MockGroup(),
        'group2': MockGroup()
    }
    inv_data.hosts = {
        'host1': MockHost()
    }
    return inv_data

class MockGroup:
    def add_child_group(self, group):
        return True

    def add_host(self, host):
        return True

class MockHost:
    pass

def test_add_child_group_not_known_group(inventory_data):
    with pytest.raises(AnsibleError, match="not a known group"):
        inventory_data.add_child('unknown_group', 'group1')

def test_add_child_group_not_known_host_nor_group(inventory_data):
    with pytest.raises(AnsibleError, match="not a known host nor group"):
        inventory_data.add_child('group1', 'unknown_child')

def test_add_child_group_known_group(inventory_data):
    assert inventory_data.add_child('group1', 'group2') is True

def test_add_child_host_known_host(inventory_data):
    assert inventory_data.add_child('group1', 'host1') is True
