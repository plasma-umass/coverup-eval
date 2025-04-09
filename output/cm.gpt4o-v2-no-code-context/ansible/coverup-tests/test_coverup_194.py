# file: lib/ansible/inventory/data.py:258-273
# asked: {"lines": [258, 260, 261, 262, 263, 264, 265, 266, 268, 269, 270, 272, 273], "branches": [[261, 262], [261, 272], [263, 264], [263, 265], [265, 266], [265, 268]]}
# gained: {"lines": [258], "branches": []}

import pytest
from ansible.errors import AnsibleError

class MockGroup:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.hosts = []

    def add_child_group(self, group):
        self.children.append(group)
        return True

    def add_host(self, host):
        self.hosts.append(host)
        return True

class MockDisplay:
    @staticmethod
    def debug(msg):
        pass

class InventoryData:
    def __init__(self):
        self.groups = {}
        self.hosts = {}
        self._groups_dict_cache = {}

    def add_child(self, group, child):
        ''' Add host or group to group '''
        added = False
        if group in self.groups:
            g = self.groups[group]
            if child in self.groups:
                added = g.add_child_group(self.groups[child])
            elif child in self.hosts:
                added = g.add_host(self.hosts[child])
            else:
                raise AnsibleError("%s is not a known host nor group" % child)
            self._groups_dict_cache = {}
            MockDisplay.debug('Group %s now contains %s' % (group, child))
        else:
            raise AnsibleError("%s is not a known group" % group)
        return added

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_add_child_group_to_group(inventory_data, monkeypatch):
    group1 = MockGroup('group1')
    group2 = MockGroup('group2')
    inventory_data.groups['group1'] = group1
    inventory_data.groups['group2'] = group2

    monkeypatch.setattr('ansible.inventory.data.display', MockDisplay)
    result = inventory_data.add_child('group1', 'group2')
    assert result is True
    assert group2 in group1.children

def test_add_child_host_to_group(inventory_data, monkeypatch):
    group1 = MockGroup('group1')
    host1 = 'host1'
    inventory_data.groups['group1'] = group1
    inventory_data.hosts['host1'] = host1

    monkeypatch.setattr('ansible.inventory.data.display', MockDisplay)
    result = inventory_data.add_child('group1', 'host1')
    assert result is True
    assert host1 in group1.hosts

def test_add_child_unknown_child(inventory_data, monkeypatch):
    group1 = MockGroup('group1')
    inventory_data.groups['group1'] = group1

    monkeypatch.setattr('ansible.inventory.data.display', MockDisplay)
    with pytest.raises(AnsibleError, match="unknown_child is not a known host nor group"):
        inventory_data.add_child('group1', 'unknown_child')

def test_add_child_unknown_group(inventory_data, monkeypatch):
    monkeypatch.setattr('ansible.inventory.data.display', MockDisplay)
    with pytest.raises(AnsibleError, match="unknown_group is not a known group"):
        inventory_data.add_child('unknown_group', 'child')
