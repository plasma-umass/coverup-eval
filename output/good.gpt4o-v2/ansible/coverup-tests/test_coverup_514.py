# file: lib/ansible/utils/collection_loader/_collection_finder.py:158-163
# asked: {"lines": [158, 159, 160, 161, 162, 163], "branches": [[161, 162], [161, 163]]}
# gained: {"lines": [158, 159, 160, 161, 162, 163], "branches": [[161, 162], [161, 163]]}

import pytest
from unittest.mock import patch

@pytest.fixture
def collection_finder():
    from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
    return _AnsibleCollectionFinder(paths=['/fake/path'], scan_sys_paths=False)

def test_n_collection_paths_initially_empty(collection_finder):
    with patch.object(collection_finder, '_n_playbook_paths', ['/playbook/path']), \
         patch.object(collection_finder, '_n_configured_paths', ['/configured/path']):
        assert collection_finder._n_collection_paths == ['/playbook/path', '/configured/path']
        assert collection_finder._n_cached_collection_paths == ['/playbook/path', '/configured/path']

def test_n_collection_paths_cached(collection_finder):
    with patch.object(collection_finder, '_n_cached_collection_paths', ['/cached/path']):
        assert collection_finder._n_collection_paths == ['/cached/path']
