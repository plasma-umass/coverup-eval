# file: lib/ansible/parsing/dataloader.py:420-452
# asked: {"lines": [439], "branches": [[438, 439]]}
# gained: {"lines": [439], "branches": [[438, 439]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes

@pytest.fixture
def dataloader():
    return DataLoader()

@pytest.fixture
def mock_path_exists():
    with patch('ansible.parsing.dataloader.DataLoader.path_exists') as mock:
        yield mock

@pytest.fixture
def mock_is_directory():
    with patch('ansible.parsing.dataloader.DataLoader.is_directory') as mock:
        yield mock

@pytest.fixture
def mock_get_dir_vars_files():
    with patch('ansible.parsing.dataloader.DataLoader._get_dir_vars_files') as mock:
        yield mock

def test_find_vars_files_with_extension(dataloader, mock_path_exists, mock_is_directory, mock_get_dir_vars_files):
    path = 'some/path'
    name = 'vars'
    extensions = ['yml', 'yaml']
    
    mock_path_exists.side_effect = lambda x: x.endswith(b'.yml')
    mock_is_directory.return_value = False

    result = dataloader.find_vars_files(path, name, extensions)

    expected_path = to_bytes(os.path.join(path, name)) + b'.yml'
    assert result == [expected_path]
    mock_path_exists.assert_called()
    mock_is_directory.assert_called()

def test_find_vars_files_with_dot_in_extension(dataloader, mock_path_exists, mock_is_directory, mock_get_dir_vars_files):
    path = 'some/path'
    name = 'vars'
    extensions = ['.yml', '.yaml']
    
    mock_path_exists.side_effect = lambda x: x.endswith(b'.yml')
    mock_is_directory.return_value = False

    result = dataloader.find_vars_files(path, name, extensions)

    expected_path = to_bytes(os.path.join(path, name)) + b'.yml'
    assert result == [expected_path]
    mock_path_exists.assert_called()
    mock_is_directory.assert_called()
