# file: lib/ansible/utils/collection_loader/_collection_finder.py:130-136
# asked: {"lines": [130, 131, 132, 134, 136], "branches": []}
# gained: {"lines": [130, 131, 132, 134, 136], "branches": []}

import pytest
import sys
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionConfig

@pytest.fixture
def collection_finder():
    return _AnsibleCollectionFinder()

def test_install_method(monkeypatch, collection_finder):
    # Mock the _remove method to avoid side effects
    monkeypatch.setattr(collection_finder, '_remove', lambda: None)
    
    # Ensure sys.meta_path and sys.path_hooks are clean before the test
    original_meta_path = sys.meta_path[:]
    original_path_hooks = sys.path_hooks[:]
    original_collection_finder = AnsibleCollectionConfig.collection_finder
    
    try:
        # Call the _install method
        collection_finder._install()
        
        # Assertions to verify the postconditions
        assert sys.meta_path[0] is collection_finder
        assert sys.path_hooks[0] == collection_finder._ansible_collection_path_hook
        assert AnsibleCollectionConfig.collection_finder is collection_finder
    finally:
        # Clean up to avoid state pollution
        sys.meta_path = original_meta_path
        sys.path_hooks = original_path_hooks
        AnsibleCollectionConfig._collection_finder = original_collection_finder
