# file: lib/ansible/inventory/group.py:170-203
# asked: {"lines": [], "branches": [[197, 202]]}
# gained: {"lines": [], "branches": [[197, 202]]}

import pytest
from unittest.mock import MagicMock, create_autospec
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.inventory.group import Group

@pytest.fixture
def group():
    g = Group()
    g.name = "group"
    g.child_groups = []
    g.parent_groups = []
    g.depth = 0
    g._hosts_cache = None
    return g

@pytest.fixture
def child_group():
    g = Group()
    g.name = "child_group"
    g.child_groups = []
    g.parent_groups = []
    g.depth = 0
    g._hosts_cache = None
    return g

def test_add_child_group_creates_recursive_dependency(group, child_group):
    group.get_ancestors = MagicMock(return_value=set([child_group]))
    child_group.get_ancestors = MagicMock(return_value=set())
    
    with pytest.raises(AnsibleError, match="creates a recursive dependency loop"):
        group.add_child_group(child_group)

def test_add_child_group_updates_parent_groups(group, child_group):
    group.get_ancestors = MagicMock(return_value=set())
    child_group.get_ancestors = MagicMock(return_value=set())
    child_group.get_hosts = MagicMock(return_value=[])
    group.clear_hosts_cache = MagicMock()
    
    added = group.add_child_group(child_group)
    
    assert added
    assert group in child_group.parent_groups
    group.clear_hosts_cache.assert_called_once()

def test_add_child_group_does_not_duplicate_parent_group(group, child_group):
    group.get_ancestors = MagicMock(return_value=set())
    child_group.get_ancestors = MagicMock(return_value=set())
    child_group.get_hosts = MagicMock(return_value=[])
    group.clear_hosts_cache = MagicMock()
    
    child_group.parent_groups.append(group)
    added = group.add_child_group(child_group)
    
    assert added
    assert len(child_group.parent_groups) == 1
    group.clear_hosts_cache.assert_called_once()
