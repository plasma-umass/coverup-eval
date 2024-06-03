# file lib/ansible/parsing/dataloader.py:120-122
# lines [120, 121, 122]
# branches []

import os
import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def mock_os_listdir(mocker):
    return mocker.patch('os.listdir')

@pytest.fixture
def mock_path_dwim(mocker):
    return mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim')

def test_list_directory(mock_os_listdir, mock_path_dwim):
    # Arrange
    loader = DataLoader()
    test_path = '/some/test/path'
    expected_path = '/some/expected/path'
    expected_files = ['file1.txt', 'file2.txt']
    
    mock_path_dwim.return_value = expected_path
    mock_os_listdir.return_value = expected_files
    
    # Act
    result = loader.list_directory(test_path)
    
    # Assert
    mock_path_dwim.assert_called_once_with(test_path)
    mock_os_listdir.assert_called_once_with(expected_path)
    assert result == expected_files
