# file: lib/ansible/inventory/group.py:283-288
# asked: {"lines": [283, 284, 285, 286, 288], "branches": []}
# gained: {"lines": [283, 284, 285, 286, 288], "branches": []}

import pytest
from ansible.inventory.group import Group

def test_set_priority_with_valid_integer():
    group = Group("test_group")
    group.set_priority(10)
    assert group.priority == 10

def test_set_priority_with_valid_string_integer():
    group = Group("test_group")
    group.set_priority("20")
    assert group.priority == 20

def test_set_priority_with_invalid_type():
    group = Group("test_group")
    group.set_priority(None)
    assert group.priority == 1  # Default value remains unchanged
