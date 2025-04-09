# file lib/ansible/module_utils/facts/utils.py:23-60
# lines [42, 43, 52, 54, 56]
# branches ['34->60', '48->51', '51->52']

import os
import fcntl
import pytest
from unittest import mock
from ansible.module_utils.facts.utils import get_file_content

def test_get_file_content(mocker):
    # Mock os.path.exists to return True
    mocker.patch('os.path.exists', return_value=True)
    # Mock os.access to return True
    mocker.patch('os.access', return_value=True)
    
    # Create a mock for open
    mock_open = mock.mock_open(read_data=" test content ")
    mocker.patch('builtins.open', mock_open)
    
    # Mock fcntl.fcntl to raise an exception on the first call
    def mock_fcntl(fd, op, arg=None):
        if op == fcntl.F_GETFL:
            raise Exception("Mocked exception")
        return 0
    
    mocker.patch('fcntl.fcntl', side_effect=mock_fcntl)
    
    # Test with strip=True
    result = get_file_content('/fake/path', default='default content', strip=True)
    assert result == 'test content'
    
    # Test with strip=False
    result = get_file_content('/fake/path', default='default content', strip=False)
    assert result == ' test content '
    
    # Test with empty file content
    mock_open = mock.mock_open(read_data="")
    mocker.patch('builtins.open', mock_open)
    
    result = get_file_content('/fake/path', default='default content', strip=True)
    assert result == 'default content'
    
    # Test with file not existing
    mocker.patch('os.path.exists', return_value=False)
    
    result = get_file_content('/fake/path', default='default content', strip=True)
    assert result == 'default content'
    
    # Test with file not accessible
    mocker.patch('os.access', return_value=False)
    
    result = get_file_content('/fake/path', default='default content', strip=True)
    assert result == 'default content'
