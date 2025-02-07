# file: lib/ansible/inventory/host.py:115-126
# asked: {"lines": [], "branches": [[119, 118]]}
# gained: {"lines": [], "branches": [[119, 118]]}

import pytest
from unittest.mock import Mock
from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host(name="test_host")

@pytest.fixture
def group():
    group = Mock()
    group.get_ancestors = Mock(return_value=[])
    return group

def test_add_group_with_new_ancestors(host, group):
    ancestor_group = Mock()
    group.get_ancestors.return_value = [ancestor_group]
    
    # Ensure the ancestor group is not in host.groups initially
    assert ancestor_group not in host.groups
    
    # Add the group
    host.add_group(group)
    
    # Check if the ancestor group was added
    assert ancestor_group in host.groups

def test_add_group_with_existing_ancestors(host, group):
    ancestor_group = Mock()
    group.get_ancestors.return_value = [ancestor_group]
    
    # Add the ancestor group initially
    host.groups.append(ancestor_group)
    
    # Ensure the ancestor group is in host.groups initially
    assert ancestor_group in host.groups
    
    # Add the group
    host.add_group(group)
    
    # Check that the ancestor group was not added again
    assert host.groups.count(ancestor_group) == 1

def test_add_group_without_ancestors(host, group):
    # Ensure the group is not in host.groups initially
    assert group not in host.groups
    
    # Add the group
    added = host.add_group(group)
    
    # Check if the group was added
    assert group in host.groups
    assert added

def test_add_group_already_present(host, group):
    # Add the group initially
    host.add_group(group)
    
    # Ensure the group is in host.groups
    assert group in host.groups
    
    # Try to add the group again
    added = host.add_group(group)
    
    # Check that the group was not added again
    assert host.groups.count(group) == 1
    assert not added
