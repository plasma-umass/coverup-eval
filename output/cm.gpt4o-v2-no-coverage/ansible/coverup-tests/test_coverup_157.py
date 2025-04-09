# file: lib/ansible/utils/collection_loader/_collection_finder.py:138-156
# asked: {"lines": [138, 139, 140, 141, 142, 143, 144, 145, 147, 148, 150, 151, 153, 154, 156], "branches": [[141, 142], [141, 153], [143, 144], [143, 150], [144, 145], [144, 147], [147, 143], [147, 148], [153, 154], [153, 156]]}
# gained: {"lines": [138, 139, 140, 141, 142, 143, 144, 145, 147, 148, 150, 151, 153, 154, 156], "branches": [[141, 142], [141, 153], [143, 144], [143, 150], [144, 145], [147, 148], [153, 154], [153, 156]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.common.text.converters import to_native
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder, _AnsiblePathHookFinder

@pytest.fixture
def collection_finder():
    finder = _AnsibleCollectionFinder(paths=['/mock/path'])
    finder._n_cached_collection_qualified_paths = None
    finder._ansible_pkg_path = '/mock/ansible_pkg_path'
    return finder

def test_ansible_collection_path_hook_no_cached_paths(collection_finder):
    collection_finder._n_playbook_paths = ['/mock/path1', '/mock/path2']
    collection_finder._n_configured_paths = []
    with patch('os.path.basename', side_effect=lambda p: 'ansible_collections' if 'collections' in p else 'other'), \
         patch('os.path.join', side_effect=lambda *args: '/'.join(args)):
        result = collection_finder._ansible_collection_path_hook('/mock/path1/ansible_collections')
        assert isinstance(result, _AnsiblePathHookFinder)
        assert result._pathctx == '/mock/path1/ansible_collections'

def test_ansible_collection_path_hook_with_cached_paths(collection_finder):
    collection_finder._n_cached_collection_qualified_paths = ['/mock/path1/ansible_collections']
    result = collection_finder._ansible_collection_path_hook('/mock/path1/ansible_collections')
    assert isinstance(result, _AnsiblePathHookFinder)
    assert result._pathctx == '/mock/path1/ansible_collections'

def test_ansible_collection_path_hook_import_error(collection_finder):
    collection_finder._n_playbook_paths = ['/mock/path1', '/mock/path2']
    collection_finder._n_configured_paths = []
    with patch('os.path.basename', side_effect=lambda p: 'ansible_collections' if 'collections' in p else 'other'), \
         patch('os.path.join', side_effect=lambda *args: '/'.join(args)):
        with pytest.raises(ImportError, match='not interested'):
            collection_finder._ansible_collection_path_hook('/uninteresting/path')
