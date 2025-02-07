# file: lib/ansible/utils/collection_loader/_collection_finder.py:519-522
# asked: {"lines": [519, 520, 521, 522], "branches": [[521, 0], [521, 522]]}
# gained: {"lines": [519, 520, 521, 522], "branches": [[521, 0], [521, 522]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoader

class MockAnsibleCollectionPkgLoader(_AnsibleCollectionPkgLoader):
    def __init__(self, fullname, split_name):
        self._fullname = fullname
        self._split_name = split_name

    def _validate_args(self):
        # Mock the base class validation to avoid triggering it
        if self._split_name[0] != 'ansible_collections':
            raise ImportError('this loader can only load packages from the ansible_collections package, not {0}'.format(self._fullname))
        # Call the actual method to test the additional validation
        super()._validate_args()

def test_validate_args_with_valid_split_name():
    loader = MockAnsibleCollectionPkgLoader('ansible_collections.valid.fullname', ['ansible_collections', 'valid', 'fullname'])
    loader._validate_args()  # Should not raise an exception

def test_validate_args_with_invalid_split_name():
    loader = MockAnsibleCollectionPkgLoader('ansible_collections.invalid.fullname', ['ansible_collections', 'invalid'])
    with pytest.raises(ImportError, match='this loader can only load collection packages'):
        loader._validate_args()
