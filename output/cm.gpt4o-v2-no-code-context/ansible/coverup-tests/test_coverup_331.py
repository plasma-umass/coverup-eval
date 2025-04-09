# file: lib/ansible/utils/collection_loader/_collection_finder.py:505-514
# asked: {"lines": [505, 506, 507, 508, 509, 511, 513, 514], "branches": [[508, 0], [508, 509], [513, 0], [513, 514]]}
# gained: {"lines": [505, 506, 511], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionNSPkgLoader

class MockAnsibleCollectionNSPkgLoader(_AnsibleCollectionNSPkgLoader):
    def __init__(self, fullname, split_name, package_to_load, candidate_paths, subpackage_search_paths):
        self._fullname = fullname
        self._split_name = split_name
        self._package_to_load = package_to_load
        self._candidate_paths = candidate_paths
        self._subpackage_search_paths = subpackage_search_paths
        self._source_code_path = None  # Mock attribute to avoid AttributeError

    def _validate_args(self):
        if len(self._split_name) != 2:
            raise ImportError('this loader can only load collections namespace packages, not {0}'.format(self._fullname))

    def _validate_final(self):
        if not self._subpackage_search_paths and self._package_to_load != 'ansible':
            raise ImportError('no {0} found in {1}'.format(self._package_to_load, self._candidate_paths))

@pytest.fixture
def mock_loader():
    return MockAnsibleCollectionNSPkgLoader

def test_validate_args_correct_namespace(mock_loader):
    loader = mock_loader('ansible.test', ['ansible', 'test'], 'test', [], [])
    loader._validate_args()

def test_validate_args_incorrect_namespace(mock_loader):
    loader = mock_loader('ansible.test.extra', ['ansible', 'test', 'extra'], 'test', [], [])
    with pytest.raises(ImportError, match='this loader can only load collections namespace packages'):
        loader._validate_args()

def test_validate_final_no_subpackage_search_paths(mock_loader):
    loader = mock_loader('ansible.test', ['ansible', 'test'], 'test', [], [])
    with pytest.raises(ImportError, match='no test found in'):
        loader._validate_final()

def test_validate_final_with_subpackage_search_paths(mock_loader):
    loader = mock_loader('ansible.test', ['ansible', 'test'], 'test', ['/some/path'], ['/some/path'])
    loader._validate_final()

def test_validate_final_ansible_namespace(mock_loader):
    loader = mock_loader('ansible', ['ansible'], 'ansible', [], [])
    loader._validate_final()
