# file: lib/ansible/vars/hostvars.py:98-99
# asked: {"lines": [99], "branches": []}
# gained: {"lines": [99], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

@pytest.fixture
def hostvars():
    variable_manager = MagicMock()
    inventory = MagicMock()
    loader = MagicMock()
    return HostVars(variable_manager=variable_manager, inventory=inventory, loader=loader)

def test_set_host_variable(hostvars):
    host = 'test_host'
    varname = 'test_var'
    value = 'test_value'
    
    hostvars.set_host_variable(host, varname, value)
    
    hostvars._variable_manager.set_host_variable.assert_called_once_with(host, varname, value)
