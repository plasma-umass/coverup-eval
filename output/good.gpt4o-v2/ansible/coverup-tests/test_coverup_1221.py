# file: lib/ansible/utils/collection_loader/_collection_finder.py:524-532
# asked: {"lines": [528, 529, 532], "branches": [[525, 528], [528, 529], [528, 532]]}
# gained: {"lines": [528, 529, 532], "branches": [[525, 528], [528, 529], [528, 532]]}

import pytest

from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoader

class MockAnsibleCollectionPkgLoader(_AnsibleCollectionPkgLoader):
    def __init__(self, split_name, subpackage_search_paths, package_to_load, candidate_paths):
        self._split_name = split_name
        self._subpackage_search_paths = subpackage_search_paths
        self._package_to_load = package_to_load
        self._candidate_paths = candidate_paths
        self._source_code_path = None  # Mock attribute to avoid AttributeError

def test_validate_final_ansible_builtin():
    loader = MockAnsibleCollectionPkgLoader(
        split_name=['some', 'ansible', 'builtin'],
        subpackage_search_paths=['some_path'],
        package_to_load='some_package',
        candidate_paths=['some_candidate_path']
    )
    loader._validate_final()
    assert loader._subpackage_search_paths == []

def test_validate_final_no_subpackage_search_paths():
    loader = MockAnsibleCollectionPkgLoader(
        split_name=['some', 'other', 'collection'],
        subpackage_search_paths=[],
        package_to_load='some_package',
        candidate_paths=['some_candidate_path']
    )
    with pytest.raises(ImportError, match="no some_package found in \['some_candidate_path'\]"):
        loader._validate_final()

def test_validate_final_subpackage_search_paths():
    loader = MockAnsibleCollectionPkgLoader(
        split_name=['some', 'other', 'collection'],
        subpackage_search_paths=['path1', 'path2'],
        package_to_load='some_package',
        candidate_paths=['some_candidate_path']
    )
    loader._validate_final()
    assert loader._subpackage_search_paths == ['path1']
