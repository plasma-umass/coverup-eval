# file lib/ansible/inventory/group.py:158-159
# lines [158, 159]
# branches []

import pytest
from ansible.inventory.group import Group

# Assuming the existence of a fixture that provides a mock Group object
@pytest.fixture
def mock_group(mocker):
    group = Group(name='testgroup')
    mocker.patch.object(group, '_walk_relationship', return_value=[])
    return group

def test_get_descendants(mock_group):
    # Call the method we want to test
    descendants = mock_group.get_descendants(depth=4)

    # Assert that the internal method _walk_relationship was called with the correct parameters
    mock_group._walk_relationship.assert_called_once_with('child_groups', depth=4)

    # Assert that the result is what we mocked it to be
    assert descendants == []

    # Clean up is handled by the fixture and pytest-mock, no action needed
