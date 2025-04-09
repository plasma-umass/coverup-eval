# file: lib/ansible/inventory/data.py:42-59
# asked: {"lines": [42, 44, 45, 48, 51, 53, 54, 57, 58, 59], "branches": [[57, 58], [57, 59]]}
# gained: {"lines": [42, 44, 45, 48, 51, 53, 54, 57, 58, 59], "branches": [[57, 58], [57, 59]]}

import pytest
from ansible.inventory.data import InventoryData
from ansible.errors import AnsibleError
from ansible.inventory.group import Group

def test_inventory_data_init(monkeypatch):
    # Mocking the add_group and add_child methods
    def mock_add_group(self, group):
        if group not in self.groups:
            self.groups[group] = Group(group)
    
    def mock_add_child(self, group, child):
        if group in self.groups and child in self.groups:
            self.groups[group].add_child_group(self.groups[child])
        else:
            raise AnsibleError(f'{child} is not a known host nor group')
    
    monkeypatch.setattr(InventoryData, 'add_group', mock_add_group)
    monkeypatch.setattr(InventoryData, 'add_child', mock_add_child)
    
    inventory = InventoryData()
    
    assert 'all' in inventory.groups
    assert 'ungrouped' in inventory.groups
    assert inventory.groups['all'].child_groups[0].name == 'ungrouped'
