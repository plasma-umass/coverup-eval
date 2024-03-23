# file lib/ansible/inventory/group.py:266-278
# lines [266, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278]
# branches ['270->271', '270->278', '272->270', '272->273', '273->272', '273->274', '275->276', '275->277']

import pytest
from ansible.inventory.group import Group
from ansible.inventory.host import Host
from unittest.mock import MagicMock

# Mocking the Host class to add 'implicit' attribute
class MockHost(Host):
    def __init__(self, name, implicit=False):
        super().__init__(name)
        self.implicit = implicit

@pytest.fixture
def setup_group():
    # Setup for Group with 'all' name
    group_all = Group('all')
    group_child = Group('child')
    group_all.add_child_group(group_child)

    # Adding hosts to child group
    host1 = MockHost('host1', implicit=True)
    host2 = MockHost('host2', implicit=False)
    group_child.add_host(host1)
    group_child.add_host(host2)

    # Mocking get_descendants to control the order and content
    group_all.get_descendants = MagicMock(return_value=[group_all, group_child])

    return group_all, host1, host2

def test_get_hosts_excludes_implicit_hosts_in_all_group(setup_group):
    group_all, host1, host2 = setup_group

    # Call the method under test
    hosts = group_all._get_hosts()

    # Assertions to verify the correct hosts are returned
    assert host1 not in hosts, "Implicit host should not be included in 'all' group"
    assert host2 in hosts, "Non-implicit host should be included in 'all' group"
    assert len(hosts) == 1, "Only one non-implicit host should be in the 'all' group"

def test_get_hosts_includes_implicit_hosts_in_non_all_group(setup_group):
    group_all, host1, host2 = setup_group
    group_non_all = Group('non_all')
    group_non_all.add_child_group(group_all)

    # Adding hosts to non_all group
    group_non_all.add_host(host1)
    group_non_all.add_host(host2)

    # Mocking get_descendants to control the order and content
    group_non_all.get_descendants = MagicMock(return_value=[group_non_all, group_all])

    # Call the method under test
    hosts = group_non_all._get_hosts()

    # Assertions to verify the correct hosts are returned
    assert host1 in hosts, "Implicit host should be included in non-'all' group"
    assert host2 in hosts, "Non-implicit host should be included in non-'all' group"
    assert len(hosts) == 2, "Both implicit and non-implicit hosts should be in the non-'all' group"
