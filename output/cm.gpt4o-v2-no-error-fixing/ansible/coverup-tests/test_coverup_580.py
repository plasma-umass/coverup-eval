# file: lib/ansible/inventory/group.py:155-156
# asked: {"lines": [155, 156], "branches": []}
# gained: {"lines": [155, 156], "branches": []}

import pytest
from ansible.inventory.group import Group

@pytest.fixture
def group_with_parents():
    parent_group = Group(name="parent")
    child_group = Group(name="child")
    child_group.parent_groups.append(parent_group)
    return child_group

def test_get_ancestors(group_with_parents, mocker):
    mock_walk_relationship = mocker.patch.object(Group, '_walk_relationship', return_value=['parent'])
    ancestors = group_with_parents.get_ancestors()
    mock_walk_relationship.assert_called_once_with('parent_groups')
    assert ancestors == ['parent']
