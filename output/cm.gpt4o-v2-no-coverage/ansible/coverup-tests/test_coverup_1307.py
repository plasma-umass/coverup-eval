# file: lib/ansible/utils/collection_loader/_collection_finder.py:599-603
# asked: {"lines": [601], "branches": [[600, 601]]}
# gained: {"lines": [601], "branches": [[600, 601]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionLoader

class MockAnsibleCollectionPkgLoaderBase:
    def __init__(self, fullname, path_list=None):
        self._fullname = fullname
        self._split_name = fullname.split('.')
        self._rpart_name = fullname.rpartition('.')
        self._parent_package_name = self._rpart_name[0]
        self._package_to_load = self._rpart_name[2]
        self._source_code_path = None
        self._decoded_source = None
        self._compiled_code = None
        self._validate_args()
        self._candidate_paths = self._get_candidate_paths([p for p in path_list])
        self._subpackage_search_paths = self._get_subpackage_search_paths(self._candidate_paths)
        self._validate_final()

    def _validate_args(self):
        if self._split_name[0] != 'ansible_collections':
            raise ImportError('this loader can only load packages from the ansible_collections package, not {0}'.format(self._fullname))

    def _get_candidate_paths(self, path_list):
        return path_list

    def _get_subpackage_search_paths(self, candidate_paths):
        return candidate_paths

    def _validate_final(self):
        pass

class TestAnsibleCollectionLoader:
    @pytest.fixture
    def loader(self, monkeypatch):
        monkeypatch.setattr(_AnsibleCollectionLoader, "_validate_args", MockAnsibleCollectionPkgLoaderBase._validate_args)
        monkeypatch.setattr(_AnsibleCollectionLoader, "_get_subpackage_search_paths", MockAnsibleCollectionPkgLoaderBase._get_subpackage_search_paths)
        return _AnsibleCollectionLoader("ansible_collections.namespace.ansible.builtin", ["path"])

    def test_get_candidate_paths_single_path(self, loader):
        assert loader._get_candidate_paths(["path"]) == ["path"]

    def test_get_candidate_paths_multiple_paths_builtin(self, loader):
        loader._split_name = ["ansible_collections", "ansible", "builtin"]
        assert loader._get_candidate_paths(["path1", "path2"]) == ["path1", "path2"]

    def test_get_candidate_paths_multiple_paths_non_builtin(self, loader):
        loader._split_name = ["ansible_collections", "namespace", "ansible", "custom"]
        with pytest.raises(ValueError, match="this loader requires exactly one path to search"):
            loader._get_candidate_paths(["path1", "path2"])

    def test_get_candidate_paths_no_paths(self, loader):
        loader._split_name = ["ansible_collections", "namespace", "ansible", "custom"]
        with pytest.raises(ValueError, match="this loader requires exactly one path to search"):
            loader._get_candidate_paths([])

    def test_get_candidate_paths_single_path_non_builtin(self, loader):
        loader._split_name = ["ansible_collections", "namespace", "ansible", "custom"]
        assert loader._get_candidate_paths(["path"]) == ["path"]
