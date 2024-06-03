# file lib/ansible/inventory/group.py:155-156
# lines [155, 156]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the Group class is part of a module named ansible.inventory.group
from ansible.inventory.group import Group

@pytest.fixture
def mock_group(mocker):
    group = Group()
    mocker.patch.object(group, '_walk_relationship', return_value=['parent1', 'parent2'])
    return group

def test_get_ancestors(mock_group):
    ancestors = mock_group.get_ancestors()
    assert ancestors == ['parent1', 'parent2']
    mock_group._walk_relationship.assert_called_once_with('parent_groups')
