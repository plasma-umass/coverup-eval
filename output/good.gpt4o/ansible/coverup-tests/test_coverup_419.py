# file lib/ansible/inventory/group.py:61-71
# lines [61, 63, 64, 65, 66, 67, 68, 69, 70, 71]
# branches []

import pytest
from unittest.mock import patch

# Assuming to_safe_group_name is a function that needs to be imported
from ansible.inventory.group import Group, to_safe_group_name

@pytest.fixture
def mock_to_safe_group_name(mocker):
    return mocker.patch('ansible.inventory.group.to_safe_group_name', side_effect=lambda x: f"safe_{x}")

def test_group_initialization(mock_to_safe_group_name):
    group_name = "test_group"
    group = Group(name=group_name)
    
    # Assertions to verify the postconditions
    assert group.depth == 0
    assert group.name == f"safe_{group_name}"
    assert group.hosts == []
    assert group._hosts is None
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group._hosts_cache is None
    assert group.priority == 1

    # Verify that to_safe_group_name was called with the correct argument
    mock_to_safe_group_name.assert_called_once_with(group_name)
