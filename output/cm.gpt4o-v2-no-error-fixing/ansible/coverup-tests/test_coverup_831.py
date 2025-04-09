# file: lib/ansible/inventory/helpers.py:25-26
# asked: {"lines": [26], "branches": []}
# gained: {"lines": [26], "branches": []}

import pytest

class Group:
    def __init__(self, name, depth, priority):
        self.name = name
        self.depth = depth
        self.priority = priority

def test_sort_groups():
    from ansible.inventory.helpers import sort_groups

    group1 = Group("group1", 1, 10)
    group2 = Group("group2", 2, 5)
    group3 = Group("group3", 1, 5)
    group4 = Group("group4", 1, 10)

    groups = [group1, group2, group3, group4]
    sorted_groups = sort_groups(groups)

    assert sorted_groups == [group3, group1, group4, group2]
