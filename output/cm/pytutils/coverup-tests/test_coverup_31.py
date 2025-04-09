# file pytutils/files.py:55-68
# lines [55, 59, 60, 62, 63, 64, 65, 67, 68]
# branches ['59->60', '59->62', '62->63', '62->64', '64->65', '64->67']

import os
import sys
import pytest
from pytutils.files import burp

def test_burp_to_stdout(mocker):
    # Mock sys.stdout.write to verify it's called with correct content
    mock_stdout_write = mocker.patch('sys.stdout.write')

    # Call burp with '-' as filename to write to stdout
    burp('-', 'test content')

    # Verify that sys.stdout.write was called with 'test content'
    mock_stdout_write.assert_called_once_with('test content')

def test_burp_to_file_with_expansion(mocker, tmp_path):
    # Mock os.path.expanduser and os.path.expandvars to verify they are called
    mock_expanduser = mocker.patch('os.path.expanduser')
    mock_expandvars = mocker.patch('os.path.expandvars')

    # Set the return value for expanduser and expandvars to the tmp_path
    test_file_path = str(tmp_path / 'testfile')
    mock_expanduser.return_value = test_file_path
    mock_expandvars.return_value = test_file_path

    # Create a test file path
    test_file = tmp_path / 'testfile'

    # Call burp with a filename that requires user and vars expansion
    burp('~/testfile', 'test content', expanduser=True, expandvars=True)

    # Verify that the file was created and contains the correct content
    assert test_file.read_text() == 'test content'

    # Verify that expanduser and expandvars were called with the original path
    mock_expanduser.assert_called_once_with('~/testfile')
    mock_expandvars.assert_called_once_with(test_file_path)

def test_burp_to_file_without_expansion(mocker, tmp_path):
    # Create a test file path
    test_file = tmp_path / 'testfile'

    # Call burp with a filename without requiring user and vars expansion
    burp(str(test_file), 'test content', expanduser=False, expandvars=False)

    # Verify that the file was created and contains the correct content
    assert test_file.read_text() == 'test content'
