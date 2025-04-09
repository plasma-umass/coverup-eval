# file: lib/ansible/inventory/group.py:234-242
# asked: {"lines": [234, 235, 236, 237, 238, 239, 240, 241, 242], "branches": [[236, 237], [236, 242]]}
# gained: {"lines": [234, 235, 236, 237, 238, 239, 240, 241, 242], "branches": [[236, 237], [236, 242]]}

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
    
    def test_remove_host_success(self, group, host):
        group.hosts.append(host)
        group._hosts = [host.name]
        host.remove_group = Mock()
        group.clear_hosts_cache = Mock()
        
        removed = group.remove_host(host)
        
        assert removed is True
        assert host not in group.hosts
        assert host.name not in group._hosts
        host.remove_group.assert_called_once_with(group)
        group.clear_hosts_cache.assert_called_once()
    
    def test_remove_host_not_present(self, group, host):
        host.name = "non_existent_host"
        
        removed = group.remove_host(host)
        
        assert removed is False
