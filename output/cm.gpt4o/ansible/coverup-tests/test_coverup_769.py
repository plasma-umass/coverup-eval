# file lib/ansible/parsing/dataloader.py:124-127
# lines [124, 126, 127]
# branches []

import pytest
import os
from unittest.mock import patch
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def mock_path_dwim(mocker):
    return mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim')

@pytest.fixture
def mock_is_executable(mocker):
    return mocker.patch('ansible.parsing.dataloader.is_executable')

def test_is_executable(mock_path_dwim, mock_is_executable):
    loader = DataLoader()
    test_path = '/fake/path/to/executable'
    dwim_path = '/resolved/path/to/executable'
    
    mock_path_dwim.return_value = dwim_path
    mock_is_executable.return_value = True
    
    result = loader.is_executable(test_path)
    
    mock_path_dwim.assert_called_once_with(test_path)
    mock_is_executable.assert_called_once_with(dwim_path)
    assert result is True
