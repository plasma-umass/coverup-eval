# file: lib/ansible/inventory/data.py:148-158
# asked: {"lines": [148, 151, 154, 156, 158], "branches": [[154, 156], [154, 158]]}
# gained: {"lines": [148, 151, 154, 156, 158], "branches": [[154, 156], [154, 158]]}

import pytest
from ansible.inventory.data import InventoryData
from ansible import constants as C

class MockHost:
    pass

@pytest.fixture
def inventory_data():
    class MockInventoryData(InventoryData):
        def __init__(self):
            self.hosts = {}

        def _create_implicit_localhost(self, hostname):
            return MockHost()

    return MockInventoryData()

def test_get_host_existing_host(inventory_data):
    host = MockHost()
    inventory_data.hosts['existing_host'] = host
    assert inventory_data.get_host('existing_host') is host

def test_get_host_implicit_localhost(inventory_data, monkeypatch):
    monkeypatch.setattr(C, 'LOCALHOST', ['localhost', '127.0.0.1'])
    host = inventory_data.get_host('localhost')
    assert isinstance(host, MockHost)

def test_get_host_nonexistent_host(inventory_data, monkeypatch):
    monkeypatch.setattr(C, 'LOCALHOST', ['localhost', '127.0.0.1'])
    assert inventory_data.get_host('nonexistent_host') is None
