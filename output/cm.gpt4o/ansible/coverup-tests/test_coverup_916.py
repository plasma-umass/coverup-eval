# file lib/ansible/utils/collection_loader/_collection_finder.py:328-330
# lines [328, 330]
# branches []

import os
import pytest
from unittest import mock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def mock_os_path_isdir(mocker):
    mock_isdir = mocker.patch('os.path.isdir')
    return mock_isdir

@pytest.fixture
def mock_to_bytes(mocker):
    mock_to_bytes = mocker.patch('ansible.utils.collection_loader._collection_finder.to_bytes', side_effect=lambda x: x)
    return mock_to_bytes

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self):
        pass

def test_get_subpackage_search_paths(mock_os_path_isdir, mock_to_bytes):
    loader = MockAnsibleCollectionPkgLoaderBase()
    candidate_paths = ['/path/one', '/path/two', '/path/three']

    # Mock os.path.isdir to return True for specific paths
    mock_os_path_isdir.side_effect = lambda x: x in ['/path/one', '/path/three']

    result = loader._get_subpackage_search_paths(candidate_paths)

    assert result == ['/path/one', '/path/three']
    mock_to_bytes.assert_any_call('/path/one')
    mock_to_bytes.assert_any_call('/path/two')
    mock_to_bytes.assert_any_call('/path/three')
    assert mock_to_bytes.call_count == 3
    assert mock_os_path_isdir.call_count == 3
