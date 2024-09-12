# file: lib/ansible/inventory/data.py:42-59
# asked: {"lines": [42, 44, 45, 48, 51, 53, 54, 57, 58, 59], "branches": [[57, 58], [57, 59]]}
# gained: {"lines": [42, 44, 45, 48, 51, 53, 54, 57, 58, 59], "branches": [[57, 58], [57, 59]]}

import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError
from ansible.inventory.group import Group

def test_inventory_data_init(mocker):
    mocker.patch('ansible.inventory.data.InventoryData.add_group')
    mocker.patch('ansible.inventory.data.InventoryData.add_child')
    
    inventory = InventoryData()
    
    assert inventory.groups == {}
    assert inventory.hosts == {}
    assert inventory._groups_dict_cache == {}
    assert inventory.localhost is None
    assert inventory.current_source is None
    assert inventory.processed_sources == []
    
    inventory.add_group.assert_any_call('all')
    inventory.add_group.assert_any_call('ungrouped')
    inventory.add_child.assert_called_once_with('all', 'ungrouped')

def test_add_group():
    inventory = InventoryData()
    
    group_name = 'testgroup'
    result = inventory.add_group(group_name)
    
    assert result == group_name
    assert group_name in inventory.groups
    assert isinstance(inventory.groups[group_name], Group)
    
    with pytest.raises(AnsibleError):
        inventory.add_group(None)
    
    with pytest.raises(AnsibleError):
        inventory.add_group(123)

def test_add_child():
    inventory = InventoryData()
    inventory.add_group('parent')
    inventory.add_group('child')
    
    result = inventory.add_child('parent', 'child')
    
    assert result is True
    assert inventory.groups['child'] in inventory.groups['parent'].child_groups
    
    with pytest.raises(AnsibleError):
        inventory.add_child('parent', 'unknown')
    
    with pytest.raises(AnsibleError):
        inventory.add_child('unknown', 'child')
