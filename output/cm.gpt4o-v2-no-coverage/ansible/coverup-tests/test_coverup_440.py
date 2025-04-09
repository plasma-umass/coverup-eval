# file: lib/ansible/inventory/group.py:224-232
# asked: {"lines": [224, 225, 226, 227, 228, 229, 230, 231, 232], "branches": [[226, 227], [226, 232]]}
# gained: {"lines": [224, 225, 226, 227, 228, 229, 230, 231, 232], "branches": [[226, 227], [226, 232]]}

import pytest
from unittest.mock import Mock

class TestGroup:
    @pytest.fixture
    def group(self):
        from ansible.inventory.group import Group
        return Group(name="test_group")

    @pytest.fixture
    def host(self):
        host = Mock()
        host.name = "test_host"
        return host

    def test_add_host_not_in_group(self, group, host):
        host.add_group = Mock()
        group.clear_hosts_cache = Mock()
        group._hosts = set()

        added = group.add_host(host)

        assert added is True
        assert host in group.hosts
        assert host.name in group._hosts
        host.add_group.assert_called_once_with(group)
        group.clear_hosts_cache.assert_called_once()

    def test_add_host_already_in_group(self, group, host):
        host.add_group = Mock()
        group.clear_hosts_cache = Mock()
        group._hosts = {host.name}

        added = group.add_host(host)

        assert added is False
        assert host not in group.hosts
        host.add_group.assert_not_called()
        group.clear_hosts_cache.assert_not_called()
