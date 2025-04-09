# file: lib/ansible/inventory/group.py:170-203
# asked: {"lines": [173, 182, 200], "branches": [[172, 173], [176, 203], [181, 182], [197, 202], [199, 200]]}
# gained: {"lines": [173, 182, 200], "branches": [[172, 173], [176, 203], [181, 182], [199, 200]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.inventory.group import Group

class MockHost:
    def populate_ancestors(self, additions):
        pass

@pytest.fixture
def group():
    return Group(name="group")

@pytest.fixture
def child_group():
    return Group(name="child_group")

@pytest.fixture
def mocker(mocker):
    return mocker

def test_add_child_group_self(group):
    with pytest.raises(Exception, match="can't add group to itself"):
        group.add_child_group(group)

def test_add_child_group_already_present(group, child_group, mocker):
    group.child_groups.append(child_group)
    assert not group.add_child_group(child_group)

def test_add_child_group_recursive_dependency(group, child_group, mocker):
    mocker.patch.object(group, 'get_ancestors', return_value={child_group})
    with pytest.raises(AnsibleError, match="creates a recursive dependency loop"):
        group.add_child_group(child_group)

def test_add_child_group_success(group, child_group, mocker):
    mocker.patch.object(group, 'get_ancestors', return_value=set())
    mocker.patch.object(child_group, 'get_ancestors', return_value=set())
    mocker.patch.object(child_group, '_check_children_depth')
    mocker.patch.object(group, 'clear_hosts_cache')
    mocker.patch.object(child_group, 'get_hosts', return_value=[MockHost()])

    assert group.add_child_group(child_group)
    assert child_group in group.child_groups
    assert group in child_group.parent_groups
    group.clear_hosts_cache.assert_called_once()
    child_group._check_children_depth.assert_called_once()

def test_add_child_group_update_depth(group, child_group, mocker):
    mocker.patch.object(group, 'get_ancestors', return_value=set())
    mocker.patch.object(child_group, 'get_ancestors', return_value=set())
    mocker.patch.object(child_group, '_check_children_depth')
    mocker.patch.object(group, 'clear_hosts_cache')
    mocker.patch.object(child_group, 'get_hosts', return_value=[MockHost()])

    child_group.depth = 1
    group.depth = 2
    group.add_child_group(child_group)
    assert child_group.depth == 3
