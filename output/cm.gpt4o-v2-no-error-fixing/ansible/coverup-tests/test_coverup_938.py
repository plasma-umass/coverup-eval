# file: lib/ansible/inventory/data.py:236-243
# asked: {"lines": [], "branches": [[238, 241]]}
# gained: {"lines": [], "branches": [[238, 241]]}

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
    inv.hosts = {}
    inv.groups = {}
    return inv

def test_remove_host_from_hosts(inventory_data):
    host = MockHost('test_host')
    inventory_data.hosts[host.name] = host
    inventory_data.remove_host(host)
    assert host.name not in inventory_data.hosts

def test_remove_host_from_groups(inventory_data):
    host = MockHost('test_host')
    group = MockGroup()
    group.hosts[host.name] = host
    inventory_data.groups['test_group'] = group
    inventory_data.remove_host(host)
    assert host.name not in group.hosts
