# file: lib/ansible/inventory/group.py:170-203
# asked: {"lines": [173, 200], "branches": [[172, 173], [176, 203], [197, 202], [199, 200]]}
# gained: {"lines": [173, 200], "branches": [[172, 173], [199, 200]]}

import pytest
from ansible.inventory.group import Group
from ansible.errors import AnsibleError
from unittest.mock import Mock

def test_add_child_group_to_itself():
    group = Group("group1")
    with pytest.raises(Exception, match="can't add group to itself"):
        group.add_child_group(group)

def test_add_child_group_creates_recursive_dependency(mocker):
    group1 = Group("group1")
    group2 = Group("group2")
    mocker.patch.object(group2, 'get_ancestors', return_value={group1})
    mocker.patch.object(group1, 'get_ancestors', return_value={group2})
    
    with pytest.raises(AnsibleError, match="creates a recursive dependency loop"):
        group1.add_child_group(group2)

def test_add_child_group_success(mocker):
    group1 = Group("group1")
    group2 = Group("group2")
    mocker.patch.object(group2, 'get_ancestors', return_value=set())
    mocker.patch.object(group1, 'get_ancestors', return_value=set())
    mocker.patch.object(group2, 'get_hosts', return_value=[])
    
    added = group1.add_child_group(group2)
    
    assert added
    assert group2 in group1.child_groups
    assert group1 in group2.parent_groups
    assert group2.depth == group1.depth + 1

def test_add_child_group_with_hosts(mocker):
    group1 = Group("group1")
    group2 = Group("group2")
    mock_host = Mock()
    mocker.patch.object(group2, 'get_ancestors', return_value=set())
    mocker.patch.object(group1, 'get_ancestors', return_value=set())
    mocker.patch.object(group2, 'get_hosts', return_value=[mock_host])
    
    added = group1.add_child_group(group2)
    
    assert added
    assert group2 in group1.child_groups
    assert group1 in group2.parent_groups
    assert group2.depth == group1.depth + 1
    mock_host.populate_ancestors.assert_called_once()
