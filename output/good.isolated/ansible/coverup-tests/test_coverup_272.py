# file lib/ansible/inventory/host.py:115-126
# lines [115, 116, 118, 119, 120, 123, 124, 125, 126]
# branches ['118->119', '118->123', '119->118', '119->120', '123->124', '123->126']

import pytest
from ansible.inventory.host import Host

class GroupMock:
    def __init__(self, name, ancestors=None):
        self.name = name
        self.ancestors = ancestors or []

    def get_ancestors(self):
        return self.ancestors

@pytest.fixture
def host():
    return Host()

def test_add_group_with_ancestors(host):
    # Create mock groups with ancestors
    ancestor_group = GroupMock('ancestor_group')
    group_with_ancestors = GroupMock('group_with_ancestors', [ancestor_group])

    # Add group with ancestors to the host
    added = host.add_group(group_with_ancestors)

    # Assert that the group was added
    assert added == True
    # Assert that the ancestor was added
    assert ancestor_group in host.groups
    # Assert that the group is in the host's groups
    assert group_with_ancestors in host.groups

def test_add_group_without_ancestors(host):
    # Create mock group without ancestors
    group_without_ancestors = GroupMock('group_without_ancestors')

    # Add group without ancestors to the host
    added = host.add_group(group_without_ancestors)

    # Assert that the group was added
    assert added == True
    # Assert that the group is in the host's groups
    assert group_without_ancestors in host.groups

def test_add_existing_group(host):
    # Create mock group
    existing_group = GroupMock('existing_group')

    # Add group for the first time
    host.add_group(existing_group)
    # Try to add the same group again
    added = host.add_group(existing_group)

    # Assert that the group was not added the second time
    assert added == False
    # Assert that the group is still in the host's groups
    assert existing_group in host.groups
    # Assert that the group is only added once
    assert host.groups.count(existing_group) == 1
