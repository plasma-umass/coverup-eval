# file: lib/ansible/utils/collection_loader/_collection_finder.py:492-496
# asked: {"lines": [492, 493, 494, 495, 496], "branches": [[495, 0], [495, 496]]}
# gained: {"lines": [492, 493, 494, 495, 496], "branches": [[495, 0], [495, 496]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionRootPkgLoader

class MockAnsibleCollectionRootPkgLoader(_AnsibleCollectionRootPkgLoader):
    def __init__(self, fullname, split_name):
        self._fullname = fullname
        self._split_name = split_name

def test_validate_args_with_valid_split_name():
    loader = MockAnsibleCollectionRootPkgLoader('ansible_collections', ['ansible_collections'])
    loader._validate_args()  # Should not raise ImportError

def test_validate_args_with_invalid_split_name():
    loader = MockAnsibleCollectionRootPkgLoader('ansible_collections.invalid', ['ansible_collections', 'invalid'])
    with pytest.raises(ImportError, match='this loader can only load the ansible_collections toplevel package'):
        loader._validate_args()
