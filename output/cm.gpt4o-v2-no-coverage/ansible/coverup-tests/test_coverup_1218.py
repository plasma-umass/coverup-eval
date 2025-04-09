# file: lib/ansible/inventory/group.py:73-74
# asked: {"lines": [74], "branches": []}
# gained: {"lines": [74], "branches": []}

import pytest
from ansible.inventory.group import Group

@pytest.fixture
def group():
    return Group(name="test_group")

def test_group_repr(group):
    assert repr(group) == "test_group"

def test_group_get_name(group):
    assert group.get_name() == "test_group"
