# file: lib/ansible/inventory/host.py:128-142
# asked: {"lines": [129, 130, 131, 132, 135, 136, 137, 138, 139, 141, 142], "branches": [[130, 131], [130, 142], [135, 136], [135, 142], [136, 135], [136, 137], [137, 138], [137, 141], [138, 137], [138, 139]]}
# gained: {"lines": [129, 130, 131, 132, 135, 136, 137, 138, 141, 142], "branches": [[130, 131], [130, 142], [135, 136], [135, 142], [136, 135], [136, 137], [137, 138], [137, 141], [138, 137]]}

import pytest
from unittest.mock import Mock

class Group:
    def __init__(self, name):
        self.name = name
        self._ancestors = []

    def get_ancestors(self):
        return self._ancestors

    def add_ancestor(self, ancestor):
        self._ancestors.append(ancestor)

@pytest.fixture
def host():
    from ansible.inventory.host import Host
    return Host(name="test_host")

def test_remove_group_with_ancestors(host):
    group_all = Group(name="all")
    group_parent = Group(name="parent")
    group_child = Group(name="child")

    group_child.add_ancestor(group_parent)
    group_parent.add_ancestor(group_all)

    host.groups = [group_child, group_parent, group_all]

    removed = host.remove_group(group_child)
    assert removed
    assert group_child not in host.groups
    assert group_parent not in host.groups
    assert group_all in host.groups

def test_remove_group_without_ancestors(host):
    group = Group(name="group")
    host.groups = [group]

    removed = host.remove_group(group)
    assert removed
    assert group not in host.groups

def test_remove_group_not_in_groups(host):
    group = Group(name="group")
    host.groups = []

    removed = host.remove_group(group)
    assert not removed
