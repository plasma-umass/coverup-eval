# file lib/ansible/utils/collection_loader/_collection_finder.py:519-522
# lines [519, 520, 521, 522]
# branches ['521->exit', '521->522']

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoader

# Assuming the _AnsibleCollectionPkgLoaderBase is available and can be imported
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

# Mocking the _AnsibleCollectionPkgLoaderBase to avoid any side effects
class MockedAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, fullname):
        self._fullname = fullname
        self._split_name = self._fullname.split('.')

    def _validate_args(self):
        pass

# Injecting the mock into the _AnsibleCollectionPkgLoader class
_AnsibleCollectionPkgLoader.__bases__ = (MockedAnsibleCollectionPkgLoaderBase,)

@pytest.fixture
def collection_pkg_loader():
    fullname = "ansible_collections.namespace.name"
    loader = _AnsibleCollectionPkgLoader(fullname)
    return loader

@pytest.fixture
def collection_pkg_loader_invalid():
    fullname = "invalid_name"
    loader = _AnsibleCollectionPkgLoader(fullname)
    return loader

def test_validate_args_valid(collection_pkg_loader):
    # Test with a valid collection package name
    try:
        collection_pkg_loader._validate_args()
    except ImportError:
        pytest.fail("Unexpected ImportError raised")

def test_validate_args_invalid(collection_pkg_loader_invalid):
    # Test with an invalid collection package name
    with pytest.raises(ImportError) as excinfo:
        collection_pkg_loader_invalid._validate_args()
    assert "this loader can only load collection packages" in str(excinfo.value)
