# file: lib/ansible/inventory/group.py:155-156
# asked: {"lines": [155, 156], "branches": []}
# gained: {"lines": [155, 156], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.group import Group

class TestGroup:
    @pytest.fixture
    def group(self):
        return Group(name="test_group")

    def test_get_ancestors(self, group, mocker):
        # Mock the _walk_relationship method
        mock_walk_relationship = mocker.patch.object(group, '_walk_relationship', return_value=set(['A', 'B', 'C', 'D', 'E']))

        # Call the get_ancestors method
        ancestors = group.get_ancestors()

        # Assert that _walk_relationship was called with the correct arguments
        mock_walk_relationship.assert_called_once_with('parent_groups')

        # Assert the return value
        assert ancestors == set(['A', 'B', 'C', 'D', 'E'])
