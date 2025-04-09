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
    burp('-', 'test content')
    mock_stdout.write.assert_called_once_with('test content')

def test_burp_write_to_file(tmp_path):
    test_file = tmp_path / "testfile.txt"
    burp(str(test_file), 'test content')
    with open(test_file, 'r') as f:
        assert f.read() == 'test content'

def test_burp_expanduser(tmp_path, monkeypatch):
    test_file = tmp_path / "testfile.txt"
    monkeypatch.setattr(os.path, 'expanduser', lambda x: str(test_file))
    burp('~testfile.txt', 'test content', expanduser=True)
    with open(test_file, 'r') as f:
        assert f.read() == 'test content'

def test_burp_expandvars(tmp_path, monkeypatch):
    test_file = tmp_path / "testfile.txt"
    monkeypatch.setattr(os.path, 'expandvars', lambda x: str(test_file))
    burp('$TESTFILE', 'test content', expandvars=True)
    with open(test_file, 'r') as f:
        assert f.read() == 'test content'

def test_burp_no_expanduser(tmp_path):
    test_file = tmp_path / "testfile.txt"
    burp(str(test_file), 'test content', expanduser=False)
    with open(test_file, 'r') as f:
        assert f.read() == 'test content'

def test_burp_no_expandvars(tmp_path):
    test_file = tmp_path / "testfile.txt"
    burp(str(test_file), 'test content', expandvars=False)
    with open(test_file, 'r') as f:
        assert f.read() == 'test content'
