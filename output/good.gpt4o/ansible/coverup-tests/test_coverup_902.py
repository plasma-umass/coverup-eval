# file lib/ansible/utils/collection_loader/_collection_finder.py:910-911
# lines [910, 911]
# branches []

import pytest
from unittest.mock import patch

# Assuming the function _get_collection_resource_path is defined in the same module
from ansible.utils.collection_loader._collection_finder import _get_collection_role_path

@patch('ansible.utils.collection_loader._collection_finder._get_collection_resource_path')
def test_get_collection_role_path(mock_get_collection_resource_path):
    role_name = 'test_role'
    collection_list = ['collection1', 'collection2']
    
    # Call the function
    _get_collection_role_path(role_name, collection_list)
    
    # Assert that _get_collection_resource_path was called with the correct arguments
    mock_get_collection_resource_path.assert_called_once_with(role_name, 'role', collection_list)

    # Call the function without collection_list
    _get_collection_role_path(role_name)
    
    # Assert that _get_collection_resource_path was called with the correct arguments
    mock_get_collection_resource_path.assert_called_with(role_name, 'role', None)
