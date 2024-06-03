# file lib/ansible/inventory/group.py:85-100
# lines [86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 100]
# branches ['87->88', '87->90']

import pytest
from unittest.mock import MagicMock

# Assuming the Group class is defined in ansible.inventory.group
from ansible.inventory.group import Group

@pytest.fixture
def mock_group():
    group = Group()
    group.name = "test_group"
    group.vars = {"var1": "value1"}
    group.depth = 1
    group.hosts = ["host1", "host2"]
    group.parent_groups = []
    return group

def test_serialize_with_parent_groups(mock_group):
    # Mocking a parent group
    parent_group = MagicMock()
    parent_group.serialize.return_value = {"name": "parent_group"}
    mock_group.parent_groups.append(parent_group)

    result = mock_group.serialize()

    assert result["name"] == "test_group"
    assert result["vars"] == {"var1": "value1"}
    assert result["depth"] == 1
    assert result["hosts"] == ["host1", "host2"]
    assert result["parent_groups"] == [{"name": "parent_group"}]

    # Ensure _hosts is set to None
    assert mock_group._hosts is None

    # Clean up
    mock_group.parent_groups = []

def test_serialize_without_parent_groups(mock_group):
    result = mock_group.serialize()

    assert result["name"] == "test_group"
    assert result["vars"] == {"var1": "value1"}
    assert result["depth"] == 1
    assert result["hosts"] == ["host1", "host2"]
    assert result["parent_groups"] == []

    # Ensure _hosts is set to None
    assert mock_group._hosts is None
