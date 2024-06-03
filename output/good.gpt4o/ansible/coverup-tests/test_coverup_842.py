# file lib/ansible/plugins/filter/core.py:108-110
# lines [108, 110]
# branches []

import pytest
import os
import glob
from unittest.mock import patch

# Assuming the function fileglob is imported from ansible.plugins.filter.core
from ansible.plugins.filter.core import fileglob

@pytest.fixture
def mock_glob(mocker):
    mock_glob = mocker.patch('glob.glob')
    mock_glob.return_value = ['/path/to/file1.txt', '/path/to/dir', '/path/to/file2.txt']
    return mock_glob

@pytest.fixture
def mock_isfile(mocker):
    mock_isfile = mocker.patch('os.path.isfile')
    mock_isfile.side_effect = lambda x: x.endswith('.txt')
    return mock_isfile

def test_fileglob(mock_glob, mock_isfile):
    result = fileglob('/path/to/*')
    assert result == ['/path/to/file1.txt', '/path/to/file2.txt']
    mock_glob.assert_called_once_with('/path/to/*')
    assert mock_isfile.call_count == 3
