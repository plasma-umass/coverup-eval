# file: lib/ansible/utils/collection_loader/_collection_finder.py:594-597
# asked: {"lines": [595, 596, 597], "branches": [[596, 0], [596, 597]]}
# gained: {"lines": [595, 596, 597], "branches": [[596, 0], [596, 597]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionLoader, _AnsibleCollectionPkgLoaderBase

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, split_name, fullname):
        self._split_name = split_name
        self._fullname = fullname

    def _validate_args(self):
        pass

class TestAnsibleCollectionLoader:
    def test_validate_args_with_valid_split_name(self, mocker):
        # Mocking the base class to avoid calling its actual implementation
        mocker.patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_args', return_value=None)
        
        loader = _AnsibleCollectionLoader.__new__(_AnsibleCollectionLoader)
        loader._split_name = ['namespace', 'collection', 'module', 'submodule']
        loader._fullname = 'namespace.collection.module.submodule'
        
        # This should not raise an exception
        loader._validate_args()

    def test_validate_args_with_invalid_split_name(self, mocker):
        # Mocking the base class to avoid calling its actual implementation
        mocker.patch.object(_AnsibleCollectionPkgLoaderBase, '_validate_args', return_value=None)
        
        loader = _AnsibleCollectionLoader.__new__(_AnsibleCollectionLoader)
        loader._split_name = ['namespace', 'collection', 'module']
        loader._fullname = 'namespace.collection.module'
        
        with pytest.raises(ValueError, match='this loader is only for sub-collection modules/packages, not namespace.collection.module'):
            loader._validate_args()
