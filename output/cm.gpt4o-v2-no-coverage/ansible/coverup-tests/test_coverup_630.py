# file: lib/ansible/utils/collection_loader/_collection_finder.py:492-496
# asked: {"lines": [492, 493, 494, 495, 496], "branches": [[495, 0], [495, 496]]}
# gained: {"lines": [492, 493, 494, 495, 496], "branches": [[495, 0], [495, 496]]}

import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionRootPkgLoader
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self, fullname, path_list=None):
        self._fullname = fullname
        self._split_name = fullname.split('.')
        self._validate_args_called = False

    def _validate_args(self):
        self._validate_args_called = True

    def _get_candidate_paths(self, path_list):
        return []

    def _get_subpackage_search_paths(self, candidate_paths):
        return []

    def _validate_final(self):
        pass

def test_validate_args_correct(monkeypatch):
    monkeypatch.setattr(_AnsibleCollectionRootPkgLoader, '_get_candidate_paths', MockAnsibleCollectionPkgLoaderBase._get_candidate_paths)
    monkeypatch.setattr(_AnsibleCollectionRootPkgLoader, '_get_subpackage_search_paths', MockAnsibleCollectionPkgLoaderBase._get_subpackage_search_paths)
    monkeypatch.setattr(_AnsibleCollectionRootPkgLoader, '_validate_final', MockAnsibleCollectionPkgLoaderBase._validate_final)
    loader = _AnsibleCollectionRootPkgLoader('ansible_collections', path_list=[])
    assert loader._split_name == ['ansible_collections']

def test_validate_args_incorrect(monkeypatch):
    monkeypatch.setattr(_AnsibleCollectionRootPkgLoader, '_get_candidate_paths', MockAnsibleCollectionPkgLoaderBase._get_candidate_paths)
    monkeypatch.setattr(_AnsibleCollectionRootPkgLoader, '_get_subpackage_search_paths', MockAnsibleCollectionPkgLoaderBase._get_subpackage_search_paths)
    monkeypatch.setattr(_AnsibleCollectionRootPkgLoader, '_validate_final', MockAnsibleCollectionPkgLoaderBase._validate_final)
    with pytest.raises(ImportError, match='this loader can only load the ansible_collections toplevel package'):
        _AnsibleCollectionRootPkgLoader('ansible_collections.subpackage', path_list=[])
