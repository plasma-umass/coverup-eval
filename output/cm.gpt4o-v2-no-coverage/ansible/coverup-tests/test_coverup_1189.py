# file: lib/ansible/utils/collection_loader/_collection_finder.py:451-463
# asked: {"lines": [453, 459], "branches": [[452, 453], [457, 463], [458, 459]]}
# gained: {"lines": [453, 459], "branches": [[452, 453], [457, 463], [458, 459]]}

import pytest
import os
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:
    
    @pytest.fixture
    def loader(self):
        with patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_args'), \
             patch.object(_AnsibleCollectionPkgLoaderBase, '_get_candidate_paths', return_value=[]), \
             patch.object(_AnsibleCollectionPkgLoaderBase, '_get_subpackage_search_paths', return_value=[]), \
             patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_final'):
            return _AnsibleCollectionPkgLoaderBase(fullname='ansible_collections.test.fullname', path_list=['/fake/path'])

    def test_get_filename_fullname_mismatch(self, loader):
        with pytest.raises(ValueError, match="this loader cannot find files for other.fullname, only ansible_collections.test.fullname"):
            loader.get_filename('other.fullname')

    def test_get_filename_source_code_path(self, loader):
        loader._source_code_path = '/fake/source_code_path'
        assert loader.get_filename('ansible_collections.test.fullname') == '/fake/source_code_path'

    def test_get_filename_is_package_single_subpackage_path(self, loader):
        loader._source_code_path = None
        loader.is_package = MagicMock(return_value=True)
        loader._subpackage_search_paths = ['/fake/subpackage_path']
        assert loader.get_filename('ansible_collections.test.fullname') == os.path.join('/fake/subpackage_path', '__synthetic__')

    def test_get_filename_is_package_multiple_subpackage_paths(self, loader):
        loader._source_code_path = None
        loader.is_package = MagicMock(return_value=True)
        loader._subpackage_search_paths = ['/fake/subpackage_path1', '/fake/subpackage_path2']
        loader._synthetic_filename = MagicMock(return_value='/fake/synthetic_filename')
        assert loader.get_filename('ansible_collections.test.fullname') == '/fake/synthetic_filename'
        loader._synthetic_filename.assert_called_once_with('ansible_collections.test.fullname')

    def test_get_filename_not_package(self, loader):
        loader._source_code_path = None
        loader.is_package = MagicMock(return_value=False)
        assert loader.get_filename('ansible_collections.test.fullname') is None
