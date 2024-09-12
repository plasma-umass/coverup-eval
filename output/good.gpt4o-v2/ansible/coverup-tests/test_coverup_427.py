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
    return inv

def test_remove_host_from_inventory(inventory_data):
    host = MockHost('test_host')
    group = MockGroup()
    
    inventory_data.hosts[host.name] = host
    inventory_data.groups['test_group'] = group
    group.hosts[host.name] = host
    
    inventory_data.remove_host(host)
    
    assert host.name not in inventory_data.hosts
    assert host.name not in group.hosts

def test_remove_nonexistent_host(inventory_data):
    host = MockHost('nonexistent_host')
    group = MockGroup()
    
    inventory_data.groups['test_group'] = group
    
    inventory_data.remove_host(host)
    
    assert host.name not in inventory_data.hosts
    assert host.name not in group.hosts
