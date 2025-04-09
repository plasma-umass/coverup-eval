# file: lib/ansible/inventory/data.py:160-178
# asked: {"lines": [165, 174, 176], "branches": [[163, 176], [164, 165], [166, 174], [168, 172]]}
# gained: {"lines": [165, 174, 176], "branches": [[163, 176], [164, 165], [166, 174]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.group import Group
from ansible.module_utils.six import string_types
from ansible.inventory.data import InventoryData

class MockDisplay:
    def __init__(self):
        self.messages = []

    def debug(self, msg):
        self.messages.append(msg)

@pytest.fixture
def inventory_data(monkeypatch):
    inventory = InventoryData()
    inventory.groups = {}
    inventory._groups_dict_cache = {}
    mock_display = MockDisplay()
    monkeypatch.setattr('ansible.inventory.data.display', mock_display)
    return inventory, mock_display

def test_add_group_with_invalid_type(inventory_data):
    inventory, _ = inventory_data
    with pytest.raises(AnsibleError, match="Invalid group name supplied, expected a string but got <class 'int'> for 123"):
        inventory.add_group(123)

def test_add_group_already_in_inventory(inventory_data):
    inventory, mock_display = inventory_data
    inventory.groups['existing_group'] = Group('existing_group')
    result = inventory.add_group('existing_group')
    assert result == 'existing_group'
    assert mock_display.messages == ['group existing_group already in inventory']

def test_add_group_new_group(inventory_data):
    inventory, mock_display = inventory_data
    result = inventory.add_group('new_group')
    assert result == 'new_group'
    assert 'new_group' in inventory.groups
    assert mock_display.messages == ['Added group new_group to inventory']

def test_add_group_empty_name(inventory_data):
    inventory, _ = inventory_data
    with pytest.raises(AnsibleError, match="Invalid empty/false group name provided: "):
        inventory.add_group('')
