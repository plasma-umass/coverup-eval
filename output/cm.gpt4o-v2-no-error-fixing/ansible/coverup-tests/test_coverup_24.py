# file: lib/ansible/inventory/group.py:116-153
# asked: {"lines": [116, 130, 131, 132, 133, 134, 135, 136, 138, 139, 140, 142, 143, 144, 145, 146, 148, 149, 151, 152, 153], "branches": [[132, 133], [132, 134], [134, 135], [134, 138], [138, 139], [138, 151], [142, 143], [142, 148], [144, 142], [144, 145], [145, 142], [145, 146], [151, 152], [151, 153]]}
# gained: {"lines": [116, 130, 131, 132, 133, 134, 135, 136, 138, 139, 140, 142, 143, 144, 145, 146, 148, 149, 151, 152, 153], "branches": [[132, 133], [132, 134], [134, 135], [134, 138], [138, 139], [138, 151], [142, 143], [142, 148], [144, 142], [144, 145], [145, 142], [145, 146], [151, 152], [151, 153]]}

import pytest
from ansible.inventory.group import Group

@pytest.fixture
def group_hierarchy():
    # Create a hierarchy of groups
    group_f = Group(name="F")
    group_e = Group(name="E")
    group_d = Group(name="D")
    group_c = Group(name="C")
    group_b = Group(name="B")
    group_a = Group(name="A")

    # Establish relationships
    group_f.parent_groups = [group_d]
    group_d.parent_groups = [group_a, group_b, group_e]
    group_e.parent_groups = [group_b, group_c]
    group_b.parent_groups = [group_a]
    group_c.parent_groups = [group_a]

    return {
        "A": group_a,
        "B": group_b,
        "C": group_c,
        "D": group_d,
        "E": group_e,
        "F": group_f,
    }

def test_walk_relationship_include_self(group_hierarchy):
    group_f = group_hierarchy["F"]
    result = group_f._walk_relationship("parent_groups", include_self=True)
    expected = {group_hierarchy["A"], group_hierarchy["B"], group_hierarchy["C"], group_hierarchy["D"], group_hierarchy["E"], group_hierarchy["F"]}
    assert result == expected

def test_walk_relationship_preserve_ordering(group_hierarchy):
    group_f = group_hierarchy["F"]
    result = group_f._walk_relationship("parent_groups", preserve_ordering=True)
    expected = [group_hierarchy["D"], group_hierarchy["A"], group_hierarchy["B"], group_hierarchy["E"], group_hierarchy["C"]]
    assert result == expected

def test_walk_relationship_include_self_and_preserve_ordering(group_hierarchy):
    group_f = group_hierarchy["F"]
    result = group_f._walk_relationship("parent_groups", include_self=True, preserve_ordering=True)
    expected = [group_hierarchy["F"], group_hierarchy["D"], group_hierarchy["A"], group_hierarchy["B"], group_hierarchy["E"], group_hierarchy["C"]]
    assert result == expected
