# file: lib/ansible/inventory/data.py:191-234
# asked: {"lines": [196, 204, 223, 225, 232], "branches": [[194, 232], [195, 196], [200, 206], [201, 204], [206, 225], [219, 223], [227, 234]]}
# gained: {"lines": [196, 204, 225, 232], "branches": [[194, 232], [195, 196], [200, 206], [201, 204], [206, 225], [227, 234]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.inventory.host import Host
from ansible.utils.display import Display

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_add_host_invalid_host_type(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid host name supplied, expected a string but got"):
        inventory_data.add_host(123)

def test_add_host_group_not_found(inventory_data, monkeypatch):
    monkeypatch.setattr(inventory_data, 'groups', {})
    with pytest.raises(AnsibleError, match="Could not find group"):
        inventory_data.add_host('host1', group='nonexistent_group')

def test_add_host_duplicate_localhost_warning(inventory_data, monkeypatch):
    monkeypatch.setattr(inventory_data, 'hosts', {})
    monkeypatch.setattr(inventory_data, 'current_source', None)
    monkeypatch.setattr(inventory_data, 'localhost', None)
    monkeypatch.setattr(Display, 'warning', lambda msg: None)
    inventory_data.add_host('localhost')
    inventory_data.add_host('localhost')
    assert inventory_data.localhost.name == 'localhost'

def test_add_host_empty_host_name(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid empty host name provided"):
        inventory_data.add_host('')

def test_add_host_to_group(inventory_data, monkeypatch):
    class MockGroup:
        def add_host(self, host):
            self.host = host

    mock_group = MockGroup()
    monkeypatch.setattr(inventory_data, 'groups', {'group1': mock_group})
    monkeypatch.setattr(inventory_data, 'hosts', {})
    monkeypatch.setattr(inventory_data, 'current_source', None)
    inventory_data.add_host('host1', group='group1')
    assert mock_group.host.name == 'host1'
    assert 'host1' in inventory_data.hosts
    assert inventory_data.hosts['host1'].name == 'host1'
