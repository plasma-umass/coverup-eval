# file: lib/ansible/utils/collection_loader/_collection_finder.py:110-128
# asked: {"lines": [114, 119, 128], "branches": [[113, 114], [118, 119], [127, 128]]}
# gained: {"lines": [114, 119], "branches": [[113, 114], [118, 119]]}

import sys
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
from ansible.utils.collection_loader import AnsibleCollectionConfig

class MockMetaPathFinder:
    pass

class MockPathHook:
    def __init__(self, self_ref):
        self.__self__ = self_ref

@pytest.fixture
def setup_meta_path(monkeypatch):
    original_meta_path = sys.meta_path[:]
    sys.meta_path.append(MockMetaPathFinder())
    sys.meta_path.append(_AnsibleCollectionFinder())
    yield
    sys.meta_path = original_meta_path

@pytest.fixture
def setup_path_hooks(monkeypatch):
    original_path_hooks = sys.path_hooks[:]
    sys.path_hooks.append(MockPathHook(MockMetaPathFinder()))
    sys.path_hooks.append(MockPathHook(_AnsibleCollectionFinder()))
    yield
    sys.path_hooks = original_path_hooks

@pytest.fixture
def setup_collection_finder(monkeypatch):
    original_finder = AnsibleCollectionConfig._collection_finder
    AnsibleCollectionConfig._collection_finder = _AnsibleCollectionFinder()
    yield
    AnsibleCollectionConfig._collection_finder = original_finder

def test_remove_meta_path(setup_meta_path):
    _AnsibleCollectionFinder._remove()
    assert not any(isinstance(mps, _AnsibleCollectionFinder) for mps in sys.meta_path)

def test_remove_path_hooks(setup_path_hooks):
    _AnsibleCollectionFinder._remove()
    assert not any(hasattr(ph, '__self__') and isinstance(ph.__self__, _AnsibleCollectionFinder) for ph in sys.path_hooks)

def test_remove_collection_finder(setup_collection_finder):
    _AnsibleCollectionFinder._remove()
    assert AnsibleCollectionConfig.collection_finder is None
