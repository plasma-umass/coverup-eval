# file: lib/ansible/utils/collection_loader/_collection_finder.py:158-163
# asked: {"lines": [158, 159, 160, 161, 162, 163], "branches": [[161, 162], [161, 163]]}
# gained: {"lines": [158, 159, 160, 161, 162, 163], "branches": [[161, 162], [161, 163]]}

import pytest
from unittest.mock import patch

from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

@pytest.fixture
def collection_finder():
    return _AnsibleCollectionFinder(paths=['/fake/path'], scan_sys_paths=False)

def test_n_collection_paths_cached(collection_finder):
    collection_finder._n_cached_collection_paths = ['cached_path']
    assert collection_finder._n_collection_paths == ['cached_path']

def test_n_collection_paths_not_cached(collection_finder):
    collection_finder._n_cached_collection_paths = None
    collection_finder._n_playbook_paths = ['playbook_path']
    collection_finder._n_configured_paths = ['configured_path']
    expected_paths = ['playbook_path', 'configured_path']
    assert collection_finder._n_collection_paths == expected_paths
    assert collection_finder._n_cached_collection_paths == expected_paths
