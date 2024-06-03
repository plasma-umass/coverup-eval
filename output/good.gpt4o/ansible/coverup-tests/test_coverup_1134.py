# file lib/ansible/utils/collection_loader/_collection_finder.py:165-179
# lines [166, 167, 170, 173, 174, 178, 179]
# branches ['166->167', '166->170', '178->exit', '178->179']

import os
import pytest
from unittest import mock
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder

@pytest.fixture
def collection_finder():
    return _AnsibleCollectionFinder()

def test_set_playbook_paths_string_type(collection_finder, mocker):
    mocker.patch('ansible.utils.collection_loader._collection_finder._AnsibleCollectionFinder._reload_hack')
    playbook_path = 'test_playbook_path'
    
    collection_finder.set_playbook_paths(playbook_path)
    
    assert collection_finder._n_playbook_paths == [os.path.join(playbook_path, 'collections')]
    assert collection_finder._n_cached_collection_paths is None
    collection_finder._reload_hack.assert_any_call('ansible_collections')
    collection_finder._reload_hack.assert_any_call('ansible_collections.ansible')

def test_set_playbook_paths_list_type(collection_finder, mocker):
    mocker.patch('ansible.utils.collection_loader._collection_finder._AnsibleCollectionFinder._reload_hack')
    playbook_paths = ['test_playbook_path1', 'test_playbook_path2']
    
    collection_finder.set_playbook_paths(playbook_paths)
    
    expected_paths = [os.path.join(p, 'collections') for p in playbook_paths]
    assert collection_finder._n_playbook_paths == expected_paths
    assert collection_finder._n_cached_collection_paths is None
    collection_finder._reload_hack.assert_any_call('ansible_collections')
    collection_finder._reload_hack.assert_any_call('ansible_collections.ansible')
