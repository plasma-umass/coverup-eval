# file: lib/ansible/utils/collection_loader/_collection_finder.py:324-325
# asked: {"lines": [324, 325], "branches": []}
# gained: {"lines": [324, 325], "branches": []}

import os
import pytest

from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self):
        self._package_to_load = 'test_package'

class TestAnsibleCollectionPkgLoaderBase:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.loader = MockAnsibleCollectionPkgLoaderBase()
        yield
        # Cleanup if necessary

    def test_get_candidate_paths(self):
        path_list = ['/path/one', '/path/two']
        expected_paths = [os.path.join('/path/one', 'test_package'), os.path.join('/path/two', 'test_package')]
        result = self.loader._get_candidate_paths(path_list)
        assert result == expected_paths
