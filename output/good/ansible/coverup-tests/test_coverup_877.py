# file lib/ansible/inventory/group.py:76-77
# lines [76, 77]
# branches []

import pytest
from ansible.inventory.group import Group

class TestGroup:
    def test_group_str(self):
        # Setup
        group_name = "testgroup"
        group = Group()
        group.get_name = lambda: group_name  # Mocking get_name method

        # Exercise
        group_str = str(group)

        # Verify
        assert group_str == group_name

        # Cleanup - nothing to do since we used a simple lambda
