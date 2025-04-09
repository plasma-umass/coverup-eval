# file: lib/ansible/inventory/group.py:280-281
# asked: {"lines": [280, 281], "branches": []}
# gained: {"lines": [280, 281], "branches": []}

import pytest
from ansible.inventory.group import Group

def test_get_vars():
    group = Group(name="test_group")
    group.vars = {"var1": "value1", "var2": "value2"}
    
    vars_copy = group.get_vars()
    
    assert vars_copy == {"var1": "value1", "var2": "value2"}
    assert vars_copy is not group.vars  # Ensure it's a copy, not the same reference

    # Clean up
    del group
