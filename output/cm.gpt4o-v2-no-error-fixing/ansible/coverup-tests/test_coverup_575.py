# file: lib/ansible/inventory/group.py:167-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

import pytest
from ansible.inventory.group import Group

def test_get_name():
    group_name = "test_group"
    group = Group(name=group_name)
    assert group.get_name() == group_name
