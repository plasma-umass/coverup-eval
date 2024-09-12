# file: pytutils/files.py:55-68
# asked: {"lines": [55, 59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [55, 59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [64, 65]]}

import os
import sys
import pytest
from unittest import mock
from pytutils.files import burp

def test_burp_stdout(monkeypatch):
    mock_stdout = mock.Mock()
    monkeypatch.setattr(sys, 'stdout', mock_stdout)
    burp('-', 'test content')
    mock_stdout.write.assert_called_once_with('test content')

def test_burp_expanduser(tmp_path):
    test_file = tmp_path / "testfile.txt"
    with mock.patch('os.path.expanduser', return_value=str(test_file)) as mock_expanduser:
        burp('~testfile.txt', 'test content', expanduser=True)
        mock_expanduser.assert_called_once_with('~testfile.txt')
        with open(test_file, 'r') as f:
            assert f.read() == 'test content'

def test_burp_expandvars(tmp_path, monkeypatch):
    test_file = tmp_path / "testfile.txt"
    monkeypatch.setenv('TESTFILE', str(test_file))
    with mock.patch('os.path.expandvars', return_value=str(test_file)) as mock_expandvars:
        burp('$TESTFILE', 'test content', expandvars=True)
        mock_expandvars.assert_called_once_with('$TESTFILE')
        with open(test_file, 'r') as f:
            assert f.read() == 'test content'

def test_burp_write_file(tmp_path):
    test_file = tmp_path / "testfile.txt"
    burp(str(test_file), 'test content')
    with open(test_file, 'r') as f:
        assert f.read() == 'test content'
