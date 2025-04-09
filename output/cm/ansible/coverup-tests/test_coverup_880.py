# file lib/ansible/inventory/host.py:150-151
# lines [150, 151]
# branches []

import pytest
from ansible.inventory.host import Host

# Assuming that the Host class is part of a larger module and has dependencies that need to be mocked
# We will use pytest-mock to mock those dependencies if necessary

def test_get_groups():
    # Setup: Create a Host instance and mock its groups attribute
    host = Host()
    mock_groups = ['group1', 'group2', 'group3']
    host.groups = mock_groups

    # Exercise: Call get_groups method
    result = host.get_groups()

    # Verify: Check if the result matches the mocked groups
    assert result == mock_groups, "The get_groups method should return the list of groups"

    # Cleanup: No cleanup is necessary as we are not modifying any external state
