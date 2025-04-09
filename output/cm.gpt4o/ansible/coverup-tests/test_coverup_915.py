# file lib/ansible/utils/collection_loader/_collection_finder.py:296-298
# lines [296, 297]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, fullname):
        self._fullname = fullname
        self._split_name = ['ansible_collections']
        self._subpackage_search_paths = []

def test_ansible_collection_pkg_loader_base():
    # Create an instance of the mock class
    loader = MockAnsibleCollectionPkgLoaderBase(fullname="ansible_collections.mock_package")
    
    # Assert that the _allows_package_code attribute is False
    assert loader._allows_package_code is False
