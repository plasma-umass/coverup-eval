# file lib/ansible/inventory/helpers.py:25-26
# lines [25, 26]
# branches []

import pytest
from ansible.inventory.helpers import sort_groups

class Group:
    def __init__(self, name, depth, priority):
        self.name = name
        self.depth = depth
        self.priority = priority

def test_sort_groups():
    group1 = Group(name="group1", depth=1, priority=10)
    group2 = Group(name="group2", depth=2, priority=5)
    group3 = Group(name="group3", depth=1, priority=5)
    group4 = Group(name="group4", depth=1, priority=5)
    
    groups = [group1, group2, group3, group4]
    sorted_groups = sort_groups(groups)
    
    assert sorted_groups == [group3, group4, group1, group2]
    assert sorted_groups[0].name == "group3"
    assert sorted_groups[1].name == "group4"
    assert sorted_groups[2].name == "group1"
    assert sorted_groups[3].name == "group2"
