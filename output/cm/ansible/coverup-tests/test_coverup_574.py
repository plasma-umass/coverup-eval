# file lib/ansible/inventory/host.py:153-159
# lines [153, 154, 155, 156, 157, 159]
# branches []

import pytest
from ansible.inventory.host import Host
from ansible.inventory.group import Group

# Mock class to simulate the behavior of the actual Ansible Inventory
class MockInventory:
    def __init__(self):
        self.groups = {}

    def add_group(self, group):
        self.groups[group.name] = group

    def get_groups_dict(self):
        return self.groups

# Test function to cover get_magic_vars method
def test_get_magic_vars(mocker):
    # Setup
    inventory = MockInventory()
    group1 = Group(name='web')
    group2 = Group(name='db')
    inventory.add_group(group1)
    inventory.add_group(group2)
    inventory.add_group(Group(name='all'))  # 'all' should be excluded from group_names

    host = Host(name='testhost.example.com')
    host.inventory = inventory

    # Mock the get_groups method to return the groups from our mock inventory
    mocker.patch.object(host, 'get_groups', return_value=inventory.get_groups_dict().values())

    # Exercise
    magic_vars = host.get_magic_vars()

    # Verify
    assert magic_vars['inventory_hostname'] == 'testhost.example.com'
    assert magic_vars['inventory_hostname_short'] == 'testhost'
    assert magic_vars['group_names'] == sorted(['web', 'db'])  # 'all' should not be included

    # Cleanup - nothing to do since we used mocker and no external resources were modified
