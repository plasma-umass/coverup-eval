# file lib/ansible/parsing/dataloader.py:112-114
# lines [112, 113, 114]
# branches []

import os
import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def mock_path_dwim(mocker):
    return mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim')

@pytest.fixture
def mock_to_bytes(mocker):
    return mocker.patch('ansible.parsing.dataloader.to_bytes')

def test_is_file_with_devnull(mock_path_dwim, mock_to_bytes):
    loader = DataLoader()
    mock_path_dwim.return_value = os.devnull
    mock_to_bytes.return_value = os.devnull.encode()

    assert loader.is_file(os.devnull) is True

def test_is_file_with_nonexistent_file(mock_path_dwim, mock_to_bytes):
    loader = DataLoader()
    non_existent_path = '/non/existent/path'
    mock_path_dwim.return_value = non_existent_path
    mock_to_bytes.return_value = non_existent_path.encode()

    assert loader.is_file(non_existent_path) is False
