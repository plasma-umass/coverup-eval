# file lib/ansible/utils/collection_loader/_collection_finder.py:165-179
# lines [166, 167, 170, 173, 174, 178, 179]
# branches ['166->167', '166->170', '178->exit', '178->179']

import os
import pytest
from ansible.utils.collection_loader import _collection_finder
from unittest.mock import call

@pytest.fixture
def ansible_collection_finder():
    return _collection_finder._AnsibleCollectionFinder()

@pytest.fixture
def mock_os_path_join(mocker):
    return mocker.patch('os.path.join', side_effect=lambda x, y: f"{x}/{y}")

@pytest.fixture
def mock_to_native(mocker):
    return mocker.patch('ansible.utils.collection_loader._collection_finder.to_native', side_effect=lambda x: x)

@pytest.fixture
def mock_reload_hack(ansible_collection_finder, mocker):
    return mocker.patch.object(ansible_collection_finder, '_reload_hack')

def test_set_playbook_paths_with_string(ansible_collection_finder, mock_os_path_join, mock_to_native, mock_reload_hack):
    playbook_path = '/path/to/playbook'
    ansible_collection_finder.set_playbook_paths(playbook_path)
    
    mock_os_path_join.assert_called_once_with(playbook_path, 'collections')
    mock_to_native.assert_called_once_with(playbook_path)
    mock_reload_hack.assert_has_calls([
        call('ansible_collections'),
        call('ansible_collections.ansible')
    ])
    assert ansible_collection_finder._n_playbook_paths == [f"{playbook_path}/collections"]
    assert ansible_collection_finder._n_cached_collection_paths is None

def test_set_playbook_paths_with_list(ansible_collection_finder, mock_os_path_join, mock_to_native, mock_reload_hack):
    playbook_paths = ['/path/to/playbook1', '/path/to/playbook2', '/path/to/playbook1']
    ansible_collection_finder.set_playbook_paths(playbook_paths)
    
    expected_calls = [call(playbook_paths[0], 'collections'), call(playbook_paths[1], 'collections')]
    mock_os_path_join.assert_has_calls(expected_calls, any_order=True)
    assert mock_os_path_join.call_count == 2
    assert mock_to_native.call_count == 2
    mock_reload_hack.assert_has_calls([
        call('ansible_collections'),
        call('ansible_collections.ansible')
    ])
    assert ansible_collection_finder._n_playbook_paths == [f"{playbook_paths[0]}/collections", f"{playbook_paths[1]}/collections"]
    assert ansible_collection_finder._n_cached_collection_paths is None
