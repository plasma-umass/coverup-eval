# file: lib/ansible/utils/collection_loader/_collection_finder.py:299-316
# asked: {"lines": [299, 300, 301, 302, 303, 304, 305, 307, 308, 309, 311, 313, 314, 316], "branches": []}
# gained: {"lines": [299, 300, 301, 302, 303, 304, 305, 307, 308, 309, 311, 313, 314, 316], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.common.text.converters import to_native
import os

from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def mock_to_native():
    with patch('ansible.module_utils.common.text.converters.to_native') as mock:
        yield mock

@pytest.fixture
def mock_isdir():
    with patch('os.path.isdir') as mock:
        yield mock

def test_ansible_collection_pkg_loader_base_init_valid(mock_to_native, mock_isdir):
    mock_to_native.side_effect = lambda x: x
    mock_isdir.side_effect = lambda x: True

    fullname = 'ansible_collections.test_collection'
    path_list = ['/fake/path']

    loader = _AnsibleCollectionPkgLoaderBase(fullname, path_list)

    assert loader._fullname == fullname
    assert loader._redirect_module is None
    assert loader._split_name == fullname.split('.')
    assert loader._rpart_name == fullname.rpartition('.')
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'test_collection'
    assert loader._source_code_path is None
    assert loader._decoded_source is None
    assert loader._compiled_code is None
    assert loader._candidate_paths == ['/fake/path/test_collection']
    assert loader._subpackage_search_paths == ['/fake/path/test_collection']

def test_ansible_collection_pkg_loader_base_init_invalid_package():
    fullname = 'invalid_package.test_collection'
    path_list = ['/fake/path']

    with pytest.raises(ImportError, match='this loader can only load packages from the ansible_collections package'):
        _AnsibleCollectionPkgLoaderBase(fullname, path_list)

def test_get_candidate_paths(mock_to_native):
    mock_to_native.side_effect = lambda x: x
    fullname = 'ansible_collections.test_collection'
    path_list = ['/fake/path']

    loader = _AnsibleCollectionPkgLoaderBase(fullname, path_list)
    candidate_paths = loader._get_candidate_paths(path_list)

    assert candidate_paths == ['/fake/path/test_collection']

def test_get_subpackage_search_paths(mock_isdir):
    mock_isdir.side_effect = lambda x: True
    fullname = 'ansible_collections.test_collection'
    path_list = ['/fake/path']

    loader = _AnsibleCollectionPkgLoaderBase(fullname, path_list)
    subpackage_search_paths = loader._get_subpackage_search_paths(['/fake/path/test_collection'])

    assert subpackage_search_paths == ['/fake/path/test_collection']

def test_validate_final():
    fullname = 'ansible_collections.test_collection'
    path_list = ['/fake/path']

    loader = _AnsibleCollectionPkgLoaderBase(fullname, path_list)
    assert loader._validate_final() is None
