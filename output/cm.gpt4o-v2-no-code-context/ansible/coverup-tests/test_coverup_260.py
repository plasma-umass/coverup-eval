# file: lib/ansible/utils/collection_loader/_collection_finder.py:299-316
# asked: {"lines": [299, 300, 301, 302, 303, 304, 305, 307, 308, 309, 311, 313, 314, 316], "branches": []}
# gained: {"lines": [299, 300, 301, 302, 303, 304, 305, 307, 308, 309, 311, 313, 314, 316], "branches": []}

import pytest
from unittest.mock import patch

# Assuming the class is imported from the module
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def mock_validate_args(mocker):
    return mocker.patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_args')

@pytest.fixture
def mock_get_candidate_paths(mocker):
    return mocker.patch.object(_AnsibleCollectionPkgLoaderBase, '_get_candidate_paths', return_value=['mock_path'])

@pytest.fixture
def mock_get_subpackage_search_paths(mocker):
    return mocker.patch.object(_AnsibleCollectionPkgLoaderBase, '_get_subpackage_search_paths', return_value=['mock_subpackage_path'])

@pytest.fixture
def mock_validate_final(mocker):
    return mocker.patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_final')

def test_ansible_collection_pkg_loader_base_init(mock_validate_args, mock_get_candidate_paths, mock_get_subpackage_search_paths, mock_validate_final):
    fullname = 'ansible_collections.somens'
    path_list = ['path1', 'path2']
    
    loader = _AnsibleCollectionPkgLoaderBase(fullname, path_list)
    
    assert loader._fullname == fullname
    assert loader._redirect_module is None
    assert loader._split_name == fullname.split('.')
    assert loader._rpart_name == fullname.rpartition('.')
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'somens'
    assert loader._source_code_path is None
    assert loader._decoded_source is None
    assert loader._compiled_code is None
    
    mock_validate_args.assert_called_once()
    mock_get_candidate_paths.assert_called_once_with(['path1', 'path2'])
    mock_get_subpackage_search_paths.assert_called_once_with(['mock_path'])
    mock_validate_final.assert_called_once()
