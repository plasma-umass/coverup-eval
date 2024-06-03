# file lib/ansible/inventory/group.py:266-278
# lines [266, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278]
# branches ['270->271', '270->278', '272->270', '272->273', '273->272', '273->274', '275->276', '275->277']

import pytest
from unittest.mock import MagicMock

# Assuming the Group class is defined in ansible.inventory.group
from ansible.inventory.group import Group

class TestGroup:
    @pytest.fixture
    def group(self, mocker):
        group = Group()
        group.name = 'all'
        group.get_descendants = mocker.MagicMock()
        return group

    def test_get_hosts(self, group, mocker):
        # Mocking the descendants and hosts
        descendant1 = mocker.MagicMock()
        descendant2 = mocker.MagicMock()
        host1 = mocker.MagicMock()
        host2 = mocker.MagicMock()
        host3 = mocker.MagicMock()
        
        host1.implicit = False
        host2.implicit = True
        host3.implicit = False
        
        descendant1.hosts = [host1, host2]
        descendant2.hosts = [host2, host3]
        
        group.get_descendants.return_value = [descendant1, descendant2]
        
        # Call the method
        hosts = group._get_hosts()
        
        # Assertions
        assert host1 in hosts
        assert host2 not in hosts  # because it is implicit and group name is 'all'
        assert host3 in hosts
        assert len(hosts) == 2  # only host1 and host3 should be in the list
