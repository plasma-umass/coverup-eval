# file lib/ansible/playbook/role/metadata.py:51-61
# lines [51, 52, 57, 58, 60, 61]
# branches ['57->58', '57->60']

import pytest
from ansible.playbook.role.metadata import RoleMetadata
from ansible.errors import AnsibleParserError
from unittest.mock import Mock

def test_role_metadata_load_with_invalid_data():
    owner_mock = Mock()
    owner_mock.get_name.return_value = 'test_role'
    
    with pytest.raises(AnsibleParserError) as excinfo:
        RoleMetadata.load("invalid_data", owner_mock)
    
    assert str(excinfo.value) == "the 'meta/main.yml' for role test_role is not a dictionary"

def test_role_metadata_load_with_valid_data(mocker):
    owner_mock = Mock()
    owner_mock.get_name.return_value = 'test_role'
    data = {'key': 'value'}
    
    mock_load_data = mocker.patch.object(RoleMetadata, 'load_data', return_value='loaded_metadata')
    
    result = RoleMetadata.load(data, owner_mock)
    
    mock_load_data.assert_called_once_with(data, variable_manager=None, loader=None)
    assert result == 'loaded_metadata'
