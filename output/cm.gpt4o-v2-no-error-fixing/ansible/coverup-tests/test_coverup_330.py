# file: lib/ansible/playbook/role/metadata.py:51-61
# asked: {"lines": [51, 52, 57, 58, 60, 61], "branches": [[57, 58], [57, 60]]}
# gained: {"lines": [51, 52, 57, 58, 60, 61], "branches": [[57, 58], [57, 60]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.role.metadata import RoleMetadata

class MockOwner:
    def get_name(self):
        return "mock_role"

def test_load_with_non_dict_data():
    with pytest.raises(AnsibleParserError, match="the 'meta/main.yml' for role mock_role is not a dictionary"):
        RoleMetadata.load(data="not_a_dict", owner=MockOwner())

def test_load_with_dict_data(monkeypatch):
    mock_data = {"key": "value"}
    mock_owner = MockOwner()

    def mock_load_data(self, data, variable_manager=None, loader=None):
        assert data == mock_data
        assert variable_manager is None
        assert loader is None
        return "mock_metadata"

    monkeypatch.setattr(RoleMetadata, "load_data", mock_load_data)

    result = RoleMetadata.load(data=mock_data, owner=mock_owner)
    assert result == "mock_metadata"
