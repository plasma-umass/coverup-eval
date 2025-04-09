# file: lib/ansible/inventory/group.py:76-77
# asked: {"lines": [76, 77], "branches": []}
# gained: {"lines": [76, 77], "branches": []}

import pytest
from ansible.inventory.group import Group

def test_group_str_method():
    group_name = "test_group"
    group = Group(name=group_name)
    
    assert str(group) == group_name

