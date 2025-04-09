# file: lib/ansible/vars/hostvars.py:64-66
# asked: {"lines": [64, 66], "branches": []}
# gained: {"lines": [64, 66], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def hostvars(mock_inventory, mock_variable_manager, mock_loader):
    hv = HostVars(mock_inventory, mock_variable_manager, mock_loader)
    return hv

def test_find_host_existing_host(hostvars, mock_inventory):
    mock_host = MagicMock()
    mock_inventory.get_host.return_value = mock_host
    host_name = "existing_host"
    
    result = hostvars._find_host(host_name)
    
    mock_inventory.get_host.assert_called_once_with(host_name)
    assert result == mock_host

def test_find_host_non_existing_host(hostvars, mock_inventory):
    mock_inventory.get_host.return_value = None
    host_name = "non_existing_host"
    
    result = hostvars._find_host(host_name)
    
    mock_inventory.get_host.assert_called_once_with(host_name)
    assert result is None
