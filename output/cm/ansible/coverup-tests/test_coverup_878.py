# file lib/ansible/inventory/group.py:155-156
# lines [155, 156]
# branches []

import pytest
from ansible.inventory.group import Group

# Mock class to simulate the behavior of the parent_groups relationship
class MockGroup(Group):
    def __init__(self, name):
        self.name = name
        self.parent_groups = []

    def add_parent_group(self, parent_group):
        self.parent_groups.append(parent_group)

    def _walk_relationship(self, relationship):
        ancestors = []
        for parent in getattr(self, relationship):
            ancestors.append(parent)
            ancestors.extend(parent._walk_relationship(relationship))
        return ancestors

# Test function to check if get_ancestors method is working correctly
def test_get_ancestors():
    # Create groups and establish parent-child relationships
    grandparent_group = MockGroup('grandparent')
    parent_group = MockGroup('parent')
    child_group = MockGroup('child')

    parent_group.add_parent_group(grandparent_group)
    child_group.add_parent_group(parent_group)

    # Get ancestors of the child group
    ancestors = child_group.get_ancestors()

    # Check if the ancestors list is correct
    assert ancestors == [parent_group, grandparent_group], "The ancestors list should contain the parent and grandparent groups"

    # Clean up
    del grandparent_group
    del parent_group
    del child_group
