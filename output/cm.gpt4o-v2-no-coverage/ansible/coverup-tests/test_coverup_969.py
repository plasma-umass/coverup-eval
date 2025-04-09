# file: lib/ansible/utils/collection_loader/_collection_finder.py:485-486
# asked: {"lines": [485, 486], "branches": []}
# gained: {"lines": [485, 486], "branches": []}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase, _iter_modules_impl

class TestAnsibleCollectionPkgLoaderBase:
    
    @pytest.fixture
    def loader(self):
        with patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_args', lambda x: None):
            loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test.fullname', path_list=['/fake/path'])
            loader._subpackage_search_paths = ['/fake/path']
            return loader

    @patch('ansible.utils.collection_loader._collection_finder._iter_modules_impl')
    def test_iter_modules(self, mock_iter_modules_impl, loader):
        mock_iter_modules_impl.return_value = iter([('module1', True), ('module2', False)])
        result = list(loader.iter_modules('prefix'))
        assert result == [('module1', True), ('module2', False)]
        mock_iter_modules_impl.assert_called_once_with(loader._subpackage_search_paths, 'prefix')

class TestIterModulesImpl:

    @patch('os.path.isdir')
    @patch('os.listdir')
    def test_iter_modules_impl(self, mock_listdir, mock_isdir):
        mock_isdir.side_effect = lambda x: x in [b'/fake/path', b'/fake/path/dir1']
        mock_listdir.return_value = [b'dir1', b'module1.py', b'__init__.py', b'__pycache__', b'invalid.module']
        
        result = list(_iter_modules_impl(['/fake/path'], 'prefix.'))
        
        assert result == [('prefix.dir1', True), ('prefix.module1', False)]
        mock_isdir.assert_any_call(b'/fake/path')
        mock_isdir.assert_any_call(b'/fake/path/dir1')
        mock_listdir.assert_called_once_with(b'/fake/path')
