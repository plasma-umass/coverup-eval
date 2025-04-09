# file: lib/ansible/utils/collection_loader/_collection_finder.py:187-225
# asked: {"lines": [202, 208, 222], "branches": [[201, 202], [207, 208], [219, 222]]}
# gained: {"lines": [202, 208, 222], "branches": [[201, 202], [207, 208], [219, 222]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

class MockLoader:
    def __init__(self, fullname, path_list):
        self.fullname = fullname
        self.path_list = path_list

class TestAnsibleCollectionFinder:
    @pytest.fixture(autouse=True)
    def setup(self, monkeypatch):
        self.finder = _AnsibleCollectionFinder()
        monkeypatch.setattr(self.finder.__class__, '_n_collection_paths', ['/mock/path'])
        monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._AnsibleInternalRedirectLoader', MockLoader)
        monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._AnsibleCollectionRootPkgLoader', MockLoader)
        monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._AnsibleCollectionNSPkgLoader', MockLoader)
        monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._AnsibleCollectionPkgLoader', MockLoader)
        monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._AnsibleCollectionLoader', MockLoader)

    def test_find_module_top_level_with_path(self):
        with pytest.raises(ValueError, match='path should not be specified for top-level packages'):
            self.finder.find_module('ansible', path=['/some/path'])

    def test_find_module_subpackage_without_path(self):
        with pytest.raises(ValueError, match='path must be specified for subpackages'):
            self.finder.find_module('ansible.module_utils')

    def test_find_module_collection_loader(self):
        result = self.finder.find_module('ansible_collections.somens.somecoll.some_module', path=['/some/path'])
        assert isinstance(result, MockLoader)
        assert result.fullname == 'ansible_collections.somens.somecoll.some_module'
        assert result.path_list == ['/some/path']
