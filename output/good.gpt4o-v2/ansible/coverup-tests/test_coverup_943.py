# file: lib/ansible/utils/collection_loader/_collection_finder.py:910-911
# asked: {"lines": [910, 911], "branches": []}
# gained: {"lines": [910, 911], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _get_collection_role_path, _get_collection_resource_path

@pytest.fixture
def mock_get_collection_resource_path(monkeypatch):
    mock = MagicMock(return_value="mocked_path")
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._get_collection_resource_path', mock)
    return mock

def test_get_collection_role_path_with_collection_list(mock_get_collection_resource_path):
    role_name = "test_role"
    collection_list = ["test_collection"]
    
    result = _get_collection_role_path(role_name, collection_list)
    
    mock_get_collection_resource_path.assert_called_once_with(role_name, u'role', collection_list)
    assert result == "mocked_path"

def test_get_collection_role_path_without_collection_list(mock_get_collection_resource_path):
    role_name = "test_role"
    
    result = _get_collection_role_path(role_name)
    
    mock_get_collection_resource_path.assert_called_once_with(role_name, u'role', None)
    assert result == "mocked_path"
