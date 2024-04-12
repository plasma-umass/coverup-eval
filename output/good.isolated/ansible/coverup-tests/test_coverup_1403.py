# file lib/ansible/utils/collection_loader/_collection_finder.py:406-409
# lines [408]
# branches ['407->408']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, fullname):
        self._fullname = fullname
        self._subpackage_search_paths = None

def test_ansible_collection_pkg_loader_base_is_package_raises_value_error():
    # Setup the loader with a specific fullname
    loader = MockAnsibleCollectionPkgLoaderBase('test_loader_fullname')

    # Test that the ValueError is raised when a different fullname is passed
    with pytest.raises(ValueError) as excinfo:
        loader.is_package('different_fullname')

    # Check that the exception message is correct
    assert str(excinfo.value) == 'this loader cannot answer is_package for different_fullname, only test_loader_fullname'

    # Cleanup is not necessary as we are not modifying any global state
