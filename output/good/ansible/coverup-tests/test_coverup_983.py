# file lib/ansible/utils/collection_loader/_collection_finder.py:910-911
# lines [910, 911]
# branches []

import pytest
from ansible.utils.collection_loader import _collection_finder

# Assuming the existence of the _get_collection_resource_path function
# If it doesn't exist, it should be mocked or implemented accordingly.

@pytest.fixture
def collection_list_cleanup(mocker):
    # Cleanup code to ensure no side effects affect other tests
    mocker.patch.object(_collection_finder, '_get_collection_resource_path', return_value="mocked_path")

def test_get_collection_role_path(collection_list_cleanup):
    role_name = "test_role"
    collection_list = ["test_collection"]
    # Call the function with the role_name and collection_list
    role_path = _collection_finder._get_collection_role_path(role_name, collection_list)
    # Assert that the returned path is what is expected
    assert role_path == "mocked_path"
    # Assert that the mocked _get_collection_resource_path was called with the correct parameters
    _collection_finder._get_collection_resource_path.assert_called_once_with(role_name, 'role', collection_list)
