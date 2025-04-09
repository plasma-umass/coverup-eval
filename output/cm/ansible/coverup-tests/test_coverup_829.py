# file lib/ansible/vars/hostvars.py:57-59
# lines [57, 58, 59]
# branches []

import pytest
from ansible.vars.hostvars import HostVars
from unittest.mock import MagicMock

# Assuming the existence of a VariableManager class, we can mock it
class MockVariableManager:
    _hostvars = None

@pytest.fixture
def variable_manager():
    return MockVariableManager()

@pytest.fixture
def host_vars(variable_manager):
    inventory = MagicMock()
    loader = MagicMock()
    # Create a HostVars instance with the mocked dependencies
    hv = HostVars(inventory=inventory, variable_manager=variable_manager, loader=loader)
    # Remove the _variable_manager attribute to simulate the initial state
    del hv._variable_manager
    return hv

def test_set_variable_manager(host_vars, variable_manager):
    # Ensure that _variable_manager is not set before the method call
    assert not hasattr(host_vars, '_variable_manager')
    
    # Call the method that needs to be tested
    host_vars.set_variable_manager(variable_manager)
    
    # Check postconditions
    assert host_vars._variable_manager is variable_manager
    assert variable_manager._hostvars is host_vars

# Clean up is handled by pytest fixtures, no additional cleanup is necessary.
