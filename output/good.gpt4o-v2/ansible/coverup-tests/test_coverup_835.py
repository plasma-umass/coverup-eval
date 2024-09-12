# file: lib/ansible/inventory/group.py:73-74
# asked: {"lines": [73, 74], "branches": []}
# gained: {"lines": [73, 74], "branches": []}

import pytest
from ansible.inventory.group import Group

def test_group_repr():
    group_name = "test_group"
    group = Group(name=group_name)
    assert repr(group) == group_name

def test_group_get_name():
    group_name = "test_group"
    group = Group(name=group_name)
    assert group.get_name() == group_name
