# file lib/ansible/inventory/group.py:161-165
# lines [161, 162, 163, 164, 165]
# branches ['163->164', '163->165']

import pytest
from unittest.mock import MagicMock

# Assuming the Group class is imported from ansible.inventory.group
from ansible.inventory.group import Group

@pytest.fixture
def group():
    group = Group()
    group._hosts = None
    group.hosts = ['host1', 'host2']
    return group

def test_host_names_initialization(group):
    # Access the host_names property to trigger the code
    host_names = group.host_names
    
    # Assert that the _hosts attribute is now set and contains the correct hosts
    assert group._hosts == set(['host1', 'host2'])
    assert host_names == set(['host1', 'host2'])

def test_host_names_cached(group):
    # Access the host_names property to trigger the code
    _ = group.host_names
    
    # Modify the hosts list to ensure the cached value is used
    group.hosts = ['host3']
    
    # Access the host_names property again and check that it hasn't changed
    host_names = group.host_names
    assert host_names == set(['host1', 'host2'])
