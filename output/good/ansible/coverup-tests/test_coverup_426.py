# file lib/ansible/inventory/group.py:61-71
# lines [61, 63, 64, 65, 66, 67, 68, 69, 70, 71]
# branches []

import pytest
from ansible.inventory.group import Group

# Mock the to_safe_group_name function to ensure it is called
@pytest.fixture
def mock_to_safe_group_name(mocker):
    return mocker.patch('ansible.inventory.group.to_safe_group_name', return_value='safe_name')

# Test function to cover Group.__init__
def test_group_init(mock_to_safe_group_name):
    group_name = 'test_group'
    group = Group(group_name)

    # Assertions to check if the Group object is initialized correctly
    assert group.depth == 0
    assert group.name == 'safe_name'
    assert group.hosts == []
    assert group._hosts is None
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group._hosts_cache is None
    assert group.priority == 1

    # Verify that to_safe_group_name was called with the correct argument
    mock_to_safe_group_name.assert_called_once_with(group_name)
