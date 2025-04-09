# file: lib/ansible/executor/discovery/python_target.py:16-22
# asked: {"lines": [16, 17, 18, 19, 20, 22], "branches": [[17, 18], [17, 19]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22], "branches": [[17, 18], [17, 19]]}

import os
import io
import pytest

from ansible.executor.discovery.python_target import read_utf8_file

def test_read_utf8_file_success(monkeypatch):
    test_path = 'test_file.txt'
    test_content = 'Hello, World!'

    def mock_open(*args, **kwargs):
        if args[0] == test_path:
            return io.StringIO(test_content)
        return open(*args, **kwargs)

    monkeypatch.setattr(io, 'open', mock_open)
    monkeypatch.setattr(os, 'access', lambda path, mode: True)

    result = read_utf8_file(test_path)
    assert result == test_content

def test_read_utf8_file_no_access(monkeypatch):
    test_path = 'test_file.txt'

    monkeypatch.setattr(os, 'access', lambda path, mode: False)

    result = read_utf8_file(test_path)
    assert result is None
