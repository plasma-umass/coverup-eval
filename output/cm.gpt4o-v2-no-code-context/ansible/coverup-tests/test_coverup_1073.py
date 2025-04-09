# file: lib/ansible/parsing/dataloader.py:112-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import os
import pytest
from unittest.mock import patch
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_is_file_with_dwim_path(mocker, dataloader):
    # Mock the path_dwim method to return a specific path
    mocker.patch.object(dataloader, 'path_dwim', return_value='/mocked/path')
    # Mock os.path.isfile to return True for the mocked path
    mocker.patch('os.path.isfile', return_value=True)
    # Mock to_bytes to return the same path for simplicity
    mocker.patch('ansible.parsing.dataloader.to_bytes', return_value=b'/mocked/path')

    result = dataloader.is_file('/some/path')
    assert result is True

def test_is_file_with_devnull(mocker, dataloader):
    # Mock the path_dwim method to return os.devnull
    mocker.patch.object(dataloader, 'path_dwim', return_value=os.devnull)
    # Mock os.path.isfile to return False for os.devnull
    mocker.patch('os.path.isfile', return_value=False)
    # Mock to_bytes to return os.devnull for simplicity
    mocker.patch('ansible.parsing.dataloader.to_bytes', return_value=os.devnull.encode())

    result = dataloader.is_file('/some/path')
    assert result is True
