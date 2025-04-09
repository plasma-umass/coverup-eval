# file: lib/ansible/utils/collection_loader/_collection_finder.py:299-316
# asked: {"lines": [299, 300, 301, 302, 303, 304, 305, 307, 308, 309, 311, 313, 314, 316], "branches": []}
# gained: {"lines": [299, 300, 301, 302, 303, 304, 305, 307, 308, 309, 311, 313, 314, 316], "branches": []}

import pytest
import os
from unittest.mock import patch, MagicMock
from ansible.module_utils.common.text.converters import to_native
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def mock_os_path_isdir():
    with patch('os.path.isdir') as mock_isdir:
        yield mock_isdir

@pytest.fixture
def mock_to_bytes():
    with patch('ansible.module_utils.common.text.converters.to_bytes', side_effect=lambda x: x.encode('utf-8')):
        yield

def test_ansible_collection_pkg_loader_base_init_valid(monkeypatch, mock_os_path_isdir, mock_to_bytes):
    mock_os_path_isdir.return_value = True
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
    assert loader._candidate_paths == [os.path.join(to_native(p), 'test_collection') for p in path_list]
    assert loader._subpackage_search_paths == [os.path.join(to_native(p), 'test_collection') for p in path_list]

def test_ansible_collection_pkg_loader_base_init_invalid():
    fullname = 'invalid_collection.test_collection'
    path_list = ['/fake/path']

    with pytest.raises(ImportError, match='this loader can only load packages from the ansible_collections package'):
        _AnsibleCollectionPkgLoaderBase(fullname, path_list)
