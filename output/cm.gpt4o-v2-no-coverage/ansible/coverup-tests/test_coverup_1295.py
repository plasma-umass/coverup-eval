# file: lib/ansible/inventory/host.py:128-142
# asked: {"lines": [139], "branches": [[138, 139]]}
# gained: {"lines": [139], "branches": [[138, 139]]}

import pytest
from unittest.mock import Mock

from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host(name="test_host")

@pytest.fixture
def group():
    group = Mock()
    group.get_ancestors.return_value = []
    return group

@pytest.fixture
def group_with_ancestors():
    group = Mock()
    ancestor = Mock()
    ancestor.name = "ancestor"
    group.get_ancestors.return_value = [ancestor]
    return group

@pytest.fixture
def group_with_all_ancestor():
    group = Mock()
    ancestor = Mock()
    ancestor.name = "all"
    group.get_ancestors.return_value = [ancestor]
    return group

def test_remove_group_not_in_groups(host, group):
    assert not host.remove_group(group)
    assert group not in host.groups

def test_remove_group_in_groups(host, group):
    host.groups.append(group)
    assert host.remove_group(group)
    assert group not in host.groups

def test_remove_group_with_ancestors(host, group_with_ancestors):
    host.groups.append(group_with_ancestors)
    assert host.remove_group(group_with_ancestors)
    assert group_with_ancestors not in host.groups

def test_remove_group_with_all_ancestor(host, group_with_all_ancestor):
    host.groups.append(group_with_all_ancestor)
    assert host.remove_group(group_with_all_ancestor)
    assert group_with_all_ancestor not in host.groups

def test_remove_group_with_child_ancestor(host, group_with_ancestors):
    child_group = Mock()
    child_group.get_ancestors.return_value = [group_with_ancestors.get_ancestors()[0]]
    host.groups.append(group_with_ancestors)
    host.groups.append(child_group)
    assert host.remove_group(group_with_ancestors)
    assert group_with_ancestors not in host.groups
    assert child_group in host.groups
