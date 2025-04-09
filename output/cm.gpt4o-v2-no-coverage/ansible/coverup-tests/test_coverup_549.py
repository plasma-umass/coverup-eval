# file: lib/ansible/playbook/role/metadata.py:51-61
# asked: {"lines": [51, 52, 57, 58, 60, 61], "branches": [[57, 58], [57, 60]]}
# gained: {"lines": [51, 52, 57, 58, 60, 61], "branches": [[57, 58], [57, 60]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.role.metadata import RoleMetadata

class MockOwner:
    def get_name(self):
        return "mock_role"

def test_load_with_valid_data(mocker):
    mock_owner = MockOwner()
    data = {"key": "value"}
    
    mock_load_data = mocker.patch.object(RoleMetadata, 'load_data', return_value="mocked_result")
    
    result = RoleMetadata.load(data, mock_owner)
    
    mock_load_data.assert_called_once_with(data, variable_manager=None, loader=None)
    assert result == "mocked_result"

def test_load_with_invalid_data():
    mock_owner = MockOwner()
    data = ["not", "a", "dict"]
    
    with pytest.raises(AnsibleParserError, match="the 'meta/main.yml' for role mock_role is not a dictionary"):
        RoleMetadata.load(data, mock_owner)
