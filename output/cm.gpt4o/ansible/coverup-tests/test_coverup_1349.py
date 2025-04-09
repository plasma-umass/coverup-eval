# file lib/ansible/vars/hostvars.py:98-99
# lines [99]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def hostvars(mock_inventory, mock_variable_manager, mock_loader):
    return HostVars(mock_inventory, mock_variable_manager, mock_loader)

def test_set_host_variable(hostvars, mock_variable_manager):
    host = 'test_host'
    varname = 'test_var'
    value = 'test_value'
    
    hostvars.set_host_variable(host, varname, value)
    
    mock_variable_manager.set_host_variable.assert_called_once_with(host, varname, value)
