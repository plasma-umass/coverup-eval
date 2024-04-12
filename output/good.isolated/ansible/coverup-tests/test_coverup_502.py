# file lib/ansible/playbook/role/metadata.py:51-61
# lines [51, 52, 57, 58, 60, 61]
# branches ['57->58', '57->60']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.role.metadata import RoleMetadata
from unittest.mock import MagicMock, patch

# Assuming the existence of a Role class with a get_name method
class MockRole:
    def get_name(self):
        return "test_role"

@pytest.fixture
def mock_owner():
    return MockRole()

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def mock_loader():
    return MagicMock()

def test_role_metadata_load_with_invalid_data_type(mock_owner, mock_variable_manager, mock_loader):
    invalid_data = "not_a_dict"

    with pytest.raises(AnsibleParserError) as excinfo:
        RoleMetadata.load(invalid_data, mock_owner, mock_variable_manager, mock_loader)

    assert "the 'meta/main.yml' for role test_role is not a dictionary" in str(excinfo.value)

def test_role_metadata_load_with_valid_data(mock_owner, mock_variable_manager, mock_loader):
    valid_data = {"some_key": "some_value"}

    # Mocking load_data method to avoid side effects
    with patch.object(RoleMetadata, 'load_data', return_value=RoleMetadata(owner=mock_owner)) as mock_load_data:
        metadata = RoleMetadata.load(valid_data, mock_owner, mock_variable_manager, mock_loader)

    assert isinstance(metadata, RoleMetadata)
    mock_load_data.assert_called_once_with(valid_data, variable_manager=mock_variable_manager, loader=mock_loader)
