# file lib/ansible/inventory/group.py:73-74
# lines [73, 74]
# branches []

import pytest
from unittest.mock import patch

# Assuming the Group class is defined in ansible.inventory.group
from ansible.inventory.group import Group

@pytest.fixture
def group_instance():
    return Group()

def test_group_repr(group_instance, mocker):
    # Mock the get_name method to ensure it returns a predictable value
    mock_get_name = mocker.patch.object(Group, 'get_name', return_value='test_group')
    
    # Call the __repr__ method and assert the expected result
    assert repr(group_instance) == 'test_group'
    
    # Ensure the get_name method was called exactly once
    mock_get_name.assert_called_once()
