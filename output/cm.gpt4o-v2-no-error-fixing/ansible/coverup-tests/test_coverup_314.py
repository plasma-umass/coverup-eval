# file: lib/ansible/executor/discovery/python_target.py:16-22
# asked: {"lines": [16, 17, 18, 19, 20, 22], "branches": [[17, 18], [17, 19]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22], "branches": [[17, 18], [17, 19]]}

import io
import os
import pytest

from ansible.executor.discovery.python_target import read_utf8_file

def test_read_utf8_file_no_access(monkeypatch):
    def mock_access(path, mode):
        return False

    monkeypatch.setattr(os, 'access', mock_access)
    result = read_utf8_file('dummy_path')
    assert result is None

def test_read_utf8_file_with_access(monkeypatch):
    def mock_access(path, mode):
        return True

    def mock_open(path, mode, encoding):
        return io.StringIO("file content")

    monkeypatch.setattr(os, 'access', mock_access)
    monkeypatch.setattr(io, 'open', mock_open)
    result = read_utf8_file('dummy_path')
    assert result == "file content"
