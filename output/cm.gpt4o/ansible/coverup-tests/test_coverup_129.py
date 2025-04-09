# file lib/ansible/collections/list.py:20-47
# lines [20, 28, 29, 31, 33, 35, 36, 38, 39, 40, 42, 43, 44, 45, 47]
# branches ['28->29', '28->31', '33->exit', '33->35', '36->38', '36->42', '38->39', '38->40', '42->43', '42->47', '43->44', '43->45']

import os
import pytest
from unittest import mock
from ansible.collections.list import list_valid_collection_paths

@pytest.fixture
def mock_ansible_collection_config(mocker):
    class MockAnsibleCollectionConfig:
        collection_paths = ['/default/path']

    mocker.patch('ansible.collections.list.AnsibleCollectionConfig', MockAnsibleCollectionConfig)

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.collections.list.display')

@pytest.fixture
def mock_to_bytes(mocker):
    return mocker.patch('ansible.collections.list.to_bytes', side_effect=lambda x: x.encode('utf-8'))

def test_list_valid_collection_paths_no_search_paths(mock_ansible_collection_config, mock_display, mock_to_bytes):
    with mock.patch('os.path.exists', return_value=False):
        with mock.patch('os.path.isdir', return_value=False):
            result = list(list_valid_collection_paths(warn=True))
            assert result == []

def test_list_valid_collection_paths_with_search_paths(mock_ansible_collection_config, mock_display, mock_to_bytes):
    search_paths = ['/valid/path', '/invalid/path']
    
    def mock_exists(path):
        return path == b'/valid/path'
    
    def mock_isdir(path):
        return path == b'/valid/path'
    
    with mock.patch('os.path.exists', side_effect=mock_exists):
        with mock.patch('os.path.isdir', side_effect=mock_isdir):
            result = list(list_valid_collection_paths(search_paths, warn=True))
            assert result == ['/valid/path']

def test_list_valid_collection_paths_warn_on_missing(mock_ansible_collection_config, mock_display, mock_to_bytes):
    search_paths = ['/missing/path']
    
    with mock.patch('os.path.exists', return_value=False):
        with mock.patch('os.path.isdir', return_value=False):
            result = list(list_valid_collection_paths(search_paths, warn=True))
            assert result == []
            mock_display.warning.assert_any_call("The configured collection path /missing/path does not exist.")

def test_list_valid_collection_paths_warn_on_not_directory(mock_ansible_collection_config, mock_display, mock_to_bytes):
    search_paths = ['/not_a_directory']
    
    with mock.patch('os.path.exists', return_value=True):
        with mock.patch('os.path.isdir', return_value=False):
            result = list(list_valid_collection_paths(search_paths, warn=True))
            assert result == []
            mock_display.warning.assert_any_call("The configured collection path /not_a_directory, exists, but it is not a directory.")
