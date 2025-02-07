# file: lib/ansible/utils/collection_loader/_collection_finder.py:505-514
# asked: {"lines": [505, 506, 507, 508, 509, 511, 513, 514], "branches": [[508, 0], [508, 509], [513, 0], [513, 514]]}
# gained: {"lines": [505, 506, 511], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionNSPkgLoader

class MockAnsibleCollectionNSPkgLoader(_AnsibleCollectionNSPkgLoader):
    def __init__(self, fullname, path_list=None):
        self._fullname = fullname
        self._split_name = fullname.split('.')
        self._package_to_load = fullname.rpartition('.')[2]
        self._candidate_paths = path_list or []
        self._subpackage_search_paths = []

    def _validate_args(self):
        if len(self._split_name) != 2:
            raise ImportError('this loader can only load collections namespace packages, not {0}'.format(self._fullname))

    def _validate_final(self):
        if not self._subpackage_search_paths and self._package_to_load != 'ansible':
            raise ImportError('no {0} found in {1}'.format(self._package_to_load, self._candidate_paths))

def test_validate_args_correct_namespace():
    loader = MockAnsibleCollectionNSPkgLoader('valid.namespace')
    loader._validate_args()  # Should not raise

def test_validate_args_incorrect_namespace():
    loader = MockAnsibleCollectionNSPkgLoader('invalid.namespace.extra')
    with pytest.raises(ImportError, match='this loader can only load collections namespace packages'):
        loader._validate_args()

def test_validate_final_no_subpackage_paths():
    loader = MockAnsibleCollectionNSPkgLoader('ansible.valid')
    loader._subpackage_search_paths = []
    loader._package_to_load = 'ansible'
    loader._validate_final()  # Should not raise

def test_validate_final_no_subpackage_paths_invalid_package():
    loader = MockAnsibleCollectionNSPkgLoader('invalid.package')
    loader._subpackage_search_paths = []
    loader._package_to_load = 'invalid'
    with pytest.raises(ImportError, match='no invalid found in'):
        loader._validate_final()
