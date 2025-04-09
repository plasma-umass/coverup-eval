# file: lib/ansible/module_utils/facts/utils.py:23-60
# asked: {"lines": [23, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 46, 48, 49, 51, 52, 54, 56, 58, 60], "branches": [[34, 35], [34, 60], [48, 49], [48, 51], [51, 52], [51, 58]]}
# gained: {"lines": [23, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 46, 48, 49, 51, 52, 54, 56, 58, 60], "branches": [[34, 35], [34, 60], [48, 49], [48, 51], [51, 52], [51, 58]]}

import os
import fcntl
import pytest
from ansible.module_utils.facts.utils import get_file_content

def test_get_file_content_file_exists_and_readable(monkeypatch, tmp_path):
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("  test content  ")

    assert get_file_content(str(test_file)) == "test content"

def test_get_file_content_file_exists_and_readable_no_strip(monkeypatch, tmp_path):
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("  test content  ")

    assert get_file_content(str(test_file), strip=False) == "  test content  "

def test_get_file_content_file_exists_and_readable_empty(monkeypatch, tmp_path):
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("")

    assert get_file_content(str(test_file), default="default content") == "default content"

def test_get_file_content_file_not_exists(monkeypatch):
    assert get_file_content("/non/existent/path", default="default content") == "default content"

def test_get_file_content_file_not_readable(monkeypatch, tmp_path):
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("test content")
    test_file.chmod(0o000)  # Make file not readable

    def mock_access(path, mode):
        return False

    monkeypatch.setattr(os, 'access', mock_access)

    assert get_file_content(str(test_file), default="default content") == "default content"

def test_get_file_content_fcntl_exception(monkeypatch, tmp_path):
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("test content")

    def mock_fcntl(*args, **kwargs):
        raise Exception("mock fcntl exception")

    monkeypatch.setattr(fcntl, 'fcntl', mock_fcntl)

    assert get_file_content(str(test_file)) == "test content"

def test_get_file_content_read_exception(monkeypatch, tmp_path):
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("test content")

    class MockFile:
        def __init__(self, *args, **kwargs):
            pass

        def fileno(self):
            return 1

        def read(self):
            raise Exception("mock read exception")

        def close(self):
            pass

    monkeypatch.setattr("builtins.open", lambda *args, **kwargs: MockFile())
    assert get_file_content(str(test_file), default="default content") == "default content"
