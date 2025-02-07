# file: lib/ansible/utils/collection_loader/_collection_finder.py:324-325
# asked: {"lines": [324, 325], "branches": []}
# gained: {"lines": [324, 325], "branches": []}

import os
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:
    
    @pytest.fixture
    def loader(self, monkeypatch):
        # Mock the _validate_args and _validate_final methods to avoid ImportError
        monkeypatch.setattr(_AnsibleCollectionPkgLoaderBase, "_validate_args", lambda x: None)
        monkeypatch.setattr(_AnsibleCollectionPkgLoaderBase, "_validate_final", lambda x: None)
        monkeypatch.setattr(_AnsibleCollectionPkgLoaderBase, "_get_subpackage_search_paths", lambda x, y: [])
        return _AnsibleCollectionPkgLoaderBase('ansible_collections.test', ['path1', 'path2'])

    def test_get_candidate_paths(self, loader):
        path_list = ['path1', 'path2']
        expected = [os.path.join(p, 'test') for p in path_list]
        result = loader._get_candidate_paths(path_list)
        assert result == expected

    def test_get_candidate_paths_empty(self, loader):
        path_list = []
        expected = []
        result = loader._get_candidate_paths(path_list)
        assert result == expected
