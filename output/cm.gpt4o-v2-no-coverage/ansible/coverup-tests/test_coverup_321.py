# file: lib/ansible/inventory/group.py:85-100
# asked: {"lines": [85, 86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 100], "branches": [[87, 88], [87, 90]]}
# gained: {"lines": [85, 86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 100], "branches": [[87, 88], [87, 90]]}

import pytest
from unittest.mock import MagicMock

# Assuming the Group class is defined in ansible/inventory/group.py
from ansible.inventory.group import Group

@pytest.fixture
def group():
    return Group(name="test_group")

def test_serialize_empty_group(group):
    expected_result = {
        "name": "test_group",
        "vars": {},
        "parent_groups": [],
        "depth": 0,
        "hosts": [],
    }
    assert group.serialize() == expected_result

def test_serialize_with_parent_groups(group):
    parent_group = Group(name="parent_group")
    parent_group.serialize = MagicMock(return_value={"name": "parent_group"})
    group.parent_groups.append(parent_group)
    
    expected_result = {
        "name": "test_group",
        "vars": {},
        "parent_groups": [{"name": "parent_group"}],
        "depth": 0,
        "hosts": [],
    }
    assert group.serialize() == expected_result
    parent_group.serialize.assert_called_once()

def test_serialize_with_vars(group):
    group.vars = {"key": "value"}
    
    expected_result = {
        "name": "test_group",
        "vars": {"key": "value"},
        "parent_groups": [],
        "depth": 0,
        "hosts": [],
    }
    assert group.serialize() == expected_result

def test_serialize_with_hosts(group):
    group.hosts = ["host1", "host2"]
    
    expected_result = {
        "name": "test_group",
        "vars": {},
        "parent_groups": [],
        "depth": 0,
        "hosts": ["host1", "host2"],
    }
    assert group.serialize() == expected_result
