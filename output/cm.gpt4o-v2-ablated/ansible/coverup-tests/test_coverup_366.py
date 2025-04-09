# file: lib/ansible/utils/collection_loader/_collection_finder.py:910-911
# asked: {"lines": [910, 911], "branches": []}
# gained: {"lines": [910, 911], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _get_collection_role_path

def test_get_collection_role_path(monkeypatch):
    def mock_get_collection_resource_path(name, resource_type, collection_list):
        assert name == "test_role"
        assert resource_type == "role"
        assert collection_list == ["collection1", "collection2"]
        return "/mocked/path/to/role"

    monkeypatch.setattr(
        'ansible.utils.collection_loader._collection_finder._get_collection_resource_path',
        mock_get_collection_resource_path
    )

    result = _get_collection_role_path("test_role", ["collection1", "collection2"])
    assert result == "/mocked/path/to/role"
