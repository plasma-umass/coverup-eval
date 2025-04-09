# file: lib/ansible/utils/collection_loader/_collection_finder.py:165-179
# asked: {"lines": [166, 167, 170, 173, 174, 178, 179], "branches": [[166, 167], [166, 170], [178, 0], [178, 179]]}
# gained: {"lines": [166, 167, 170, 173, 174, 178, 179], "branches": [[166, 167], [166, 170], [178, 0], [178, 179]]}

import os
import pytest
from unittest.mock import patch, call
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

@pytest.fixture
def collection_finder():
    return _AnsibleCollectionFinder()

def test_set_playbook_paths_string_input(collection_finder):
    with patch.object(collection_finder, '_reload_hack') as mock_reload_hack:
        collection_finder.set_playbook_paths('path1')
        assert collection_finder._n_playbook_paths == [os.path.join('path1', 'collections')]
        assert collection_finder._n_cached_collection_paths is None
        mock_reload_hack.assert_has_calls([call('ansible_collections'), call('ansible_collections.ansible')])

def test_set_playbook_paths_list_input(collection_finder):
    with patch.object(collection_finder, '_reload_hack') as mock_reload_hack:
        collection_finder.set_playbook_paths(['path1', 'path2'])
        expected_paths = [os.path.join('path1', 'collections'), os.path.join('path2', 'collections')]
        assert collection_finder._n_playbook_paths == expected_paths
        assert collection_finder._n_cached_collection_paths is None
        mock_reload_hack.assert_has_calls([call('ansible_collections'), call('ansible_collections.ansible')])

def test_set_playbook_paths_with_duplicates(collection_finder):
    with patch.object(collection_finder, '_reload_hack') as mock_reload_hack:
        collection_finder.set_playbook_paths(['path1', 'path1'])
        expected_paths = [os.path.join('path1', 'collections')]
        assert collection_finder._n_playbook_paths == expected_paths
        assert collection_finder._n_cached_collection_paths is None
        mock_reload_hack.assert_has_calls([call('ansible_collections'), call('ansible_collections.ansible')])
