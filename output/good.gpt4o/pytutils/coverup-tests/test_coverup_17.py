# file pytutils/files.py:55-68
# lines [55, 59, 60, 62, 63, 64, 65, 67, 68]
# branches ['59->60', '59->62', '62->63', '62->64', '64->65', '64->67']

import os
import sys
import pytest
from unittest import mock
from pytutils.files import burp

def test_burp_write_to_stdout(mocker):
    mock_stdout = mocker.patch('sys.stdout.write')
    burp('-', 'test content', allow_stdout=True)
    mock_stdout.assert_called_once_with('test content')

def test_burp_expanduser(mocker):
    mock_expanduser = mocker.patch('os.path.expanduser', return_value='/mocked/path')
    mock_open = mocker.patch('builtins.open', mock.mock_open())
    burp('~/testfile', 'test content', expanduser=True)
    mock_expanduser.assert_called_once_with('~/testfile')
    mock_open.assert_called_once_with('/mocked/path', 'w')
    mock_open().write.assert_called_once_with('test content')

def test_burp_expandvars(mocker):
    mock_expandvars = mocker.patch('os.path.expandvars', return_value='/mocked/path')
    mock_open = mocker.patch('builtins.open', mock.mock_open())
    burp('$HOME/testfile', 'test content', expandvars=True)
    mock_expandvars.assert_called_once_with('$HOME/testfile')
    mock_open.assert_called_once_with('/mocked/path', 'w')
    mock_open().write.assert_called_once_with('test content')

def test_burp_no_expanduser_no_expandvars(mocker):
    mock_open = mocker.patch('builtins.open', mock.mock_open())
    burp('/testfile', 'test content', expanduser=False, expandvars=False)
    mock_open.assert_called_once_with('/testfile', 'w')
    mock_open().write.assert_called_once_with('test content')
