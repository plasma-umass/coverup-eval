# file: lib/ansible/inventory/group.py:161-165
# asked: {"lines": [161, 162, 163, 164, 165], "branches": [[163, 164], [163, 165]]}
# gained: {"lines": [161, 162, 163, 164, 165], "branches": [[163, 164], [163, 165]]}

import pytest
from ansible.inventory.group import Group

@pytest.fixture
def group():
    return Group(name="test_group")

def test_host_names_initial_none(group):
    # Ensure _hosts is None initially
    assert group._hosts is None
    
    # Access host_names to trigger the property
    host_names = group.host_names
    
    # Verify _hosts is now a set
    assert isinstance(group._hosts, set)
    assert group._hosts == set(group.hosts)
    assert host_names == group._hosts

def test_host_names_cached(group):
    # Manually set _hosts to a specific value
    group._hosts = {"host1", "host2"}
    
    # Access host_names to trigger the property
    host_names = group.host_names
    
    # Verify _hosts remains unchanged
    assert group._hosts == {"host1", "host2"}
    assert host_names == group._hosts

def test_host_names_with_hosts(group):
    # Add hosts to the group
    group.hosts = ["host1", "host2"]
    
    # Access host_names to trigger the property
    host_names = group.host_names
    
    # Verify _hosts is now a set of the hosts
    assert group._hosts == {"host1", "host2"}
    assert host_names == group._hosts
