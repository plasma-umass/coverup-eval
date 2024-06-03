# file lib/ansible/inventory/data.py:191-234
# lines [191, 194, 195, 196, 199, 200, 201, 202, 204, 206, 207, 208, 209, 210, 211, 213, 214, 215, 218, 219, 220, 221, 223, 225, 227, 228, 229, 230, 232, 234]
# branches ['194->195', '194->232', '195->196', '195->199', '200->201', '200->206', '201->202', '201->204', '206->207', '206->225', '209->210', '209->213', '218->219', '218->227', '219->220', '219->223', '227->228', '227->234']

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.inventory.host import Host
from ansible.utils.display import Display

@pytest.fixture
def inventory_data():
    inventory = InventoryData()
    inventory.groups = {}
    inventory.hosts = {}
    inventory.current_source = None
    inventory.localhost = None
    return inventory

def test_add_host_with_valid_host_and_group(inventory_data, mocker):
    mocker.patch('ansible.inventory.data.basedir', return_value='/some/dir')
    mocker.patch('ansible.inventory.data.display', new_callable=Display)
    inventory_data.groups = {'testgroup': MagicMock()}
    inventory_data.current_source = '/path/to/inventory'

    host = 'testhost'
    group = 'testgroup'
    port = 22

    # Mock the Host class to include a port attribute
    with patch('ansible.inventory.data.Host', autospec=True) as MockHost:
        mock_host_instance = MockHost.return_value
        mock_host_instance.name = host
        mock_host_instance.port = port

        result = inventory_data.add_host(host, group, port)

        assert result == host
        assert host in inventory_data.hosts
        assert inventory_data.hosts[host].name == host
        assert inventory_data.hosts[host].port == port
        assert inventory_data.groups[group].add_host.called
        assert inventory_data.localhost is None

def test_add_host_with_invalid_host_type(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid host name supplied, expected a string but got"):
        inventory_data.add_host(12345)

def test_add_host_with_nonexistent_group(inventory_data):
    with pytest.raises(AnsibleError, match="Could not find group nonexistent_group in inventory"):
        inventory_data.add_host('testhost', 'nonexistent_group')

def test_add_host_with_duplicate_localhost(inventory_data, mocker):
    mocker.patch('ansible.inventory.data.basedir', return_value='/some/dir')
    mocker.patch('ansible.inventory.data.display', new_callable=Display)
    inventory_data.groups = {'testgroup': MagicMock()}
    inventory_data.current_source = '/path/to/inventory'
    inventory_data.localhost = Host('localhost')

    host = 'localhost'
    group = 'testgroup'
    port = 22

    # Mock the Host class to include a port attribute
    with patch('ansible.inventory.data.Host', autospec=True) as MockHost:
        mock_host_instance = MockHost.return_value
        mock_host_instance.name = host
        mock_host_instance.port = port

        result = inventory_data.add_host(host, group, port)

        assert result == host
        assert host in inventory_data.hosts
        assert inventory_data.hosts[host].name == host
        assert inventory_data.hosts[host].port == port
        assert inventory_data.groups[group].add_host.called
        assert inventory_data.localhost.name == 'localhost'
        assert inventory_data.localhost is not inventory_data.hosts[host]

def test_add_host_with_empty_host(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid empty host name provided"):
        inventory_data.add_host('')
