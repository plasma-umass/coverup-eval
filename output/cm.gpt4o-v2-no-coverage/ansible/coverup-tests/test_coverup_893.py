# file: lib/ansible/inventory/group.py:158-159
# asked: {"lines": [158, 159], "branches": []}
# gained: {"lines": [158, 159], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.group import Group

@pytest.fixture
def group(mocker):
    mock_to_safe_group_name = mocker.patch('ansible.inventory.group.to_safe_group_name', return_value="test_group")
    return Group(name="test_group")

def test_get_descendants(group, mocker):
    mock_walk_relationship = mocker.patch.object(group, '_walk_relationship', return_value="descendants")
    result = group.get_descendants(include_self=True)
    mock_walk_relationship.assert_called_once_with('child_groups', include_self=True)
    assert result == "descendants"
