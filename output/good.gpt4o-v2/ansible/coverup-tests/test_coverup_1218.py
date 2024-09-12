# file: lib/ansible/utils/collection_loader/_collection_finder.py:110-128
# asked: {"lines": [114, 119, 128], "branches": [[113, 114], [118, 119], [127, 128]]}
# gained: {"lines": [114, 119], "branches": [[113, 114], [118, 119]]}

import pytest
import sys
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
from ansible.utils.collection_loader._collection_config import AnsibleCollectionConfig

def test_remove_meta_path(monkeypatch):
    # Setup: Add _AnsibleCollectionFinder instance to sys.meta_path
    finder_instance = _AnsibleCollectionFinder()
    monkeypatch.setattr(sys, 'meta_path', [finder_instance])

    # Ensure the instance is in sys.meta_path
    assert finder_instance in sys.meta_path

    # Call the method
    _AnsibleCollectionFinder._remove()

    # Assert the instance is removed from sys.meta_path
    assert finder_instance not in sys.meta_path

def test_remove_path_hooks(monkeypatch):
    # Setup: Add _AnsibleCollectionFinder instance to sys.path_hooks
    class PathHook:
        __self__ = _AnsibleCollectionFinder()
    
    path_hook_instance = PathHook()
    monkeypatch.setattr(sys, 'path_hooks', [path_hook_instance])

    # Ensure the instance is in sys.path_hooks
    assert path_hook_instance in sys.path_hooks

    # Call the method
    _AnsibleCollectionFinder._remove()

    # Assert the instance is removed from sys.path_hooks
    assert path_hook_instance not in sys.path_hooks

def test_remove_collection_finder(monkeypatch):
    # Setup: Set AnsibleCollectionConfig._collection_finder to an instance
    monkeypatch.setattr(AnsibleCollectionConfig, '_collection_finder', _AnsibleCollectionFinder())

    # Ensure the _collection_finder is set
    assert AnsibleCollectionConfig._collection_finder is not None

    # Call the method
    _AnsibleCollectionFinder._remove()

    # Assert the _collection_finder is set to None
    assert AnsibleCollectionConfig._collection_finder is None

    # Ensure no AssertionError is raised
    try:
        if AnsibleCollectionConfig.collection_finder is not None:
            raise AssertionError('_AnsibleCollectionFinder remove did not reset AnsibleCollectionConfig.collection_finder')
    except AssertionError:
        pytest.fail("_AnsibleCollectionFinder remove did not reset AnsibleCollectionConfig.collection_finder")
