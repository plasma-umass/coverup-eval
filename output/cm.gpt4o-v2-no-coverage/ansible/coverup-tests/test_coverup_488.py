# file: lib/ansible/inventory/data.py:236-243
# asked: {"lines": [236, 238, 239, 241, 242, 243], "branches": [[238, 239], [238, 241], [241, 0], [241, 242]]}
# gained: {"lines": [236, 238, 239, 241, 242, 243], "branches": [[238, 239], [238, 241], [241, 0], [241, 242]]}

import pytest

class MockHost:
    def __init__(self, name):
        self.name = name

class MockGroup:
    def __init__(self):
        self.hosts = {}

    def remove_host(self, host):
        if host.name in self.hosts:
            del self.hosts[host.name]

@pytest.fixture
def inventory_data():
    from ansible.inventory.data import InventoryData
    inv = InventoryData()
    inv.groups = {
        'group1': MockGroup(),
        'group2': MockGroup()
    }
    inv.hosts = {
        'host1': MockHost('host1'),
        'host2': MockHost('host2')
    }
    inv.groups['group1'].hosts = {'host1': MockHost('host1')}
    inv.groups['group2'].hosts = {'host2': MockHost('host2')}
    return inv

def test_remove_host_from_inventory(inventory_data):
    host_to_remove = MockHost('host1')
    inventory_data.remove_host(host_to_remove)
    
    assert 'host1' not in inventory_data.hosts
    assert 'host1' not in inventory_data.groups['group1'].hosts
    assert 'host1' not in inventory_data.groups['group2'].hosts

def test_remove_nonexistent_host(inventory_data):
    host_to_remove = MockHost('host3')
    inventory_data.remove_host(host_to_remove)
    
    assert 'host3' not in inventory_data.hosts
    assert 'host1' in inventory_data.hosts
    assert 'host2' in inventory_data.hosts
    assert 'host1' in inventory_data.groups['group1'].hosts
    assert 'host2' in inventory_data.groups['group2'].hosts
