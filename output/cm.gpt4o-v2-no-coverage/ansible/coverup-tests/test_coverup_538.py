# file: lib/ansible/executor/discovery/python_target.py:16-22
# asked: {"lines": [16, 17, 18, 19, 20, 22], "branches": [[17, 18], [17, 19]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22], "branches": [[17, 18], [17, 19]]}

import pytest
import io
import os
from unittest.mock import mock_open, patch

from ansible.executor.discovery.python_target import read_utf8_file

def test_read_utf8_file_no_access(monkeypatch):
    def mock_access(path, mode):
        return False

    monkeypatch.setattr(os, 'access', mock_access)
    result = read_utf8_file('fake_path')
    assert result is None

def test_read_utf8_file_success(monkeypatch):
    mock_file_content = 'test content'
    
    def mock_access(path, mode):
        return True

    monkeypatch.setattr(os, 'access', mock_access)
    with patch('io.open', mock_open(read_data=mock_file_content)) as mock_file:
        result = read_utf8_file('fake_path')
        mock_file.assert_called_once_with('fake_path', 'r', encoding='utf-8')
        assert result == mock_file_content
