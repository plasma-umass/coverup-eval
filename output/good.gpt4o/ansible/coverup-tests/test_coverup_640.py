# file lib/ansible/utils/collection_loader/_collection_finder.py:130-136
# lines [130, 131, 132, 134, 136]
# branches []

import sys
import pytest
from unittest import mock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder, AnsibleCollectionConfig

@pytest.fixture
def mock_remove(mocker):
    return mocker.patch.object(_AnsibleCollectionFinder, '_remove')

@pytest.fixture
def mock_ansible_collection_path_hook(mocker):
    return mocker.patch.object(_AnsibleCollectionFinder, '_ansible_collection_path_hook', create=True)

@pytest.fixture
def reset_collection_finder():
    original_finder = AnsibleCollectionConfig.collection_finder
    AnsibleCollectionConfig._collection_finder = None
    yield
    AnsibleCollectionConfig._collection_finder = original_finder

def test_install(mock_remove, mock_ansible_collection_path_hook, reset_collection_finder):
    finder = _AnsibleCollectionFinder()
    
    # Mocking the methods and attributes
    finder._remove = mock_remove
    finder._ansible_collection_path_hook = mock_ansible_collection_path_hook
    
    # Ensure sys.meta_path and sys.path_hooks are clean before the test
    original_meta_path = sys.meta_path[:]
    original_path_hooks = sys.path_hooks[:]
    
    try:
        finder._install()
        
        # Assertions to verify the postconditions
        assert sys.meta_path[0] == finder
        assert sys.path_hooks[0] == finder._ansible_collection_path_hook
        assert AnsibleCollectionConfig.collection_finder == finder
        
    finally:
        # Clean up to ensure no side effects on other tests
        sys.meta_path = original_meta_path
        sys.path_hooks = original_path_hooks
        AnsibleCollectionConfig._collection_finder = None
