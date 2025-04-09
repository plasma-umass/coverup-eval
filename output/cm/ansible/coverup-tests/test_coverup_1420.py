# file lib/ansible/utils/collection_loader/_collection_finder.py:465-483
# lines [467]
# branches ['466->467']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockLoader(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, fullname):
        # Mock the required attributes to bypass the _validate_args check
        self._fullname = fullname
        self._split_name = ['ansible_collections'] + fullname.split('.')
        self._compiled_code = None

    def get_filename(self, fullname):
        return None

    def get_source(self, fullname):
        return None

@pytest.fixture
def mock_loader():
    # Use a fullname that starts with 'ansible_collections' to pass the validation
    return MockLoader(fullname='ansible_collections.dummy_namespace.dummy_collection')

def test_get_code_with_compiled_code(mock_loader):
    # Set the _compiled_code attribute to simulate a previously compiled code object
    mock_loader._compiled_code = "compiled"

    # Call get_code and assert that it returns the compiled code without recompiling
    assert mock_loader.get_code("ansible_collections.dummy_namespace.dummy_collection") == "compiled"

def test_get_code_without_compiled_code(mock_loader):
    # Ensure _compiled_code is None to simulate no previously compiled code
    mock_loader._compiled_code = None

    # Call get_code and assert that it returns None since get_source returns None
    assert mock_loader.get_code("ansible_collections.dummy_namespace.dummy_collection") is None
