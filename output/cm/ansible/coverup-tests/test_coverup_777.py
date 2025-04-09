# file lib/ansible/utils/collection_loader/_collection_finder.py:589-593
# lines [589, 591, 592]
# branches []

import pytest
from ansible.utils.collection_loader import _collection_finder

class MockAnsibleCollectionPkgLoaderBase(_collection_finder._AnsibleCollectionPkgLoaderBase):
    def __init__(self, fullname):
        super().__init__(fullname)

def test_ansible_collection_loader_attributes(mocker):
    # Mock the __init__ method of _AnsibleCollectionPkgLoaderBase to not require the fullname argument
    mocker.patch.object(_collection_finder._AnsibleCollectionPkgLoaderBase, '__init__', return_value=None)
    
    # Instantiate the _AnsibleCollectionLoader to test its attributes
    loader = _collection_finder._AnsibleCollectionLoader('dummy_fullname')

    # Assert that the _redirected_package_map is a dictionary
    assert isinstance(loader._redirected_package_map, dict)
    # Assert that the _redirected_package_map is initially empty
    assert loader._redirected_package_map == {}
    # Assert that the _allows_package_code is a boolean and set to True
    assert isinstance(loader._allows_package_code, bool)
    assert loader._allows_package_code is True
