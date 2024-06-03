# file lib/ansible/inventory/group.py:76-77
# lines [76, 77]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the Group class is imported from ansible.inventory.group
from ansible.inventory.group import Group

@pytest.fixture
def group():
    group = Group()
    group.get_name = MagicMock(return_value="test_group")
    return group

def test_group_str_method(group):
    assert str(group) == "test_group"
    group.get_name.assert_called_once()

