# file lib/ansible/parsing/dataloader.py:399-407
# lines [399, 405, 406, 407]
# branches ['405->exit', '405->406']

import os
import pytest
from unittest.mock import patch, MagicMock

from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._tempfiles = []
    return loader

def test_cleanup_tmp_file_removes_temp_file(dataloader, mocker):
    # Create a temporary file
    temp_file = 'temp_file.txt'
    dataloader._tempfiles.append(temp_file)
    
    # Mock os.unlink to avoid actually deleting any files
    mock_unlink = mocker.patch('os.unlink')
    
    # Call the method
    dataloader.cleanup_tmp_file(temp_file)
    
    # Assert the file was removed from _tempfiles
    assert temp_file not in dataloader._tempfiles
    
    # Assert os.unlink was called with the correct file path
    mock_unlink.assert_called_once_with(temp_file)

def test_cleanup_tmp_file_no_action_if_not_in_tempfiles(dataloader, mocker):
    # Create a temporary file that is not in _tempfiles
    temp_file = 'temp_file.txt'
    
    # Mock os.unlink to ensure it is not called
    mock_unlink = mocker.patch('os.unlink')
    
    # Call the method
    dataloader.cleanup_tmp_file(temp_file)
    
    # Assert os.unlink was not called
    mock_unlink.assert_not_called()
