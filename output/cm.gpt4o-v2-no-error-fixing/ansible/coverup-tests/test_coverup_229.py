# file: lib/ansible/utils/collection_loader/_collection_finder.py:165-179
# asked: {"lines": [165, 166, 167, 170, 173, 174, 178, 179], "branches": [[166, 167], [166, 170], [178, 0], [178, 179]]}
# gained: {"lines": [165, 166, 167, 170, 173, 174, 178, 179], "branches": [[166, 167], [166, 170], [178, 0], [178, 179]]}

import pytest
import os
import sys
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

@pytest.fixture
def collection_finder():
    return _AnsibleCollectionFinder()

def test_set_playbook_paths_string(collection_finder, monkeypatch):
    playbook_path = "/path/to/playbook"
    expected_path = os.path.join(playbook_path, 'collections')

    monkeypatch.setattr(sys, 'modules', {'ansible_collections': MagicMock(), 'ansible_collections.ansible': MagicMock()})
    with patch.object(collection_finder, '_reload_hack') as mock_reload_hack:
        collection_finder.set_playbook_paths(playbook_path)
        assert collection_finder._n_playbook_paths == [expected_path]
        assert collection_finder._n_cached_collection_paths is None
        mock_reload_hack.assert_any_call('ansible_collections')
        mock_reload_hack.assert_any_call('ansible_collections.ansible')

def test_set_playbook_paths_list(collection_finder, monkeypatch):
    playbook_paths = ["/path/to/playbook1", "/path/to/playbook2"]
    expected_paths = [os.path.join(p, 'collections') for p in playbook_paths]

    monkeypatch.setattr(sys, 'modules', {'ansible_collections': MagicMock(), 'ansible_collections.ansible': MagicMock()})
    with patch.object(collection_finder, '_reload_hack') as mock_reload_hack:
        collection_finder.set_playbook_paths(playbook_paths)
        assert collection_finder._n_playbook_paths == expected_paths
        assert collection_finder._n_cached_collection_paths is None
        mock_reload_hack.assert_any_call('ansible_collections')
        mock_reload_hack.assert_any_call('ansible_collections.ansible')

def test_set_playbook_paths_with_duplicates(collection_finder, monkeypatch):
    playbook_paths = ["/path/to/playbook1", "/path/to/playbook1"]
    expected_paths = [os.path.join(playbook_paths[0], 'collections')]

    monkeypatch.setattr(sys, 'modules', {'ansible_collections': MagicMock(), 'ansible_collections.ansible': MagicMock()})
    with patch.object(collection_finder, '_reload_hack') as mock_reload_hack:
        collection_finder.set_playbook_paths(playbook_paths)
        assert collection_finder._n_playbook_paths == expected_paths
        assert collection_finder._n_cached_collection_paths is None
        mock_reload_hack.assert_any_call('ansible_collections')
        mock_reload_hack.assert_any_call('ansible_collections.ansible')
