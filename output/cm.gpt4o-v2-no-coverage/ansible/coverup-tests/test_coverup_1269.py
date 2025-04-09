# file: lib/ansible/inventory/data.py:191-234
# asked: {"lines": [210, 211, 228, 229, 230, 232], "branches": [[194, 232], [209, 210], [227, 228]]}
# gained: {"lines": [228, 229, 230, 232], "branches": [[194, 232], [227, 228]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible import constants as C
from ansible.utils.path import basedir

class MockDisplay:
    def debug(self, msg):
        pass

    def vvvv(self, msg):
        pass

    def warning(self, msg):
        pass

@pytest.fixture
def inventory_data(monkeypatch):
    inventory = InventoryData()
    inventory.groups = {}
    inventory.hosts = {}
    inventory.current_source = None
    inventory.localhost = None
    inventory._groups_dict_cache = {}
    monkeypatch.setattr('ansible.inventory.data.display', MockDisplay())
    return inventory

def test_add_host_with_valid_host(inventory_data):
    host = 'test_host'
    result = inventory_data.add_host(host)
    assert result == host
    assert host in inventory_data.hosts
    assert isinstance(inventory_data.hosts[host], Host)

def test_add_host_with_invalid_host_type(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid host name supplied, expected a string but got"):
        inventory_data.add_host(123)

def test_add_host_with_empty_host(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid empty host name provided"):
        inventory_data.add_host('')

def test_add_host_with_group(inventory_data):
    host = 'test_host'
    group = 'test_group'
    inventory_data.add_group(group)
    result = inventory_data.add_host(host, group=group)
    assert result == host
    assert host in inventory_data.hosts
    assert isinstance(inventory_data.hosts[host], Host)
    assert inventory_data.hosts[host] in inventory_data.groups[group].hosts

def test_add_host_with_nonexistent_group(inventory_data):
    with pytest.raises(AnsibleError, match="Could not find group"):
        inventory_data.add_host('test_host', group='nonexistent_group')

def test_add_host_with_port(inventory_data):
    host = 'test_host'
    port = 2222
    result = inventory_data.add_host(host, port=port)
    assert result == host
    assert host in inventory_data.hosts
    assert isinstance(inventory_data.hosts[host], Host)
    assert inventory_data.hosts[host].vars['ansible_port'] == port

def test_add_duplicate_host(inventory_data):
    host = 'test_host'
    inventory_data.add_host(host)
    result = inventory_data.add_host(host)
    assert result == host
    assert len(inventory_data.hosts) == 1

def test_add_localhost(inventory_data):
    host = 'localhost'
    result = inventory_data.add_host(host)
    assert result == host
    assert inventory_data.localhost == inventory_data.hosts[host]

def test_add_duplicate_localhost(inventory_data, monkeypatch):
    host = 'localhost'
    inventory_data.add_host(host)
    mock_display = MockDisplay()
    monkeypatch.setattr('ansible.inventory.data.display', mock_display)
    result = inventory_data.add_host(host)
    assert result == host
    assert inventory_data.localhost == inventory_data.hosts[host]
