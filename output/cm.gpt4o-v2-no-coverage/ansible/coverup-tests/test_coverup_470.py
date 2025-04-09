# file: lib/ansible/inventory/group.py:61-71
# asked: {"lines": [61, 63, 64, 65, 66, 67, 68, 69, 70, 71], "branches": []}
# gained: {"lines": [61, 63, 64, 65, 66, 67, 68, 69, 70, 71], "branches": []}

import pytest
from ansible.inventory.group import Group

def to_safe_group_name(name):
    # Mock implementation of to_safe_group_name
    return name if name else "default"

@pytest.fixture
def mock_to_safe_group_name(monkeypatch):
    monkeypatch.setattr("ansible.inventory.group.to_safe_group_name", to_safe_group_name)

def test_group_init_with_name(mock_to_safe_group_name):
    group = Group(name="test_group")
    assert group.depth == 0
    assert group.name == "test_group"
    assert group.hosts == []
    assert group._hosts is None
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group._hosts_cache is None
    assert group.priority == 1

def test_group_init_without_name(mock_to_safe_group_name):
    group = Group()
    assert group.depth == 0
    assert group.name == "default"
    assert group.hosts == []
    assert group._hosts is None
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group._hosts_cache is None
    assert group.priority == 1
