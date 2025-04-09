# file: lib/ansible/inventory/data.py:191-234
# asked: {"lines": [194, 195, 196, 199, 200, 201, 202, 204, 206, 207, 208, 209, 210, 211, 213, 214, 215, 218, 219, 220, 221, 223, 225, 227, 228, 229, 230, 232, 234], "branches": [[194, 195], [194, 232], [195, 196], [195, 199], [200, 201], [200, 206], [201, 202], [201, 204], [206, 207], [206, 225], [209, 210], [209, 213], [218, 219], [218, 227], [219, 220], [219, 223], [227, 228], [227, 234]]}
# gained: {"lines": [194, 195, 196, 199, 200, 201, 202, 204, 206, 207, 208, 209, 213, 214, 215, 218, 219, 220, 221, 223, 225, 227, 234], "branches": [[194, 195], [195, 196], [195, 199], [200, 201], [200, 206], [201, 202], [201, 204], [206, 207], [206, 225], [209, 213], [218, 219], [218, 227], [219, 220], [219, 223], [227, 234]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.inventory.host import Host
from ansible import constants as C
from ansible.utils.path import basedir

@pytest.fixture
def inventory_data():
    class MockDisplay:
        def debug(self, msg):
            pass
        def vvvv(self, msg):
            pass
        def warning(self, msg):
            pass

    class MockInventoryData(InventoryData):
        def __init__(self):
            self.groups = {}
            self.hosts = {}
            self.current_source = None
            self.localhost = None
            self._groups_dict_cache = {}
            global display
            display = MockDisplay()

        def set_variable(self, host, varname, value):
            self.hosts[host].vars[varname] = value

    return MockInventoryData()

def test_add_host_with_valid_host(inventory_data):
    host = "test_host"
    inventory_data.add_host(host)
    assert host in inventory_data.hosts
    assert inventory_data.hosts[host].name == host

def test_add_host_with_invalid_host_type(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid host name supplied, expected a string but got"):
        inventory_data.add_host(123)

def test_add_host_with_group(inventory_data):
    host = "test_host"
    group = "test_group"
    inventory_data.groups[group] = []
    inventory_data.add_host(host, group)
    assert host in inventory_data.hosts
    assert inventory_data.hosts[host].name == host
    assert inventory_data._groups_dict_cache == {}

def test_add_host_with_nonexistent_group(inventory_data):
    with pytest.raises(AnsibleError, match="Could not find group"):
        inventory_data.add_host("test_host", "nonexistent_group")

def test_add_duplicate_host(inventory_data):
    host = "test_host"
    inventory_data.add_host(host)
    inventory_data.add_host(host)
    assert host in inventory_data.hosts
    assert len(inventory_data.hosts) == 1

def test_add_localhost(inventory_data, monkeypatch):
    host = "localhost"
    monkeypatch.setattr(C, 'LOCALHOST', ['localhost'])
    inventory_data.add_host(host)
    assert inventory_data.localhost == inventory_data.hosts[host]

def test_add_duplicate_localhost(inventory_data, monkeypatch):
    host1 = "localhost"
    host2 = "localhost2"
    monkeypatch.setattr(C, 'LOCALHOST', ['localhost', 'localhost2'])
    inventory_data.add_host(host1)
    inventory_data.add_host(host2)
    assert inventory_data.localhost == inventory_data.hosts[host1]
