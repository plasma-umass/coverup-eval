# file: lib/ansible/plugins/filter/core.py:108-110
# asked: {"lines": [108, 110], "branches": []}
# gained: {"lines": [108, 110], "branches": []}

import pytest
import glob
import os

# Mocking glob.glob and os.path.isfile
@pytest.fixture
def mock_glob_isfile(mocker):
    mock_glob = mocker.patch('glob.glob')
    mock_isfile = mocker.patch('os.path.isfile')
    return mock_glob, mock_isfile

def test_fileglob_no_match(mock_glob_isfile):
    mock_glob, mock_isfile = mock_glob_isfile
    mock_glob.return_value = []
    mock_isfile.return_value = False

    from ansible.plugins.filter.core import fileglob
    result = fileglob('*.txt')
    assert result == []

def test_fileglob_with_match(mock_glob_isfile):
    mock_glob, mock_isfile = mock_glob_isfile
    mock_glob.return_value = ['file1.txt', 'file2.txt']
    mock_isfile.side_effect = lambda x: x == 'file1.txt'

    from ansible.plugins.filter.core import fileglob
    result = fileglob('*.txt')
    assert result == ['file1.txt']
