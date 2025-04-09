# file: lib/ansible/plugins/filter/core.py:108-110
# asked: {"lines": [108, 110], "branches": []}
# gained: {"lines": [108, 110], "branches": []}

import pytest
import glob
import os
from unittest.mock import patch

# Assuming the fileglob function is defined in ansible/plugins/filter/core.py
from ansible.plugins.filter.core import fileglob

@pytest.fixture
def mock_glob():
    with patch('glob.glob') as mock:
        yield mock

@pytest.fixture
def mock_isfile():
    with patch('os.path.isfile') as mock:
        yield mock

def test_fileglob_no_matches(mock_glob, mock_isfile):
    mock_glob.return_value = []
    result = fileglob('*.txt')
    assert result == []
    mock_glob.assert_called_once_with('*.txt')
    mock_isfile.assert_not_called()

def test_fileglob_with_matches(mock_glob, mock_isfile):
    mock_glob.return_value = ['file1.txt', 'file2.txt', 'dir1']
    mock_isfile.side_effect = lambda x: x != 'dir1'
    result = fileglob('*.txt')
    assert result == ['file1.txt', 'file2.txt']
    mock_glob.assert_called_once_with('*.txt')
    assert mock_isfile.call_count == 3
    mock_isfile.assert_any_call('file1.txt')
    mock_isfile.assert_any_call('file2.txt')
    mock_isfile.assert_any_call('dir1')
