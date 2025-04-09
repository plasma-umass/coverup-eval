# file: lib/ansible/utils/collection_loader/_collection_finder.py:158-163
# asked: {"lines": [158, 159, 160, 161, 162, 163], "branches": [[161, 162], [161, 163]]}
# gained: {"lines": [158, 159, 160, 161, 162, 163], "branches": [[161, 162], [161, 163]]}

import pytest
from unittest.mock import patch

@pytest.fixture
def collection_finder():
    from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
    return _AnsibleCollectionFinder(paths=['/fake/path'], scan_sys_paths=False)

def test_n_collection_paths_with_cached_paths(collection_finder):
    # Set up the cached paths
    collection_finder._n_cached_collection_paths = ['/cached/path']
    
    # Access the property
    paths = collection_finder._n_collection_paths
    
    # Assert the cached paths are returned
    assert paths == ['/cached/path']

def test_n_collection_paths_without_cached_paths(collection_finder):
    # Ensure cached paths are None
    collection_finder._n_cached_collection_paths = None
    collection_finder._n_playbook_paths = ['/playbook/path']
    collection_finder._n_configured_paths = ['/configured/path']
    
    # Access the property
    paths = collection_finder._n_collection_paths
    
    # Assert the combined paths are returned
    assert paths == ['/playbook/path', '/configured/path']
    # Assert the cached paths are now set
    assert collection_finder._n_cached_collection_paths == ['/playbook/path', '/configured/path']
