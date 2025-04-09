# file: pytutils/files.py:55-68
# asked: {"lines": [55, 59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [55, 59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

import os
import sys
import pytest
from unittest import mock
from pytutils.files import burp

def test_burp_write_to_stdout(monkeypatch):
    mock_stdout = mock.Mock()
    monkeypatch.setattr(sys, 'stdout', mock_stdout)
    burp('-', 'test content', allow_stdout=True)
    mock_stdout.write.assert_called_once_with('test content')

def test_burp_expanduser_and_expandvars(tmp_path):
    filename = str(tmp_path / 'testfile.txt')
    with mock.patch('os.path.expanduser', side_effect=os.path.expanduser) as mock_expanduser, \
         mock.patch('os.path.expandvars', side_effect=os.path.expandvars) as mock_expandvars:
        burp(filename, 'test content', expanduser=True, expandvars=True)
        mock_expanduser.assert_called_once_with(filename)
        mock_expandvars.assert_called_once_with(filename)
        with open(filename, 'r') as f:
            assert f.read() == 'test content'

def test_burp_no_expanduser(tmp_path):
    filename = str(tmp_path / 'testfile.txt')
    with mock.patch('os.path.expanduser') as mock_expanduser:
        burp(filename, 'test content', expanduser=False)
        mock_expanduser.assert_not_called()
        with open(filename, 'r') as f:
            assert f.read() == 'test content'

def test_burp_no_expandvars(tmp_path):
    filename = str(tmp_path / 'testfile.txt')
    with mock.patch('os.path.expandvars') as mock_expandvars:
        burp(filename, 'test content', expandvars=False)
        mock_expandvars.assert_not_called()
        with open(filename, 'r') as f:
            assert f.read() == 'test content'
