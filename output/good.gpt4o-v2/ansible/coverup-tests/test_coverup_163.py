# file: lib/ansible/inventory/data.py:258-273
# asked: {"lines": [258, 260, 261, 262, 263, 264, 265, 266, 268, 269, 270, 272, 273], "branches": [[261, 262], [261, 272], [263, 264], [263, 265], [265, 266], [265, 268]]}
# gained: {"lines": [258, 260, 261, 262, 263, 264, 265, 266, 268, 269, 270, 272, 273], "branches": [[261, 262], [261, 272], [263, 264], [263, 265], [265, 266], [265, 268]]}

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
    return InventoryData()

def test_add_child_group_exists(inventory_data, mocker):
    mocker.patch.object(inventory_data, 'groups', {'group1': MockGroup(), 'group2': MockGroup()})
    result = inventory_data.add_child('group1', 'group2')
    assert result is True
    assert inventory_data._groups_dict_cache == {}

def test_add_child_host_exists(inventory_data, mocker):
    mocker.patch.object(inventory_data, 'groups', {'group1': MockGroup()})
    mocker.patch.object(inventory_data, 'hosts', {'host1': 'host_object'})
    result = inventory_data.add_child('group1', 'host1')
    assert result is True
    assert inventory_data._groups_dict_cache == {}

def test_add_child_unknown_child(inventory_data, mocker):
    mocker.patch.object(inventory_data, 'groups', {'group1': MockGroup()})
    with pytest.raises(AnsibleError, match="unknown_child is not a known host nor group"):
        inventory_data.add_child('group1', 'unknown_child')

def test_add_child_unknown_group(inventory_data):
    with pytest.raises(AnsibleError, match="unknown_group is not a known group"):
        inventory_data.add_child('unknown_group', 'child')
