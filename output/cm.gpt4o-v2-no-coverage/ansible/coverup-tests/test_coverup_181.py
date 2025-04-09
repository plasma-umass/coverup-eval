# file: lib/ansible/inventory/host.py:128-142
# asked: {"lines": [128, 129, 130, 131, 132, 135, 136, 137, 138, 139, 141, 142], "branches": [[130, 131], [130, 142], [135, 136], [135, 142], [136, 135], [136, 137], [137, 138], [137, 141], [138, 137], [138, 139]]}
# gained: {"lines": [128, 129, 130, 131, 132, 135, 136, 137, 138, 141, 142], "branches": [[130, 131], [130, 142], [135, 136], [135, 142], [136, 135], [136, 137], [137, 138], [137, 141], [138, 137]]}

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
    ancestor.get_ancestors.return_value = []
    group.get_ancestors.return_value = [ancestor]
    return group

@pytest.fixture
def group_with_all_ancestor():
    group = Mock()
    ancestor = Mock()
    ancestor.name = "all"
    ancestor.get_ancestors.return_value = []
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
    ancestor = group_with_ancestors.get_ancestors()[0]
    host.groups.append(ancestor)
    assert host.remove_group(group_with_ancestors)
    assert group_with_ancestors not in host.groups
    assert ancestor not in host.groups

def test_remove_group_with_all_ancestor(host, group_with_all_ancestor):
    host.groups.append(group_with_all_ancestor)
    ancestor = group_with_all_ancestor.get_ancestors()[0]
    host.groups.append(ancestor)
    assert host.remove_group(group_with_all_ancestor)
    assert group_with_all_ancestor not in host.groups
    assert ancestor in host.groups
