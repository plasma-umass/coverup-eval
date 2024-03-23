# file lib/ansible/inventory/helpers.py:25-26
# lines [25, 26]
# branches []

import pytest
from ansible.inventory.helpers import sort_groups
from ansible.inventory.group import Group

@pytest.fixture
def create_groups():
    # Create a list of groups with different depths, priorities, and names
    group_a = Group(name='group_a')
    group_a.depth = 1
    group_a.priority = 1

    group_b = Group(name='group_b')
    group_b.depth = 2
    group_b.priority = 1

    group_c = Group(name='group_c')
    group_c.depth = 1
    group_c.priority = 2

    group_d = Group(name='group_d')
    group_d.depth = 1
    group_d.priority = 1

    return [group_b, group_d, group_c, group_a]

def test_sort_groups(create_groups):
    sorted_groups = sort_groups(create_groups)
    # Assert that the groups are sorted by depth, priority, and then name
    assert sorted_groups == [create_groups[3], create_groups[1], create_groups[2], create_groups[0]]
    # Assert that the order is correct according to the sorting key
    assert sorted_groups[0].name == 'group_a'
    assert sorted_groups[1].name == 'group_d'
    assert sorted_groups[2].name == 'group_c'
    assert sorted_groups[3].name == 'group_b'
