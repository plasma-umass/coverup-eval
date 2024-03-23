# file lib/ansible/vars/hostvars.py:98-99
# lines [98, 99]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

# Assuming the HostVars class is part of a larger module with necessary imports and context

@pytest.fixture
def hostvars_and_mocks():
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    hostvars = HostVars(inventory, variable_manager, loader)
    host = MagicMock()
    varname = 'test_var'
    value = 'test_value'
    return hostvars, host, varname, value, variable_manager

def test_set_host_variable(hostvars_and_mocks):
    hostvars, host, varname, value, variable_manager = hostvars_and_mocks

    # Call the method we want to test
    hostvars.set_host_variable(host, varname, value)

    # Assert that the variable_manager's set_host_variable was called with the correct arguments
    variable_manager.set_host_variable.assert_called_once_with(host, varname, value)

# No top-level code is included as per instructions
