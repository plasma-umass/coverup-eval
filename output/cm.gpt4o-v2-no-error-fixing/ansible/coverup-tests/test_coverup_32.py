# file: lib/ansible/inventory/group.py:170-203
# asked: {"lines": [170, 171, 172, 173, 176, 179, 180, 181, 182, 183, 184, 186, 187, 190, 193, 197, 198, 199, 200, 202, 203], "branches": [[172, 173], [172, 176], [176, 179], [176, 203], [181, 182], [181, 183], [197, 198], [197, 202], [199, 200], [199, 202]]}
# gained: {"lines": [170, 171, 172, 173, 176, 179, 180, 181, 182, 183, 184, 186, 187, 190, 193, 197, 198, 199, 200, 202, 203], "branches": [[172, 173], [172, 176], [176, 179], [176, 203], [181, 182], [181, 183], [197, 198], [199, 200], [199, 202]]}

import pytest
from unittest.mock import Mock, create_autospec
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.inventory.group import Group

@pytest.fixture
def group():
    return Group()

@pytest.fixture
def child_group():
    return Group()

def test_add_child_group_self(group):
    with pytest.raises(Exception, match="can't add group to itself"):
        group.add_child_group(group)

def test_add_child_group_already_present(group, child_group, mocker):
    group.child_groups = [child_group]
    assert not group.add_child_group(child_group)

def test_add_child_group_recursive_dependency(group, child_group, mocker):
    mocker.patch.object(group, 'get_ancestors', return_value={child_group})
    with pytest.raises(AnsibleError, match="creates a recursive dependency loop"):
        group.add_child_group(child_group)

def test_add_child_group_success(group, child_group, mocker):
    mocker.patch.object(group, 'get_ancestors', return_value=set())
    mocker.patch.object(child_group, 'get_ancestors', return_value=set())
    mocker.patch.object(child_group, '_check_children_depth')
    mocker.patch.object(child_group, 'get_hosts', return_value=[])
    mocker.patch.object(group, 'clear_hosts_cache')

    group.name = "parent"
    child_group.name = "child"
    group.depth = 1
    child_group.depth = 0
    child_group.parent_groups = []

    assert group.add_child_group(child_group)
    assert child_group in group.child_groups
    assert child_group.depth == 2
    child_group._check_children_depth.assert_called_once()
    assert group in child_group.parent_groups
    group.clear_hosts_cache.assert_called_once()

def test_add_child_group_with_hosts(group, child_group, mocker):
    mocker.patch.object(group, 'get_ancestors', return_value=set())
    mocker.patch.object(child_group, 'get_ancestors', return_value=set())
    mocker.patch.object(child_group, '_check_children_depth')
    mocker.patch.object(group, 'clear_hosts_cache')

    mock_host = Mock()
    mocker.patch.object(child_group, 'get_hosts', return_value=[mock_host])
    mocker.patch.object(mock_host, 'populate_ancestors')

    group.name = "parent"
    child_group.name = "child"
    group.depth = 1
    child_group.depth = 0
    child_group.parent_groups = []

    assert group.add_child_group(child_group)
    assert child_group in group.child_groups
    assert child_group.depth == 2
    child_group._check_children_depth.assert_called_once()
    assert group in child_group.parent_groups
    mock_host.populate_ancestors.assert_called_once_with(additions={group})
    group.clear_hosts_cache.assert_called_once()
