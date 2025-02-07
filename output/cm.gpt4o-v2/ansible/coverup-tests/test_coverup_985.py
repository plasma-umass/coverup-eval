# file: lib/ansible/utils/collection_loader/_collection_finder.py:488-489
# asked: {"lines": [488, 489], "branches": []}
# gained: {"lines": [488, 489], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def _validate_args(self):
        # Override to bypass the original validation
        pass

def test_ansible_collection_pkg_loader_base_repr():
    # Create an instance of the mock class with mock data
    loader = MockAnsibleCollectionPkgLoaderBase(fullname='test.fullname', path_list=['/mock/path'])

    # Mock the _subpackage_search_paths and _source_code_path attributes
    loader._subpackage_search_paths = ['/mock/subpackage/path']
    loader._source_code_path = '/mock/source/code/path'

    # Test the __repr__ method
    repr_result = repr(loader)
    assert repr_result == "MockAnsibleCollectionPkgLoaderBase(path=['/mock/subpackage/path'])"

    # Clean up
    del loader

def test_ansible_collection_pkg_loader_base_repr_no_subpackage_search_paths():
    # Create an instance of the mock class with mock data
    loader = MockAnsibleCollectionPkgLoaderBase(fullname='test.fullname', path_list=['/mock/path'])

    # Mock the _subpackage_search_paths and _source_code_path attributes
    loader._subpackage_search_paths = None
    loader._source_code_path = '/mock/source/code/path'

    # Test the __repr__ method
    repr_result = repr(loader)
    assert repr_result == "MockAnsibleCollectionPkgLoaderBase(path=/mock/source/code/path)"

    # Clean up
    del loader
