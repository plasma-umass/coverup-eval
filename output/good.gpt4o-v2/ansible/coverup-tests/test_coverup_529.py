# file: lib/ansible/inventory/data.py:148-158
# asked: {"lines": [148, 151, 154, 156, 158], "branches": [[154, 156], [154, 158]]}
# gained: {"lines": [148, 151, 154, 156, 158], "branches": [[154, 156], [154, 158]]}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.data import InventoryData
from ansible import constants as C

@pytest.fixture
def inventory_data():
    inventory = InventoryData()
    inventory.hosts = {}
    inventory._create_implicit_localhost = MagicMock(return_value='implicit_localhost')
    return inventory

def test_get_host_existing_host(inventory_data):
    inventory_data.hosts['existing_host'] = 'host_object'
    result = inventory_data.get_host('existing_host')
    assert result == 'host_object'

def test_get_host_implicit_localhost(inventory_data):
    C.LOCALHOST = ['localhost']
    result = inventory_data.get_host('localhost')
    assert result == 'implicit_localhost'
    inventory_data._create_implicit_localhost.assert_called_once_with('localhost')

def test_get_host_nonexistent_host(inventory_data):
    result = inventory_data.get_host('nonexistent_host')
    assert result is None
