# file: lib/ansible/executor/discovery/python_target.py:16-22
# asked: {"lines": [16, 17, 18, 19, 20, 22], "branches": [[17, 18], [17, 19]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22], "branches": [[17, 18], [17, 19]]}

import os
import io
import pytest
from unittest import mock

# Assuming the function is imported from the module
from ansible.executor.discovery.python_target import read_utf8_file

def test_read_utf8_file_no_access(monkeypatch):
    path = 'fake_path.txt'
    
    def mock_access(path, mode):
        return False
    
    monkeypatch.setattr(os, 'access', mock_access)
    
    result = read_utf8_file(path)
    assert result is None

def test_read_utf8_file_success(monkeypatch):
    path = 'fake_path.txt'
    content = 'This is a test content.'

    def mock_access(path, mode):
        return True

    def mock_open(*args, **kwargs):
        return mock.mock_open(read_data=content).return_value

    monkeypatch.setattr(os, 'access', mock_access)
    monkeypatch.setattr(io, 'open', mock_open)

    result = read_utf8_file(path)
    assert result == content

def test_read_utf8_file_different_encoding(monkeypatch):
    path = 'fake_path.txt'
    content = 'This is a test content with different encoding.'

    def mock_access(path, mode):
        return True

    def mock_open(*args, **kwargs):
        return mock.mock_open(read_data=content).return_value

    monkeypatch.setattr(os, 'access', mock_access)
    monkeypatch.setattr(io, 'open', mock_open)

    result = read_utf8_file(path, encoding='utf-16')
    assert result == content
