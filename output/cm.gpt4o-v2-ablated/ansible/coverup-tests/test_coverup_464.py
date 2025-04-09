# file: lib/ansible/utils/collection_loader/_collection_finder.py:492-496
# asked: {"lines": [496], "branches": [[495, 496]]}
# gained: {"lines": [496], "branches": [[495, 496]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionRootPkgLoader, _AnsibleCollectionPkgLoaderBase

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, fullname, split_name):
        self._fullname = fullname
        self._split_name = split_name

@pytest.fixture
def mock_loader():
    return MockAnsibleCollectionPkgLoaderBase('ansible_collections', ['ansible_collections'])

def test_validate_args_success(mock_loader, monkeypatch):
    class TestLoader(_AnsibleCollectionRootPkgLoader):
        def __init__(self, base_loader):
            self._fullname = base_loader._fullname
            self._split_name = base_loader._split_name

    loader = TestLoader(mock_loader)
    monkeypatch.setattr(_AnsibleCollectionPkgLoaderBase, '_validate_args', lambda x: None)
    loader._validate_args()

def test_validate_args_failure(monkeypatch):
    class TestLoader(_AnsibleCollectionRootPkgLoader):
        def __init__(self, fullname, split_name):
            self._fullname = fullname
            self._split_name = split_name

    loader = TestLoader('ansible_collections.subpackage', ['ansible_collections', 'subpackage'])
    monkeypatch.setattr(_AnsibleCollectionPkgLoaderBase, '_validate_args', lambda x: None)
    
    with pytest.raises(ImportError) as excinfo:
        loader._validate_args()
    
    assert str(excinfo.value) == 'this loader can only load the ansible_collections toplevel package, not ansible_collections.subpackage'
