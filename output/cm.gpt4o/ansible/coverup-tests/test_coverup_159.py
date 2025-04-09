# file lib/ansible/inventory/data.py:160-178
# lines [160, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 176, 178]
# branches ['163->164', '163->176', '164->165', '164->166', '166->167', '166->174', '168->169', '168->172']

import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError
from ansible.inventory.group import Group
from unittest.mock import patch

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_add_group_with_valid_group(inventory_data, mocker):
    mocker.patch.object(inventory_data, 'groups', new_callable=dict)
    mocker.patch('ansible.inventory.data.display')
    
    group_name = "test_group"
    result = inventory_data.add_group(group_name)
    
    assert result == group_name
    assert group_name in inventory_data.groups
    assert isinstance(inventory_data.groups[group_name], Group)

def test_add_group_with_invalid_group_type(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid group name supplied, expected a string but got"):
        inventory_data.add_group(123)

def test_add_group_with_empty_group(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid empty/false group name provided"):
        inventory_data.add_group("")

def test_add_group_already_in_inventory(inventory_data, mocker):
    mocker.patch.object(inventory_data, 'groups', new_callable=dict)
    mocker.patch('ansible.inventory.data.display')
    
    group_name = "existing_group"
    inventory_data.groups[group_name] = Group(group_name)
    
    result = inventory_data.add_group(group_name)
    
    assert result == group_name
    assert group_name in inventory_data.groups
    assert isinstance(inventory_data.groups[group_name], Group)
