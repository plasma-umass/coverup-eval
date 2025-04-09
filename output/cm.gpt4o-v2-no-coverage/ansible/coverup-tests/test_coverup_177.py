# file: lib/ansible/utils/collection_loader/_collection_finder.py:110-128
# asked: {"lines": [110, 111, 112, 113, 114, 117, 118, 119, 122, 124, 127, 128], "branches": [[112, 113], [112, 117], [113, 112], [113, 114], [117, 118], [117, 122], [118, 117], [118, 119], [127, 0], [127, 128]]}
# gained: {"lines": [110, 111, 112, 113, 114, 117, 118, 119, 122, 124, 127], "branches": [[112, 113], [112, 117], [113, 112], [113, 114], [117, 118], [117, 122], [118, 117], [118, 119], [127, 0]]}

import pytest
import sys
from unittest.mock import MagicMock, patch
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
from ansible.utils.collection_loader._collection_config import AnsibleCollectionConfig

@pytest.fixture(autouse=True)
def cleanup():
    # Ensure the state is clean before and after each test
    original_meta_path = sys.meta_path.copy()
    original_path_hooks = sys.path_hooks.copy()
    original_path_importer_cache = sys.path_importer_cache.copy()
    original_collection_finder = AnsibleCollectionConfig._collection_finder

    yield

    sys.meta_path = original_meta_path
    sys.path_hooks = original_path_hooks
    sys.path_importer_cache = original_path_importer_cache
    AnsibleCollectionConfig._collection_finder = original_collection_finder

def test_remove_meta_path():
    finder_instance = _AnsibleCollectionFinder()
    sys.meta_path.append(finder_instance)
    assert finder_instance in sys.meta_path

    _AnsibleCollectionFinder._remove()
    assert finder_instance not in sys.meta_path

def test_remove_path_hooks():
    finder_instance = _AnsibleCollectionFinder()
    path_hook = MagicMock(__self__=finder_instance)
    sys.path_hooks.append(path_hook)
    assert path_hook in sys.path_hooks

    _AnsibleCollectionFinder._remove()
    assert path_hook not in sys.path_hooks

def test_clear_path_importer_cache():
    sys.path_importer_cache['test'] = 'value'
    assert 'test' in sys.path_importer_cache

    _AnsibleCollectionFinder._remove()
    assert 'test' not in sys.path_importer_cache

def test_reset_collection_finder():
    AnsibleCollectionConfig._collection_finder = _AnsibleCollectionFinder()
    assert AnsibleCollectionConfig._collection_finder is not None

    _AnsibleCollectionFinder._remove()
    assert AnsibleCollectionConfig._collection_finder is None

def test_collection_finder_property():
    AnsibleCollectionConfig._collection_finder = _AnsibleCollectionFinder()
    assert AnsibleCollectionConfig.collection_finder is not None

    _AnsibleCollectionFinder._remove()
    assert AnsibleCollectionConfig.collection_finder is None
