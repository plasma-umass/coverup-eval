# file: lib/ansible/parsing/dataloader.py:116-118
# asked: {"lines": [117, 118], "branches": []}
# gained: {"lines": [117, 118], "branches": []}

import os
import pytest
from unittest.mock import patch
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_is_directory_with_dwim_path(mocker, dataloader):
    # Mock the path_dwim method to return a specific path
    mocker.patch.object(dataloader, 'path_dwim', return_value='/mocked/path')
    # Mock os.path.isdir to return True
    mocker.patch('os.path.isdir', return_value=True)
    # Mock to_bytes to return the same path
    mocker.patch('ansible.parsing.dataloader.to_bytes', return_value=b'/mocked/path')

    result = dataloader.is_directory('/some/path')
    
    # Assert that path_dwim was called with the original path
    dataloader.path_dwim.assert_called_once_with('/some/path')
    # Assert that os.path.isdir was called with the mocked byte path
    os.path.isdir.assert_called_once_with(b'/mocked/path')
    # Assert the result is True
    assert result is True

def test_is_directory_with_non_directory(mocker, dataloader):
    # Mock the path_dwim method to return a specific path
    mocker.patch.object(dataloader, 'path_dwim', return_value='/mocked/path')
    # Mock os.path.isdir to return False
    mocker.patch('os.path.isdir', return_value=False)
    # Mock to_bytes to return the same path
    mocker.patch('ansible.parsing.dataloader.to_bytes', return_value=b'/mocked/path')

    result = dataloader.is_directory('/some/path')
    
    # Assert that path_dwim was called with the original path
    dataloader.path_dwim.assert_called_once_with('/some/path')
    # Assert that os.path.isdir was called with the mocked byte path
    os.path.isdir.assert_called_once_with(b'/mocked/path')
    # Assert the result is False
    assert result is False
