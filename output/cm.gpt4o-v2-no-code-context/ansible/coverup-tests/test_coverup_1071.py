# file: lib/ansible/utils/collection_loader/_collection_finder.py:492-496
# asked: {"lines": [496], "branches": [[495, 496]]}
# gained: {"lines": [496], "branches": [[495, 496]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionRootPkgLoader

class MockLoaderBase:
    def __init__(self, fullname, path_list=None):
        self._fullname = fullname
        self._split_name = fullname.split('.')
        self._validate_args()

    def _validate_args(self):
        pass

class TestAnsibleCollectionRootPkgLoader:
    @pytest.fixture(autouse=True)
    def setup_loader(self, monkeypatch):
        monkeypatch.setattr(
            'ansible.utils.collection_loader._collection_finder._AnsibleCollectionPkgLoaderBase',
            MockLoaderBase
        )
        self.loader = _AnsibleCollectionRootPkgLoader('ansible_collections', [])
        yield
        del self.loader

    def test_validate_args_import_error(self):
        self.loader._split_name = ['ansible_collections', 'extra']
        self.loader._fullname = 'ansible_collections.extra'
        with pytest.raises(ImportError) as excinfo:
            self.loader._validate_args()
        assert str(excinfo.value) == 'this loader can only load the ansible_collections toplevel package, not ansible_collections.extra'

    def test_validate_args_no_error(self):
        self.loader._split_name = ['ansible_collections']
        self.loader._fullname = 'ansible_collections'
        try:
            self.loader._validate_args()
        except ImportError:
            pytest.fail("ImportError raised unexpectedly")
