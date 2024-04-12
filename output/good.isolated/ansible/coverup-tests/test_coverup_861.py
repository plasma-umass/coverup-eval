# file lib/ansible/inventory/group.py:73-74
# lines [73, 74]
# branches []

import pytest
from ansible.inventory.group import Group

# Mock class to simulate the Group class behavior
class MockGroup(Group):
    def get_name(self):
        return "test_group"

# Test function to cover __repr__ method in Group class
def test_group_repr():
    group = MockGroup()
    assert repr(group) == "test_group", "The __repr__ method should return the group name"
