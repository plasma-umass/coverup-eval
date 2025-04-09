# file: lib/ansible/inventory/group.py:61-71
# asked: {"lines": [61, 63, 64, 65, 66, 67, 68, 69, 70, 71], "branches": []}
# gained: {"lines": [61, 63, 64, 65, 66, 67, 68, 69, 70, 71], "branches": []}

import pytest
from ansible.inventory.group import Group
from ansible.module_utils._text import to_text

def test_group_init_with_name(mocker):
    mock_to_safe_group_name = mocker.patch('ansible.inventory.group.to_safe_group_name', return_value='safe_name')
    group = Group(name='unsafe_name')
    
    mock_to_safe_group_name.assert_called_once_with('unsafe_name')
    assert group.depth == 0
    assert group.name == 'safe_name'
    assert group.hosts == []
    assert group._hosts is None
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group._hosts_cache is None
    assert group.priority == 1

def test_group_init_without_name(mocker):
    mock_to_safe_group_name = mocker.patch('ansible.inventory.group.to_safe_group_name', return_value=None)
    group = Group()
    
    mock_to_safe_group_name.assert_called_once_with(None)
    assert group.depth == 0
    assert group.name is None
    assert group.hosts == []
    assert group._hosts is None
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group._hosts_cache is None
    assert group.priority == 1
