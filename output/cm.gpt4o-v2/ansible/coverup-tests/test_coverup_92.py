# file: lib/ansible/utils/collection_loader/_collection_finder.py:138-156
# asked: {"lines": [138, 139, 140, 141, 142, 143, 144, 145, 147, 148, 150, 151, 153, 154, 156], "branches": [[141, 142], [141, 153], [143, 144], [143, 150], [144, 145], [144, 147], [147, 143], [147, 148], [153, 154], [153, 156]]}
# gained: {"lines": [138, 139, 140, 141, 142, 143, 144, 145, 147, 148, 150, 151, 153, 154, 156], "branches": [[141, 142], [141, 153], [143, 144], [143, 150], [144, 145], [147, 148], [153, 154], [153, 156]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

@pytest.fixture
def collection_finder():
    return _AnsibleCollectionFinder(paths=['/fake/path'], scan_sys_paths=False)

def test_ansible_collection_path_hook_no_interesting_paths(collection_finder):
    with patch.object(_AnsibleCollectionFinder, '_n_collection_paths', new_callable=MagicMock) as mock_paths, \
         patch('ansible.utils.collection_loader._collection_finder._AnsiblePathHookFinder') as mock_finder:
        
        mock_paths.__iter__.return_value = iter(['/fake/path1', '/fake/path2'])
        collection_finder._ansible_pkg_path = '/fake/pkg/path'
        collection_finder._n_cached_collection_qualified_paths = None
        
        result = collection_finder._ansible_collection_path_hook('/fake/path1/ansible_collections')
        
        assert mock_finder.called
        assert result == mock_finder.return_value

def test_ansible_collection_path_hook_with_interesting_paths(collection_finder):
    with patch('ansible.utils.collection_loader._collection_finder._AnsiblePathHookFinder') as mock_finder:
        
        collection_finder._n_cached_collection_qualified_paths = ['/fake/path1/ansible_collections']
        
        result = collection_finder._ansible_collection_path_hook('/fake/path1/ansible_collections')
        
        assert mock_finder.called
        assert result == mock_finder.return_value

def test_ansible_collection_path_hook_import_error(collection_finder):
    with patch.object(_AnsibleCollectionFinder, '_n_collection_paths', new_callable=MagicMock) as mock_paths:
        
        mock_paths.__iter__.return_value = iter(['/fake/path1', '/fake/path2'])
        collection_finder._ansible_pkg_path = '/fake/pkg/path'
        collection_finder._n_cached_collection_qualified_paths = None
        
        with pytest.raises(ImportError, match='not interested'):
            collection_finder._ansible_collection_path_hook('/unrelated/path')
