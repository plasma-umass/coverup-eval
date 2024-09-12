# file: lib/ansible/utils/collection_loader/_collection_finder.py:328-330
# asked: {"lines": [328, 330], "branches": []}
# gained: {"lines": [328, 330], "branches": []}

import os
import pytest
from ansible.module_utils.common.text.converters import to_bytes
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, tmpdir):
        self.test_dir = tmpdir.mkdir("test_dir")
        self.nonexistent_dir = tmpdir.join("nonexistent_dir")
        yield
        # Cleanup is handled by tmpdir fixture

    def test_get_subpackage_search_paths_with_existing_directories(self):
        existing_dir = self.test_dir.mkdir("existing_dir")
        candidate_paths = [str(existing_dir), str(self.nonexistent_dir)]
        loader = _AnsibleCollectionPkgLoaderBase(fullname="ansible_collections.test_fullname", path_list=candidate_paths)
        result = loader._get_subpackage_search_paths(candidate_paths)
        assert result == [str(existing_dir)]

    def test_get_subpackage_search_paths_with_no_existing_directories(self):
        candidate_paths = [str(self.nonexistent_dir)]
        loader = _AnsibleCollectionPkgLoaderBase(fullname="ansible_collections.test_fullname", path_list=candidate_paths)
        result = loader._get_subpackage_search_paths(candidate_paths)
        assert result == []

    def test_get_subpackage_search_paths_with_mixed_directories(self):
        existing_dir = self.test_dir.mkdir("existing_dir")
        another_existing_dir = self.test_dir.mkdir("another_existing_dir")
        candidate_paths = [str(existing_dir), str(self.nonexistent_dir), str(another_existing_dir)]
        loader = _AnsibleCollectionPkgLoaderBase(fullname="ansible_collections.test_fullname", path_list=candidate_paths)
        result = loader._get_subpackage_search_paths(candidate_paths)
        assert result == [str(existing_dir), str(another_existing_dir)]
