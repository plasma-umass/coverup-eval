# file: lib/ansible/inventory/data.py:258-273
# asked: {"lines": [265, 266, 268, 272], "branches": [[261, 272], [263, 265], [265, 266], [265, 268]]}
# gained: {"lines": [265, 266, 268, 272], "branches": [[261, 272], [263, 265], [265, 266], [265, 268]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData

class MockGroup:
    def add_child_group(self, group):
        return True

    def add_host(self, host):
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
    return data

def test_add_child_group_known_group(inventory_data):
    result = inventory_data.add_child('group1', 'group2')
    assert result is True

def test_add_child_host_known_group(inventory_data):
    result = inventory_data.add_child('group1', 'host1')
    assert result is True

def test_add_child_unknown_child(inventory_data):
    with pytest.raises(AnsibleError, match="unknown_child is not a known host nor group"):
        inventory_data.add_child('group1', 'unknown_child')

def test_add_child_unknown_group(inventory_data):
    with pytest.raises(AnsibleError, match="unknown_group is not a known group"):
        inventory_data.add_child('unknown_group', 'host1')
