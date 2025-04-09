# file: lib/ansible/inventory/data.py:80-102
# asked: {"lines": [80, 82, 83, 85, 87, 88, 91, 92, 94, 95, 97, 98, 100, 102], "branches": [[82, 83], [82, 85], [92, 94], [92, 97]]}
# gained: {"lines": [80, 82, 83, 85, 87, 88, 91, 92, 94, 95, 97, 98, 100, 102], "branches": [[82, 83], [82, 85], [92, 94], [92, 97]]}

import pytest
import sys
from unittest.mock import patch, MagicMock

# Assuming the InventoryData and Host classes are defined in ansible/inventory/data.py
from ansible.inventory.data import InventoryData, Host

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_create_implicit_localhost_with_existing_localhost(inventory_data):
    mock_localhost = MagicMock()
    inventory_data.localhost = mock_localhost

    result = inventory_data._create_implicit_localhost('localhost')

    assert result == mock_localhost

def test_create_implicit_localhost_without_existing_localhost(monkeypatch, inventory_data):
    inventory_data.localhost = None

    mock_host = MagicMock()
    monkeypatch.setattr('ansible.inventory.data.Host', lambda pattern: mock_host)

    with patch('sys.executable', '/usr/bin/python3'):
        result = inventory_data._create_implicit_localhost('localhost')

    assert result == mock_host
    assert result.address == "127.0.0.1"
    assert result.implicit is True
    assert result.set_variable.call_count == 2
    result.set_variable.assert_any_call("ansible_python_interpreter", '/usr/bin/python3')
    result.set_variable.assert_any_call("ansible_connection", 'local')
    assert inventory_data.localhost == result

def test_create_implicit_localhost_without_sys_executable(monkeypatch, inventory_data):
    inventory_data.localhost = None

    mock_host = MagicMock()
    monkeypatch.setattr('ansible.inventory.data.Host', lambda pattern: mock_host)
    monkeypatch.setattr('sys.executable', None)

    with patch('ansible.inventory.data.display.warning') as mock_warning:
        result = inventory_data._create_implicit_localhost('localhost')

    assert result == mock_host
    assert result.address == "127.0.0.1"
    assert result.implicit is True
    assert result.set_variable.call_count == 2
    result.set_variable.assert_any_call("ansible_python_interpreter", '/usr/bin/python')
    result.set_variable.assert_any_call("ansible_connection", 'local')
    assert inventory_data.localhost == result
    mock_warning.assert_called_once_with(
        'Unable to determine python interpreter from sys.executable. Using /usr/bin/python default. '
        'You can correct this by setting ansible_python_interpreter for localhost'
    )
