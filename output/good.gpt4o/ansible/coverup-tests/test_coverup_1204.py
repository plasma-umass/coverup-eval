# file lib/ansible/inventory/data.py:191-234
# lines [220, 221, 225]
# branches ['200->206', '206->225', '219->220', '227->234']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.inventory.host import Host
from ansible.utils.display import Display
import ansible.constants as C

@pytest.fixture
def inventory_data(mocker):
    inventory = InventoryData()
    inventory.groups = {}
    inventory.hosts = {}
    inventory.current_source = None
    inventory.localhost = None
    mocker.patch('ansible.inventory.data.basedir', return_value='/mocked/path')
    mocker.patch('ansible.utils.display.Display', return_value=Display())
    return inventory

def test_add_host_with_group(inventory_data, mocker):
    inventory_data.groups = {'testgroup': mocker.Mock()}
    inventory_data.add_host('testhost', 'testgroup')
    assert 'testhost' in inventory_data.hosts
    assert inventory_data.groups['testgroup'].add_host.called

def test_add_host_without_group(inventory_data):
    inventory_data.add_host('testhost')
    assert 'testhost' in inventory_data.hosts

def test_add_duplicate_host(inventory_data):
    inventory_data.add_host('testhost')
    inventory_data.add_host('testhost')
    assert 'testhost' in inventory_data.hosts

def test_add_localhost(inventory_data):
    inventory_data.add_host('localhost')
    assert inventory_data.localhost is not None

def test_add_duplicate_localhost(inventory_data, mocker):
    mocker.patch.object(C, 'LOCALHOST', ['localhost'])
    inventory_data.add_host('localhost')
    inventory_data.add_host('localhost')
    assert inventory_data.localhost is not None

def test_add_host_invalid_group(inventory_data):
    with pytest.raises(AnsibleError, match="Could not find group invalidgroup in inventory"):
        inventory_data.add_host('testhost', 'invalidgroup')

def test_add_host_invalid_name(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid host name supplied, expected a string but got"):
        inventory_data.add_host(123)

def test_add_empty_host(inventory_data):
    with pytest.raises(AnsibleError, match="Invalid empty host name provided"):
        inventory_data.add_host('')
