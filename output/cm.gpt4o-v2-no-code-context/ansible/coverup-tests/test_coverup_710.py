# file: lib/ansible/inventory/helpers.py:25-26
# asked: {"lines": [25, 26], "branches": []}
# gained: {"lines": [25, 26], "branches": []}

import pytest
from ansible.inventory.helpers import sort_groups

class Group:
    def __init__(self, depth, priority, name):
        self.depth = depth
        self.priority = priority
        self.name = name

def test_sort_groups():
    group1 = Group(depth=1, priority=2, name='group1')
    group2 = Group(depth=1, priority=1, name='group2')
    group3 = Group(depth=2, priority=1, name='group3')
    group4 = Group(depth=1, priority=1, name='group4')

    groups = [group1, group2, group3, group4]
    sorted_groups = sort_groups(groups)

    assert sorted_groups == [group2, group4, group1, group3]
