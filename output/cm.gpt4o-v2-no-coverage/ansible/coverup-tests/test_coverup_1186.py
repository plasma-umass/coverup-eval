# file: lib/ansible/inventory/group.py:283-288
# asked: {"lines": [284, 285, 286, 288], "branches": []}
# gained: {"lines": [284, 285, 286, 288], "branches": []}

import pytest
from ansible.inventory.group import Group

def test_set_priority_valid():
    group = Group(name="test_group")
    group.set_priority(10)
    assert group.priority == 10

def test_set_priority_invalid():
    group = Group(name="test_group")
    group.set_priority(None)
    assert group.priority == 1  # Default priority should remain unchanged
