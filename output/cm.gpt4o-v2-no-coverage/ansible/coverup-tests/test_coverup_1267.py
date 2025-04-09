# file: lib/ansible/inventory/group.py:266-278
# asked: {"lines": [273, 274, 275, 276, 277], "branches": [[272, 273], [273, 272], [273, 274], [275, 276], [275, 277]]}
# gained: {"lines": [273, 274, 275, 276, 277], "branches": [[272, 273], [273, 272], [273, 274], [275, 276], [275, 277]]}

import pytest
from unittest.mock import MagicMock

class TestGroup:
    
    @pytest.fixture
    def group(self):
        from ansible.inventory.group import Group
        return Group(name='test_group')
    
    @pytest.fixture
    def host(self):
        Host = MagicMock()
        Host.implicit = False
        return Host
    
    def test_get_hosts_no_descendants(self, group):
        group.get_descendants = MagicMock(return_value=[])
        assert group._get_hosts() == []
    
    def test_get_hosts_with_descendants(self, group, host):
        descendant = MagicMock()
        descendant.hosts = [host]
        group.get_descendants = MagicMock(return_value=[descendant])
        
        hosts = group._get_hosts()
        assert hosts == [host]
    
    def test_get_hosts_with_seen_hosts(self, group, host):
        descendant = MagicMock()
        descendant.hosts = [host, host]
        group.get_descendants = MagicMock(return_value=[descendant])
        
        hosts = group._get_hosts()
        assert hosts == [host]
    
    def test_get_hosts_with_all_group_and_implicit_host(self, group, host):
        group.name = 'all'
        host.implicit = True
        descendant = MagicMock()
        descendant.hosts = [host]
        group.get_descendants = MagicMock(return_value=[descendant])
        
        hosts = group._get_hosts()
        assert hosts == []
    
    def test_get_hosts_with_all_group_and_non_implicit_host(self, group, host):
        group.name = 'all'
        host.implicit = False
        descendant = MagicMock()
        descendant.hosts = [host]
        group.get_descendants = MagicMock(return_value=[descendant])
        
        hosts = group._get_hosts()
        assert hosts == [host]
