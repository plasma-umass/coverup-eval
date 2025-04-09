# file lib/ansible/parsing/dataloader.py:108-110
# lines [108, 109, 110]
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

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

def test_path_exists(mock_path_dwim, mock_to_bytes, mock_os_path_exists):
    loader = DataLoader()
    
    # Mock the path_dwim method to return a specific path
    mock_path_dwim.return_value = '/mocked/path'
    
    # Mock the to_bytes function to return a byte string
    mock_to_bytes.return_value = b'/mocked/path'
    
    # Mock os.path.exists to return True
    mock_os_path_exists.return_value = True
    
    # Call the method under test
    result = loader.path_exists('/some/path')
    
    # Verify the mocks were called with expected arguments
    mock_path_dwim.assert_called_once_with('/some/path')
    mock_to_bytes.assert_called_once_with('/mocked/path', errors='surrogate_or_strict')
    mock_os_path_exists.assert_called_once_with(b'/mocked/path')
    
    # Assert the result is True
    assert result is True

    # Mock os.path.exists to return False
    mock_os_path_exists.return_value = False
    
    # Call the method under test again
    result = loader.path_exists('/some/other/path')
    
    # Verify the mocks were called with expected arguments
    mock_path_dwim.assert_called_with('/some/other/path')
    mock_to_bytes.assert_called_with('/mocked/path', errors='surrogate_or_strict')
    mock_os_path_exists.assert_called_with(b'/mocked/path')
    
    # Assert the result is False
    assert result is False
