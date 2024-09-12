# file: lib/ansible/vars/hostvars.py:98-99
# asked: {"lines": [98, 99], "branches": []}
# gained: {"lines": [98, 99], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def mock_variable_manager():
    return Mock()

@pytest.fixture
def hostvars(mock_variable_manager):
    inventory = Mock()
    loader = Mock()
    return HostVars(inventory, mock_variable_manager, loader)

def test_set_host_variable(hostvars, mock_variable_manager):
    host = 'test_host'
    varname = 'test_var'
    value = 'test_value'
    
    hostvars.set_host_variable(host, varname, value)
    
    mock_variable_manager.set_host_variable.assert_called_once_with(host, varname, value)
