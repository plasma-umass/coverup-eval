# file: lib/ansible/utils/collection_loader/_collection_finder.py:485-486
# asked: {"lines": [485, 486], "branches": []}
# gained: {"lines": [485, 486], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def mock_iter_modules_impl():
    with patch('ansible.utils.collection_loader._collection_finder._iter_modules_impl') as mock:
        yield mock

def test_iter_modules(mock_iter_modules_impl):
    # Mock the methods that are not relevant to the test
    with patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_args'), \
         patch.object(_AnsibleCollectionPkgLoaderBase, '_get_candidate_paths', return_value=['/fake/path']), \
         patch.object(_AnsibleCollectionPkgLoaderBase, '_get_subpackage_search_paths', return_value=['/fake/path']), \
         patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_final'):
        
        loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.test.fullname', path_list=['/fake/path'])
        mock_iter_modules_impl.return_value = iter([('prefixmodule1', True), ('prefixmodule2', False)])
        
        result = list(loader.iter_modules('prefix'))
        
        assert result == [('prefixmodule1', True), ('prefixmodule2', False)]
        mock_iter_modules_impl.assert_called_once_with(loader._subpackage_search_paths, 'prefix')
