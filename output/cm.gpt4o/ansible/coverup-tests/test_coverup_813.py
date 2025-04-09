# file lib/ansible/inventory/group.py:280-281
# lines [280, 281]
# branches []

import pytest
from ansible.inventory.group import Group

@pytest.fixture
def group_with_vars():
    group = Group()
    group.vars = {'key1': 'value1', 'key2': 'value2'}
    return group

def test_get_vars(group_with_vars):
    result = group_with_vars.get_vars()
    assert result == {'key1': 'value1', 'key2': 'value2'}
    assert result is not group_with_vars.vars  # Ensure a copy is returned

def test_get_vars_empty():
    group = Group()
    group.vars = {}
    result = group.get_vars()
    assert result == {}
    assert result is not group.vars  # Ensure a copy is returned
