# file: lib/ansible/inventory/group.py:280-281
# asked: {"lines": [280, 281], "branches": []}
# gained: {"lines": [280, 281], "branches": []}

import pytest
from ansible.inventory.group import Group

def test_get_vars():
    group = Group(name="test_group")
    group.vars = {"var1": "value1", "var2": "value2"}
    
    result = group.get_vars()
    
    assert result == {"var1": "value1", "var2": "value2"}
    assert result is not group.vars  # Ensure a copy is returned
