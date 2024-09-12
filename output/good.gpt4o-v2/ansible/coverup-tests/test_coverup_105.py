# file: lib/ansible/inventory/group.py:205-222
# asked: {"lines": [205, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222], "branches": [[212, 0], [212, 213], [217, 218], [217, 221], [218, 217], [218, 219], [221, 212], [221, 222]]}
# gained: {"lines": [205, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 221], "branches": [[212, 0], [212, 213], [217, 218], [217, 221], [218, 217], [221, 212]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.inventory.group import Group

@pytest.fixture
def group():
    return Group(name="test_group")

@pytest.fixture
def child_group():
    return Group(name="child_group")

def test_check_children_depth_no_recursion(group, child_group):
    child_group.depth = 1
    group.add_child_group(child_group)
    group._check_children_depth()
    assert child_group.depth == 1

def test_check_children_depth_with_recursion(group, child_group):
    child_group.depth = 1
    group.add_child_group(child_group)
    with pytest.raises(AnsibleError, match="Adding group 'test_group' as child to 'child_group' creates a recursive dependency loop."):
        child_group.add_child_group(group)

def test_check_children_depth_increase_depth(group, child_group):
    child_group.depth = 0
    group.add_child_group(child_group)
    group._check_children_depth()
    assert child_group.depth == 1
