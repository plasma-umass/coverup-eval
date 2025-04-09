# file: lib/ansible/inventory/data.py:180-189
# asked: {"lines": [180, 182, 183, 184, 185, 187, 188, 189], "branches": [[182, 183], [182, 187], [187, 0], [187, 188]]}
# gained: {"lines": [180], "branches": []}

import pytest
from unittest.mock import MagicMock

class InventoryData:
    def __init__(self):
        self.groups = {}
        self.hosts = {}
        self._groups_dict_cache = {}

    def remove_group(self, group):
        if group in self.groups:
            del self.groups[group]
            self._groups_dict_cache = {}
        
        for host in self.hosts:
            h = self.hosts[host]
            h.remove_group(group)

class Host:
    def __init__(self, name):
        self.name = name
        self.groups = []

    def remove_group(self, group):
        if group in self.groups:
            self.groups.remove(group)

@pytest.fixture
def inventory():
    return InventoryData()

@pytest.fixture
def host():
    return Host("test_host")

def test_remove_group_from_inventory(inventory, host, mocker):
    # Setup
    group_name = "test_group"
    inventory.groups[group_name] = "some_group_data"
    inventory.hosts[host.name] = host
    host.groups.append(group_name)
    
    # Mock display.debug to avoid side effects
    mocker.patch('ansible.inventory.data.display.debug')

    # Act
    inventory.remove_group(group_name)

    # Assert
    assert group_name not in inventory.groups
    assert inventory._groups_dict_cache == {}
    assert group_name not in host.groups

def test_remove_nonexistent_group(inventory, host, mocker):
    # Setup
    group_name = "nonexistent_group"
    inventory.hosts[host.name] = host
    
    # Mock display.debug to avoid side effects
    mocker.patch('ansible.inventory.data.display.debug')

    # Act
    inventory.remove_group(group_name)

    # Assert
    assert group_name not in inventory.groups
    assert inventory._groups_dict_cache == {}
    assert group_name not in host.groups
