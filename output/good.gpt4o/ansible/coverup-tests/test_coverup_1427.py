# file lib/ansible/inventory/group.py:170-203
# lines [173, 182]
# branches ['172->173', '176->203', '181->182', '197->202']

import pytest
from unittest.mock import MagicMock, patch

# Assuming the Group class and AnsibleError are imported from ansible.inventory.group
from ansible.inventory.group import Group
from ansible.errors import AnsibleError

def test_add_child_group_self():
    group = Group()
    with pytest.raises(Exception, match="can't add group to itself"):
        group.add_child_group(group)

def test_add_child_group_recursive_dependency(mocker):
    group1 = Group()
    group2 = Group()
    
    mocker.patch.object(group1, 'get_ancestors', return_value=set([group2]))
    mocker.patch.object(group2, 'get_ancestors', return_value=set([group1]))
    
    with pytest.raises(AnsibleError, match="creates a recursive dependency loop"):
        group1.add_child_group(group2)

def test_add_child_group_update_depth_and_cache(mocker):
    group1 = Group()
    group2 = Group()
    group1.child_groups = []
    group1.parent_groups = []
    group2.child_groups = []
    group2.parent_groups = []
    group1.depth = 1
    group2.depth = 0
    
    mocker.patch.object(group1, 'get_ancestors', return_value=set())
    mocker.patch.object(group2, 'get_ancestors', return_value=set())
    mocker.patch.object(group2, '_check_children_depth')
    mocker.patch.object(group2, 'get_hosts', return_value=[])
    mocker.patch.object(group1, 'clear_hosts_cache')
    
    added = group1.add_child_group(group2)
    
    assert added
    assert group2 in group1.child_groups
    assert group2.depth == 2
    group2._check_children_depth.assert_called_once()
    group1.clear_hosts_cache.assert_called_once()
