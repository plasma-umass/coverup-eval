# file: lib/ansible/playbook/role/metadata.py:51-61
# asked: {"lines": [51, 52, 57, 58, 60, 61], "branches": [[57, 58], [57, 60]]}
# gained: {"lines": [51, 52, 57, 58, 60, 61], "branches": [[57, 58], [57, 60]]}

import pytest
from ansible.playbook.role.metadata import RoleMetadata
from ansible.errors import AnsibleParserError

class MockOwner:
    def get_name(self):
        return "mock_role"

def test_load_with_valid_data(mocker):
    data = {}
    owner = MockOwner()
    mocker.patch.object(RoleMetadata, '_valid_attrs', new_callable=dict)
    result = RoleMetadata.load(data, owner)
    assert isinstance(result, RoleMetadata)

def test_load_with_invalid_data():
    data = ["not", "a", "dict"]
    owner = MockOwner()
    with pytest.raises(AnsibleParserError, match="the 'meta/main.yml' for role mock_role is not a dictionary"):
        RoleMetadata.load(data, owner)
