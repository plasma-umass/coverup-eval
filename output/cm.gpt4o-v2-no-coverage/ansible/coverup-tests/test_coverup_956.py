# file: lib/ansible/utils/collection_loader/_collection_finder.py:488-489
# asked: {"lines": [488, 489], "branches": []}
# gained: {"lines": [488, 489], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:
    
    @pytest.fixture
    def loader(self, monkeypatch):
        def mock_validate_args(self):
            pass
        
        monkeypatch.setattr(_AnsibleCollectionPkgLoaderBase, "_validate_args", mock_validate_args)
        return _AnsibleCollectionPkgLoaderBase(fullname="ansible_collections.test.fullname", path_list=["/path/to/collection"])

    def test_repr_with_subpackage_search_paths(self, loader):
        loader._subpackage_search_paths = ["/path/to/subpackage"]
        repr_str = repr(loader)
        assert repr_str == "_AnsibleCollectionPkgLoaderBase(path=['/path/to/subpackage'])"

    def test_repr_with_source_code_path(self, loader):
        loader._subpackage_search_paths = None
        loader._source_code_path = "/path/to/source"
        repr_str = repr(loader)
        assert repr_str == "_AnsibleCollectionPkgLoaderBase(path=/path/to/source)"
