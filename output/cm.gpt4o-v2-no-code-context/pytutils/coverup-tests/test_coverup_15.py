# file: pytutils/files.py:55-68
# asked: {"lines": [55, 59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [55, 59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

import os
import sys
import pytest
from unittest import mock
from pytutils.files import burp

def test_burp_write_to_stdout(monkeypatch, capsys):
    # Test writing to stdout
    test_content = "Hello, World!"
    burp('-', test_content)
    captured = capsys.readouterr()
    assert captured.out == test_content

def test_burp_expanduser(mocker):
    # Test expanding user directory
    test_content = "Hello, World!"
    test_filename = '~/testfile.txt'
    expanded_filename = os.path.expanduser(test_filename)
    
    mock_open = mocker.patch("builtins.open", mock.mock_open())
    burp(test_filename, test_content)
    
    mock_open.assert_called_once_with(expanded_filename, 'w')
    mock_open().write.assert_called_once_with(test_content)

def test_burp_expandvars(mocker):
    # Test expanding environment variables
    test_content = "Hello, World!"
    test_filename = '$HOME/testfile.txt'
    expanded_filename = os.path.expandvars(test_filename)
    
    mock_open = mocker.patch("builtins.open", mock.mock_open())
    burp(test_filename, test_content)
    
    mock_open.assert_called_once_with(expanded_filename, 'w')
    mock_open().write.assert_called_once_with(test_content)

def test_burp_no_expanduser(mocker):
    # Test without expanding user directory
    test_content = "Hello, World!"
    test_filename = '~/testfile.txt'
    
    mock_open = mocker.patch("builtins.open", mock.mock_open())
    burp(test_filename, test_content, expanduser=False)
    
    mock_open.assert_called_once_with(test_filename, 'w')
    mock_open().write.assert_called_once_with(test_content)

def test_burp_no_expandvars(mocker):
    # Test without expanding environment variables
    test_content = "Hello, World!"
    test_filename = '$HOME/testfile.txt'
    
    mock_open = mocker.patch("builtins.open", mock.mock_open())
    burp(test_filename, test_content, expandvars=False)
    
    mock_open.assert_called_once_with(test_filename, 'w')
    mock_open().write.assert_called_once_with(test_content)
