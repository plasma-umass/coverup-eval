# file lib/ansible/inventory/group.py:161-165
# lines [161, 162, 163, 164, 165]
# branches ['163->164', '163->165']

import pytest
from ansible.inventory.group import Group

# Mock class to simulate the behavior of the actual Host class
class MockHost:
    def __init__(self, name):
        self.name = name

# Test function to cover the host_names property
def test_group_host_names_property():
    # Create a Group instance
    group = Group()

    # Set the group's hosts attribute with mock host objects
    mock_hosts = [MockHost('host1'), MockHost('host2')]
    group.hosts = mock_hosts

    # Access the host_names property to trigger the if branch
    host_names_first_access = group.host_names
    assert host_names_first_access == set(mock_hosts), "The host_names property should return a set of hosts"

    # Access the host_names property again to trigger the else branch
    host_names_second_access = group.host_names
    assert host_names_second_access == host_names_first_access, "Subsequent access to host_names should return the same set"

    # Clean up by deleting the group instance
    del group
