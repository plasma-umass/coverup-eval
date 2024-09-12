# file: lib/ansible/utils/collection_loader/_collection_finder.py:187-225
# asked: {"lines": [187, 190, 191, 192, 193, 195, 197, 200, 201, 202, 205, 207, 208, 211, 212, 214, 215, 216, 217, 218, 219, 220, 222, 223, 225], "branches": [[195, 197], [195, 200], [200, 201], [200, 207], [201, 202], [201, 205], [207, 208], [207, 211], [212, 214], [212, 215], [215, 216], [215, 217], [217, 218], [217, 219], [219, 220], [219, 222]]}
# gained: {"lines": [187, 190, 191, 192, 193, 195, 197, 200, 201, 202, 205, 207, 208, 211, 212, 214, 215, 216, 217, 218, 219, 220, 222, 223, 225], "branches": [[195, 197], [195, 200], [200, 201], [200, 207], [201, 202], [201, 205], [207, 208], [207, 211], [212, 214], [212, 215], [215, 216], [215, 217], [217, 218], [217, 219], [219, 220], [219, 222]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder, _AnsibleInternalRedirectLoader, _AnsibleCollectionRootPkgLoader, _AnsibleCollectionNSPkgLoader, _AnsibleCollectionPkgLoader, _AnsibleCollectionLoader

@pytest.fixture
def collection_finder():
    return _AnsibleCollectionFinder(paths=['/fake/path'])

def test_find_module_top_level_package(collection_finder):
    with pytest.raises(ValueError, match='path should not be specified for top-level packages'):
        collection_finder.find_module('ansible', path=['/some/path'])

def test_find_module_subpackage_no_path(collection_finder):
    with pytest.raises(ValueError, match='path must be specified for subpackages'):
        collection_finder.find_module('ansible.module_utils')

def test_find_module_not_interested(collection_finder):
    assert collection_finder.find_module('not_ansible') is None

def test_find_module_ansible_internal_redirect_loader(monkeypatch, collection_finder):
    def mock_init(self, fullname, path_list):
        pass
    monkeypatch.setattr(_AnsibleInternalRedirectLoader, '__init__', mock_init)
    assert isinstance(collection_finder.find_module('ansible.module_utils', path=['/some/path']), _AnsibleInternalRedirectLoader)

def test_find_module_ansible_collection_root_pkg_loader(monkeypatch, collection_finder):
    def mock_init(self, fullname, path_list):
        pass
    monkeypatch.setattr(_AnsibleCollectionRootPkgLoader, '__init__', mock_init)
    assert isinstance(collection_finder.find_module('ansible_collections', path=None), _AnsibleCollectionRootPkgLoader)

def test_find_module_ansible_collection_ns_pkg_loader(monkeypatch, collection_finder):
    def mock_init(self, fullname, path_list):
        pass
    monkeypatch.setattr(_AnsibleCollectionNSPkgLoader, '__init__', mock_init)
    assert isinstance(collection_finder.find_module('ansible_collections.somens', path=['/some/path']), _AnsibleCollectionNSPkgLoader)

def test_find_module_ansible_collection_pkg_loader(monkeypatch, collection_finder):
    def mock_init(self, fullname, path_list):
        pass
    monkeypatch.setattr(_AnsibleCollectionPkgLoader, '__init__', mock_init)
    assert isinstance(collection_finder.find_module('ansible_collections.somens.somecoll', path=['/some/path']), _AnsibleCollectionPkgLoader)

def test_find_module_ansible_collection_loader(monkeypatch, collection_finder):
    def mock_init(self, fullname, path_list):
        pass
    monkeypatch.setattr(_AnsibleCollectionLoader, '__init__', mock_init)
    assert isinstance(collection_finder.find_module('ansible_collections.somens.somecoll.module', path=['/some/path']), _AnsibleCollectionLoader)

def test_find_module_import_error(monkeypatch, collection_finder):
    def mock_init(self, fullname, path_list):
        raise ImportError
    monkeypatch.setattr(_AnsibleCollectionLoader, '__init__', mock_init)
    assert collection_finder.find_module('ansible_collections.somens.somecoll.module', path=['/some/path']) is None
