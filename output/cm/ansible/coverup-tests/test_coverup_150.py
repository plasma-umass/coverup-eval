# file lib/ansible/inventory/host.py:128-142
# lines [128, 129, 130, 131, 132, 135, 136, 137, 138, 139, 141, 142]
# branches ['130->131', '130->142', '135->136', '135->142', '136->135', '136->137', '137->138', '137->141', '138->137', '138->139']

import pytest
from ansible.inventory.host import Host
from ansible.inventory.group import Group

# Mock Group class to control the behavior of get_ancestors method
class MockGroup(Group):
    def __init__(self, name, ancestors=None):
        super().__init__(name)
        self._ancestors = ancestors or []

    def get_ancestors(self):
        return self._ancestors

@pytest.fixture
def host_and_groups(mocker):
    # Create a host and groups for testing
    host = Host(name='testhost')
    group_all = MockGroup(name='all')
    group_ancestors = MockGroup(name='ancestors', ancestors=[group_all])
    group_child = MockGroup(name='child', ancestors=[group_ancestors, group_all])
    group_unrelated = MockGroup(name='unrelated')

    # Add groups to the host
    host.add_group(group_all)
    host.add_group(group_ancestors)
    host.add_group(group_child)
    host.add_group(group_unrelated)

    return host, group_all, group_ancestors, group_child, group_unrelated

def test_remove_group_with_ancestors(host_and_groups):
    host, group_all, group_ancestors, group_child, group_unrelated = host_and_groups

    # Remove group_child and verify that group_ancestors is also removed
    removed = host.remove_group(group_child)
    assert removed is True
    assert group_child not in host.groups
    assert group_ancestors not in host.groups
    assert group_all in host.groups  # 'all' group should not be removed

    # Verify that unrelated group is still present
    assert group_unrelated in host.groups

def test_remove_group_without_ancestors(host_and_groups):
    host, group_all, group_ancestors, group_child, group_unrelated = host_and_groups

    # Remove group_unrelated which has no ancestors
    removed = host.remove_group(group_unrelated)
    assert removed is True
    assert group_unrelated not in host.groups

    # Verify that other groups are still present
    assert group_all in host.groups
    assert group_ancestors in host.groups
    assert group_child in host.groups

def test_remove_group_not_present(host_and_groups):
    host, group_all, group_ancestors, group_child, group_unrelated = host_and_groups

    # Create a new group that is not added to the host
    new_group = MockGroup(name='new_group')

    # Attempt to remove the new group
    removed = host.remove_group(new_group)
    assert removed is False
    assert new_group not in host.groups

    # Verify that other groups are still present
    assert group_all in host.groups
    assert group_ancestors in host.groups
    assert group_child in host.groups
    assert group_unrelated in host.groups
