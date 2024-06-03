# file lib/ansible/collections/list.py:20-47
# lines []
# branches ['38->40', '43->45']

import os
import pytest
from unittest import mock
from ansible.collections.list import list_valid_collection_paths

@pytest.fixture
def mock_display_warning(mocker):
    return mocker.patch('ansible.utils.display.Display.warning')

@pytest.fixture
def mock_ansible_collection_config(mocker):
    class MockAnsibleCollectionConfig:
        collection_paths = []
    return mocker.patch('ansible.collections.list.AnsibleCollectionConfig', MockAnsibleCollectionConfig)

def test_list_valid_collection_paths_warn_nonexistent_path(mock_display_warning, mock_ansible_collection_config):
    with mock.patch('os.path.exists', return_value=False):
        search_paths = ['/nonexistent/path']
        result = list(list_valid_collection_paths(search_paths, warn=True))
        assert result == []
        mock_display_warning.assert_called_once_with("The configured collection path /nonexistent/path does not exist.")

def test_list_valid_collection_paths_warn_not_directory(mock_display_warning, mock_ansible_collection_config):
    with mock.patch('os.path.exists', return_value=True), \
         mock.patch('os.path.isdir', return_value=False):
        search_paths = ['/not/a/directory']
        result = list(list_valid_collection_paths(search_paths, warn=True))
        assert result == []
        mock_display_warning.assert_called_once_with("The configured collection path /not/a/directory, exists, but it is not a directory.")

def test_list_valid_collection_paths_no_warn_nonexistent_path(mock_display_warning, mock_ansible_collection_config):
    with mock.patch('os.path.exists', return_value=False):
        search_paths = ['/nonexistent/path']
        result = list(list_valid_collection_paths(search_paths, warn=False))
        assert result == []
        mock_display_warning.assert_not_called()

def test_list_valid_collection_paths_no_warn_not_directory(mock_display_warning, mock_ansible_collection_config):
    with mock.patch('os.path.exists', return_value=True), \
         mock.patch('os.path.isdir', return_value=False):
        search_paths = ['/not/a/directory']
        result = list(list_valid_collection_paths(search_paths, warn=False))
        assert result == []
        mock_display_warning.assert_not_called()
