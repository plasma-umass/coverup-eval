# file lib/ansible/inventory/group.py:82-83
# lines [82, 83]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the Group class is imported from ansible.inventory.group
from ansible.inventory.group import Group

@pytest.fixture
def mock_deserialize(mocker):
    return mocker.patch.object(Group, 'deserialize', return_value=None)

def test_group_setstate(mock_deserialize):
    group = Group()
    data = {'some': 'data'}
    
    group.__setstate__(data)
    
    mock_deserialize.assert_called_once_with(data)
