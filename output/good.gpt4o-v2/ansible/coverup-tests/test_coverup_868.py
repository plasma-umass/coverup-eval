# file: lib/ansible/inventory/group.py:158-159
# asked: {"lines": [158, 159], "branches": []}
# gained: {"lines": [158, 159], "branches": []}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the Group class is defined in ansible/inventory/group.py
from ansible.inventory.group import Group

class TestGroup:
    @pytest.fixture
    def group(self):
        return Group(name="test_group")

    def test_get_descendants(self, group):
        with patch.object(group, '_walk_relationship', return_value=set(['group1', 'group2'])) as mock_walk_relationship:
            # Call get_descendants
            result = group.get_descendants(include_self=True, preserve_ordering=True)

            # Assert _walk_relationship was called with correct arguments
            mock_walk_relationship.assert_called_once_with('child_groups', include_self=True, preserve_ordering=True)

            # Assert the result is as expected
            assert result == set(['group1', 'group2'])
