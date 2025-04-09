# file: lib/ansible/utils/collection_loader/_collection_finder.py:524-532
# asked: {"lines": [524, 525, 527, 528, 529, 532], "branches": [[525, 527], [525, 528], [528, 529], [528, 532]]}
# gained: {"lines": [524, 525, 527, 528, 529, 532], "branches": [[525, 527], [525, 528], [528, 529], [528, 532]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoader

class MockAnsibleCollectionPkgLoader(_AnsibleCollectionPkgLoader):
    def __init__(self, split_name, subpackage_search_paths, package_to_load, candidate_paths):
        self._split_name = split_name
        self._subpackage_search_paths = subpackage_search_paths
        self._package_to_load = package_to_load
        self._candidate_paths = candidate_paths

@pytest.fixture
def mock_loader():
    return MockAnsibleCollectionPkgLoader

def test_validate_final_builtin(mock_loader):
    loader = mock_loader(['some_namespace', 'ansible', 'builtin'], ['some_path'], 'some_package', ['some_candidate_path'])
    loader._validate_final()
    assert loader._subpackage_search_paths == []

def test_validate_final_no_search_paths(mock_loader):
    loader = mock_loader(['some_namespace', 'some_collection'], [], 'some_package', ['some_candidate_path'])
    with pytest.raises(ImportError, match='no some_package found in \[\'some_candidate_path\'\]'):
        loader._validate_final()

def test_validate_final_single_search_path(mock_loader):
    loader = mock_loader(['some_namespace', 'some_collection'], ['some_path'], 'some_package', ['some_candidate_path'])
    loader._validate_final()
    assert loader._subpackage_search_paths == ['some_path']
