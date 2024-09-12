# file: lib/ansible/inventory/data.py:160-178
# asked: {"lines": [160, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 176, 178], "branches": [[163, 164], [163, 176], [164, 165], [164, 166], [166, 167], [166, 174], [168, 169], [168, 172]]}
# gained: {"lines": [160, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 176, 178], "branches": [[163, 164], [163, 176], [164, 165], [164, 166], [166, 167], [166, 174], [168, 169]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.group import Group
from ansible.module_utils.six import string_types
from ansible.inventory.data import InventoryData
from unittest.mock import patch

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_add_group_with_valid_string(inventory_data):
    with patch.object(inventory_data, 'groups', new_callable=dict), \
         patch('ansible.inventory.data.display') as mock_display:
        
        group_name = "valid_group"
        result = inventory_data.add_group(group_name)
        
        assert result == group_name
        assert group_name in inventory_data.groups
        mock_display.debug.assert_called_with(f"Added group {group_name} to inventory")

def test_add_group_with_invalid_type(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid group name supplied, expected a string but got"):
        inventory_data.add_group(123)

def test_add_group_with_empty_string(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid empty/false group name provided"):
        inventory_data.add_group("")

def test_add_group_already_exists(inventory_data):
    with patch.object(inventory_data, 'groups', new_callable=dict), \
         patch('ansible.inventory.data.display') as mock_display:
        
        group_name = "existing_group"
        inventory_data.groups[group_name] = Group(group_name)
        
        result = inventory_data.add_group(group_name)
        
        assert result == group_name
        mock_display.debug.assert_called_with(f"group {group_name} already in inventory")
