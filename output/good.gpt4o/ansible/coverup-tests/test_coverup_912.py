# file lib/ansible/utils/collection_loader/_collection_finder.py:488-489
# lines [488, 489]
# branches []

import pytest
from unittest.mock import patch

# Assuming the class _AnsibleCollectionPkgLoaderBase is imported from the module
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

@pytest.fixture
def mock_loader():
    class MockLoader(_AnsibleCollectionPkgLoaderBase):
        def __init__(self, subpackage_search_paths=None, source_code_path=None):
            self._subpackage_search_paths = subpackage_search_paths
            self._source_code_path = source_code_path

    return MockLoader

def test_ansible_collection_pkg_loader_repr_with_subpackage_search_paths(mock_loader):
    loader = mock_loader(subpackage_search_paths=['/path/to/subpackage'])
    repr_str = repr(loader)
    assert repr_str == "MockLoader(path=['/path/to/subpackage'])"

def test_ansible_collection_pkg_loader_repr_with_source_code_path(mock_loader):
    loader = mock_loader(source_code_path='/path/to/source')
    repr_str = repr(loader)
    assert repr_str == "MockLoader(path=/path/to/source)"

def test_ansible_collection_pkg_loader_repr_with_none(mock_loader):
    loader = mock_loader()
    repr_str = repr(loader)
    assert repr_str == "MockLoader(path=None)"
