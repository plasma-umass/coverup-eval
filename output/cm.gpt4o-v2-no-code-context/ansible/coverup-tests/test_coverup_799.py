# file: lib/ansible/utils/collection_loader/_collection_finder.py:910-911
# asked: {"lines": [910, 911], "branches": []}
# gained: {"lines": [910, 911], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _get_collection_role_path, _get_collection_resource_path

def test_get_collection_role_path(monkeypatch):
    def mock_get_collection_resource_path(role_name, resource_type, collection_list):
        assert role_name == "test_role"
        assert resource_type == "role"
        assert collection_list == ["test_collection"]
        return "/mocked/path"

    monkeypatch.setattr("ansible.utils.collection_loader._collection_finder._get_collection_resource_path", mock_get_collection_resource_path)
    
    result = _get_collection_role_path("test_role", ["test_collection"])
    assert result == "/mocked/path"
