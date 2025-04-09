# file: lib/ansible/inventory/group.py:161-165
# asked: {"lines": [161, 162, 163, 164, 165], "branches": [[163, 164], [163, 165]]}
# gained: {"lines": [161, 162, 163, 164, 165], "branches": [[163, 164], [163, 165]]}

import pytest
from ansible.inventory.group import Group

@pytest.fixture
def group():
    return Group(name="test_group")

def test_host_names_initial_none(group):
    # Ensure _hosts is initially None
    assert group._hosts is None
    
    # Access host_names to trigger the property
    host_names = group.host_names
    
    # Verify _hosts is now set to an empty set
    assert host_names == set()
    assert group._hosts == set()

def test_host_names_not_none(group):
    # Manually set _hosts to a specific value
    group._hosts = {"host1", "host2"}
    
    # Access host_names to trigger the property
    host_names = group.host_names
    
    # Verify _hosts remains unchanged
    assert host_names == {"host1", "host2"}
    assert group._hosts == {"host1", "host2"}

def test_host_names_with_hosts(group):
    # Add hosts to the group
    group.hosts = ["host1", "host2"]
    
    # Access host_names to trigger the property
    host_names = group.host_names
    
    # Verify _hosts is now set to the hosts in the group
    assert host_names == {"host1", "host2"}
    assert group._hosts == {"host1", "host2"}
