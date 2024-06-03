# file lib/ansible/inventory/group.py:260-264
# lines [260, 262, 263, 264]
# branches ['262->263', '262->264']

import pytest
from unittest.mock import MagicMock

# Assuming the Group class is imported from ansible.inventory.group
from ansible.inventory.group import Group

@pytest.fixture
def group():
    group = Group()
    group._hosts_cache = None
    group._get_hosts = MagicMock(return_value=['host1', 'host2'])
    return group

def test_get_hosts_cache_none(group):
    # Ensure _hosts_cache is None initially
    assert group._hosts_cache is None
    
    # Call get_hosts and check if _get_hosts was called and cache is set
    hosts = group.get_hosts()
    group._get_hosts.assert_called_once()
    assert hosts == ['host1', 'host2']
    assert group._hosts_cache == ['host1', 'host2']

def test_get_hosts_cache_not_none(group):
    # Set _hosts_cache to a non-None value
    group._hosts_cache = ['cached_host1', 'cached_host2']
    
    # Call get_hosts and check if _get_hosts was not called and cache is returned
    hosts = group.get_hosts()
    group._get_hosts.assert_not_called()
    assert hosts == ['cached_host1', 'cached_host2']
