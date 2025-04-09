# file lib/ansible/vars/hostvars.py:124-128
# lines [124, 128]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars
from copy import deepcopy

# Assuming the HostVars class is part of a larger file, we only need to test the __deepcopy__ method.

def test_hostvars_deepcopy():
    # Mock the required arguments for HostVars
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()

    # Create an instance of the HostVars class with mocked arguments
    host_vars_instance = HostVars(inventory, variable_manager, loader)

    # Perform a deepcopy on the instance
    host_vars_copy = deepcopy(host_vars_instance)

    # Assert that the deepcopy returns the same instance (since it's supposed to be immutable)
    assert host_vars_copy is host_vars_instance

    # Clean up is not necessary in this case, as we are not modifying any shared state
