# file: lib/ansible/inventory/data.py:80-102
# asked: {"lines": [82, 83, 85, 87, 88, 91, 92, 94, 95, 97, 98, 100, 102], "branches": [[82, 83], [82, 85], [92, 94], [92, 97]]}
# gained: {"lines": [82, 83, 85, 87, 88, 91, 92, 94, 95, 97, 98, 100, 102], "branches": [[82, 83], [82, 85], [92, 94], [92, 97]]}

import pytest
import sys
from unittest.mock import patch, MagicMock
from ansible.inventory.data import InventoryData
from ansible.inventory.host import Host

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_create_implicit_localhost_with_existing_localhost(inventory_data):
    existing_host = Host('localhost')
    inventory_data.localhost = existing_host

    new_host = inventory_data._create_implicit_localhost('localhost')

    assert new_host == existing_host
    assert new_host.address == 'localhost'
    assert not new_host.implicit

def test_create_implicit_localhost_without_existing_localhost(inventory_data):
    pattern = 'localhost'
    new_host = inventory_data._create_implicit_localhost(pattern)

    assert new_host.address == '127.0.0.1'
    assert new_host.implicit
    assert new_host.vars['ansible_python_interpreter'] == sys.executable
    assert new_host.vars['ansible_connection'] == 'local'
    assert inventory_data.localhost == new_host

@patch('sys.executable', None)
@patch('ansible.inventory.data.display')
def test_create_implicit_localhost_without_sys_executable(mock_display, inventory_data):
    pattern = 'localhost'
    new_host = inventory_data._create_implicit_localhost(pattern)

    assert new_host.address == '127.0.0.1'
    assert new_host.implicit
    assert new_host.vars['ansible_python_interpreter'] == '/usr/bin/python'
    assert new_host.vars['ansible_connection'] == 'local'
    assert inventory_data.localhost == new_host
    mock_display.warning.assert_called_once_with(
        'Unable to determine python interpreter from sys.executable. Using /usr/bin/python default. '
        'You can correct this by setting ansible_python_interpreter for localhost'
    )
