# file: lib/ansible/utils/collection_loader/_collection_finder.py:319-321
# asked: {"lines": [319, 320, 321], "branches": [[320, 0], [320, 321]]}
# gained: {"lines": [319, 320, 321], "branches": [[320, 0], [320, 321]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class TestAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def _get_candidate_paths(self, path_list):
        return []

    def _get_subpackage_search_paths(self, candidate_paths):
        return []

    def _validate_final(self):
        pass

def test_validate_args_success():
    loader = TestAnsibleCollectionPkgLoaderBase('ansible_collections.test', path_list=[])
    assert loader._split_name[0] == 'ansible_collections'

def test_validate_args_failure():
    with pytest.raises(ImportError, match="this loader can only load packages from the ansible_collections package, not invalid_package"):
        TestAnsibleCollectionPkgLoaderBase('invalid_package', path_list=[])
