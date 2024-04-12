# file lib/ansible/inventory/data.py:148-158
# lines [148, 151, 154, 156, 158]
# branches ['154->156', '154->158']

import pytest
from ansible.inventory.data import InventoryData
from ansible import constants as C

# Mocking the constants to include a test localhost
C.LOCALHOST = ['test_localhost']

@pytest.fixture
def inventory_data():
    return InventoryData()

@pytest.fixture
def mock_create_implicit_localhost(mocker):
    return mocker.patch.object(InventoryData, '_create_implicit_localhost')

def test_get_host_with_implicit_localhost(inventory_data, mock_create_implicit_localhost):
    hostname = 'test_localhost'
    inventory_data.get_host(hostname)
    mock_create_implicit_localhost.assert_called_once_with(hostname)

def test_get_host_without_implicit_localhost(inventory_data):
    hostname = 'nonexistent_host'
    result = inventory_data.get_host(hostname)
    assert result is None

def test_get_host_with_existing_host(inventory_data):
    hostname = 'existing_host'
    inventory_data.hosts[hostname] = 'mock_host_object'
    result = inventory_data.get_host(hostname)
    assert result == 'mock_host_object'
