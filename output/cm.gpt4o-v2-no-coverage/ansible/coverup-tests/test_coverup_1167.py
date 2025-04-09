# file: lib/ansible/inventory/data.py:148-158
# asked: {"lines": [151, 154, 156, 158], "branches": [[154, 156], [154, 158]]}
# gained: {"lines": [151, 154, 156, 158], "branches": [[154, 156], [154, 158]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.data import InventoryData
from ansible.inventory.host import Host
from ansible import constants as C

@pytest.fixture
def inventory_data():
    inventory = InventoryData()
    inventory.hosts = {}
    inventory.localhost = None
    return inventory

def test_get_host_existing_host(inventory_data):
    host = Host('existing_host')
    inventory_data.hosts['existing_host'] = host
    result = inventory_data.get_host('existing_host')
    assert result == host

def test_get_host_implicit_localhost(inventory_data):
    with patch('ansible.inventory.data.InventoryData._create_implicit_localhost', return_value=Host('localhost')) as mock_create:
        result = inventory_data.get_host('localhost')
        assert result.name == 'localhost'
        mock_create.assert_called_once_with('localhost')

def test_get_host_nonexistent_host(inventory_data):
    result = inventory_data.get_host('nonexistent_host')
    assert result is None

def test_create_implicit_localhost_no_localhost(inventory_data):
    with patch('sys.executable', '/usr/bin/python3'):
        result = inventory_data._create_implicit_localhost('localhost')
        assert result.name == 'localhost'
        assert result.address == '127.0.0.1'
        assert result.implicit is True
        assert result.vars['ansible_python_interpreter'] == '/usr/bin/python3'
        assert result.vars['ansible_connection'] == 'local'
        assert inventory_data.localhost == result

def test_create_implicit_localhost_with_localhost(inventory_data):
    existing_localhost = Host('localhost')
    inventory_data.localhost = existing_localhost
    result = inventory_data._create_implicit_localhost('localhost')
    assert result == existing_localhost
