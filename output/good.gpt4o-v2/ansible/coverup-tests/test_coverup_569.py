# file: lib/ansible/vars/hostvars.py:118-122
# asked: {"lines": [118, 119, 120, 121, 122], "branches": [[120, 121], [120, 122]]}
# gained: {"lines": [118, 119, 120, 121, 122], "branches": [[120, 121], [120, 122]]}

import pytest
from unittest.mock import MagicMock
from ansible.vars.hostvars import HostVars

def test_hostvars_repr():
    # Mocking the dependencies
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()

    # Creating a HostVars instance
    hostvars = HostVars(inventory, variable_manager, loader)

    # Setting up the mock inventory
    inventory.hosts = ['host1', 'host2']
    hostvars.get = MagicMock(side_effect=lambda host: f"vars_for_{host}")

    # Calling __repr__ and verifying the output
    result = repr(hostvars)
    expected_result = "{'host1': 'vars_for_host1', 'host2': 'vars_for_host2'}"
    assert result == expected_result

    # Clean up
    del hostvars
    del inventory
    del variable_manager
    del loader
