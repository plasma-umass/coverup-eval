# file: lib/ansible/playbook/role/metadata.py:51-61
# asked: {"lines": [51, 52, 57, 58, 60, 61], "branches": [[57, 58], [57, 60]]}
# gained: {"lines": [51, 52, 57, 58, 60, 61], "branches": [[57, 58], [57, 60]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.role.metadata import RoleMetadata

class MockOwner:
    def get_name(self):
        return "test_role"

def test_load_with_non_dict_data():
    owner = MockOwner()
    data = ["not", "a", "dict"]
    
    with pytest.raises(AnsibleParserError, match="the 'meta/main.yml' for role test_role is not a dictionary"):
        RoleMetadata.load(data, owner)

def test_load_with_dict_data(mocker):
    owner = MockOwner()
    data = {"key": "value"}
    
    mock_load_data = mocker.patch.object(RoleMetadata, 'load_data', return_value="mocked_metadata")
    
    result = RoleMetadata.load(data, owner)
    
    mock_load_data.assert_called_once_with(data, variable_manager=None, loader=None)
    assert result == "mocked_metadata"
