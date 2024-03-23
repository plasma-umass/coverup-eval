# file lib/ansible/inventory/group.py:170-203
# lines [170, 171, 172, 173, 176, 179, 180, 181, 182, 183, 184, 186, 187, 190, 193, 197, 198, 199, 200, 202, 203]
# branches ['172->173', '172->176', '176->179', '176->203', '181->182', '181->183', '197->198', '197->202', '199->200', '199->202']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.group import Group
from ansible.inventory.host import Host

class MockGroup(Group):
    def __init__(self, name):
        super(MockGroup, self).__init__(name)
        self.child_groups = []
        self.parent_groups = []
        self.depth = 0

    def _check_children_depth(self):
        pass

    def get_ancestors(self):
        return set(self.parent_groups)

    def add_host(self, host):
        if host not in self.hosts:
            self.hosts.append(host)
            host.add_group(self)

def test_add_child_group_raises_exception_on_self_addition():
    group = MockGroup(name='testgroup')
    with pytest.raises(Exception) as excinfo:
        group.add_child_group(group)
    assert "can't add group to itself" in str(excinfo.value)

def test_add_child_group_raises_exception_on_circular_dependency():
    parent = MockGroup(name='parent')
    child = MockGroup(name='child')
    parent.add_child_group(child)
    with pytest.raises(AnsibleError) as excinfo:
        child.add_child_group(parent)
    assert "creates a recursive dependency loop" in str(excinfo.value)

def test_add_child_group_adds_group_correctly():
    parent = MockGroup(name='parent')
    child = MockGroup(name='child')
    host = Host(name='host1')
    child.add_host(host)
    added = parent.add_child_group(child)
    assert added is True
    assert child in parent.child_groups
    assert parent in child.parent_groups
    assert host in child.hosts
    assert parent in host.get_groups()
    assert child.depth == parent.depth + 1

def test_add_child_group_does_not_add_duplicate():
    parent = MockGroup(name='parent')
    child = MockGroup(name='child')
    parent.add_child_group(child)
    added_again = parent.add_child_group(child)
    assert added_again is False
    assert parent.child_groups.count(child) == 1

def test_add_child_group_does_not_duplicate_parent_with_same_name():
    parent1 = MockGroup(name='parent')
    parent2 = MockGroup(name='parent')
    child = MockGroup(name='child')
    parent1.add_child_group(child)
    parent2.add_child_group(child)
    assert child.parent_groups == [parent1]
    assert parent2 not in child.parent_groups
