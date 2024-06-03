# file lib/ansible/executor/discovery/python_target.py:16-22
# lines [16, 17, 18, 19, 20, 22]
# branches ['17->18', '17->19']

import os
import io
import pytest
from unittest import mock

# Assuming the function read_utf8_file is imported from ansible.executor.discovery.python_target
from ansible.executor.discovery.python_target import read_utf8_file

def test_read_utf8_file_no_access(mocker):
    # Mock os.access to return False
    mocker.patch('os.access', return_value=False)
    
    result = read_utf8_file('dummy_path')
    
    assert result is None

def test_read_utf8_file_with_access(mocker):
    # Mock os.access to return True
    mocker.patch('os.access', return_value=True)
    
    # Mock the content of the file
    mock_content = 'test content'
    
    # Use mock_open to mock the open function
    mock_open = mocker.patch('io.open', mock.mock_open(read_data=mock_content))
    
    result = read_utf8_file('dummy_path')
    
    # Ensure the file was opened with the correct parameters
    mock_open.assert_called_once_with('dummy_path', 'r', encoding='utf-8')
    
    assert result == mock_content

