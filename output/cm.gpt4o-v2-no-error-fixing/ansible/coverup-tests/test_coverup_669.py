# file: lib/ansible/utils/collection_loader/_collection_finder.py:910-911
# asked: {"lines": [910, 911], "branches": []}
# gained: {"lines": [910, 911], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _get_collection_role_path

@pytest.fixture
def mock_get_collection_resource_path(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._get_collection_resource_path', mock)
    return mock

def test_get_collection_role_path_with_collection_list(mock_get_collection_resource_path):
    role_name = 'test_role'
    collection_list = ['test_collection']
    
    _get_collection_role_path(role_name, collection_list)
    
    mock_get_collection_resource_path.assert_called_once_with(role_name, 'role', collection_list)

def test_get_collection_role_path_without_collection_list(mock_get_collection_resource_path):
    role_name = 'test_role'
    
    _get_collection_role_path(role_name)
    
    mock_get_collection_resource_path.assert_called_once_with(role_name, 'role', None)
