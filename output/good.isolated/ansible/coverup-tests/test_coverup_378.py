# file lib/ansible/inventory/group.py:224-232
# lines [224, 225, 226, 227, 228, 229, 230, 231, 232]
# branches ['226->227', '226->232']

import pytest
from ansible.inventory.group import Group
from ansible.inventory.host import Host

class TestGroup:
    @pytest.fixture
    def group(self):
        return Group(name='testgroup')

    @pytest.fixture
    def host(self):
        return Host(name='testhost')

    def test_add_host(self, group, host):
        # Test adding a host to the group
        added = group.add_host(host)
        assert added is True
        assert host.name in group._hosts
        assert host in group.hosts

        # Test adding the same host again, should not be added
        added_again = group.add_host(host)
        assert added_again is False
        assert group.hosts.count(host) == 1  # Ensure host is not added twice

    def test_add_host_cleanup(self, group, host, mocker):
        # Mock the clear_hosts_cache method to ensure it's called
        mocker.patch.object(group, 'clear_hosts_cache')

        # Add the host and verify cleanup
        group.add_host(host)
        group.clear_hosts_cache.assert_called_once()
