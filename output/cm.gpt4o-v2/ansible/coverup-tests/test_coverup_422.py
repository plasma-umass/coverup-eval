# file: lib/ansible/inventory/group.py:61-71
# asked: {"lines": [61, 63, 64, 65, 66, 67, 68, 69, 70, 71], "branches": []}
# gained: {"lines": [61, 63, 64, 65, 66, 67, 68, 69, 70, 71], "branches": []}

import pytest
from ansible.inventory.group import Group
from ansible.module_utils._text import to_text

def test_group_initialization_with_name():
    group_name = "test_group"
    group = Group(name=group_name)
    
    assert group.depth == 0
    assert group.name == to_text(group_name)
    assert group.hosts == []
    assert group._hosts is None
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group._hosts_cache is None
    assert group.priority == 1

def test_group_initialization_without_name():
    group = Group()
    
    assert group.depth == 0
    assert group.name is None
    assert group.hosts == []
    assert group._hosts is None
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group._hosts_cache is None
    assert group.priority == 1
