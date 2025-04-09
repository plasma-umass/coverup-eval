# file: lib/ansible/utils/collection_loader/_collection_finder.py:333-334
# asked: {"lines": [333, 334], "branches": []}
# gained: {"lines": [333, 334], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self):
        pass

class TestAnsibleCollectionPkgLoaderBase:
    
    def test_validate_final(self):
        loader = MockAnsibleCollectionPkgLoaderBase()
        result = loader._validate_final()
        assert result is None
