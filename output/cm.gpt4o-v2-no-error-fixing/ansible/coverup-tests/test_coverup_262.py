# file: lib/ansible/inventory/group.py:234-242
# asked: {"lines": [234, 235, 236, 237, 238, 239, 240, 241, 242], "branches": [[236, 237], [236, 242]]}
# gained: {"lines": [234, 235, 236, 237, 238, 239, 240, 241, 242], "branches": [[236, 237], [236, 242]]}

import pytest
from unittest.mock import Mock

class TestGroup:
    
    @pytest.fixture
    def group(self):
        from ansible.inventory.group import Group
        group = Group(name="test_group")
        return group

    @pytest.fixture
    def host(self):
        host = Mock()
        host.name = "test_host"
        return host

    def test_remove_host(self, group, host):
        # Setup
        group.hosts.append(host)
        group._hosts = [host.name]
        host.remove_group = Mock()
        group.clear_hosts_cache = Mock()

        # Ensure the host is in the group
        assert host in group.hosts
        assert host.name in group._hosts

        # Execute
        removed = group.remove_host(host)

        # Verify
        assert removed
        assert host not in group.hosts
        assert host.name not in group._hosts
        host.remove_group.assert_called_once_with(group)
        group.clear_hosts_cache.assert_called_once()

    def test_remove_host_not_in_group(self, group, host):
        # Setup
        group._hosts = []

        # Ensure the host is not in the group
        assert host not in group.hosts
        assert host.name not in group._hosts

        # Execute
        removed = group.remove_host(host)

        # Verify
        assert not removed
