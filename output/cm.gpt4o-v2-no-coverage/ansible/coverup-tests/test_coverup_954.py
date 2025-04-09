# file: lib/ansible/utils/collection_loader/_collection_finder.py:324-325
# asked: {"lines": [324, 325], "branches": []}
# gained: {"lines": [324, 325], "branches": []}

import os
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:
    
    @pytest.fixture
    def loader(self, monkeypatch):
        monkeypatch.setattr(_AnsibleCollectionPkgLoaderBase, "_validate_args", lambda x: None)
        monkeypatch.setattr(_AnsibleCollectionPkgLoaderBase, "_get_subpackage_search_paths", lambda x, y: [])
        monkeypatch.setattr(_AnsibleCollectionPkgLoaderBase, "_validate_final", lambda x: None)
        return _AnsibleCollectionPkgLoaderBase(fullname="ansible_collections.test.module_utils", path_list=["/path/one", "/path/two"])

    def test_get_candidate_paths(self, loader):
        path_list = ["/path/one", "/path/two"]
        expected_paths = [os.path.join(p, "module_utils") for p in path_list]
        candidate_paths = loader._get_candidate_paths(path_list)
        assert candidate_paths == expected_paths

    def test_get_candidate_paths_empty(self, loader):
        path_list = []
        expected_paths = []
        candidate_paths = loader._get_candidate_paths(path_list)
        assert candidate_paths == expected_paths
