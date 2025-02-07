# file: lib/ansible/module_utils/facts/utils.py:23-60
# asked: {"lines": [41, 52, 54, 56], "branches": [[48, 51], [51, 52]]}
# gained: {"lines": [41, 52], "branches": [[48, 51], [51, 52]]}

import pytest
import os
import tempfile
import fcntl
from unittest import mock
from ansible.module_utils.facts.utils import get_file_content

def test_get_file_content_strip_true():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"  test content  ")
        temp_file_path = temp_file.name

    try:
        result = get_file_content(temp_file_path, strip=True)
        assert result == "test content"
    finally:
        os.remove(temp_file_path)

def test_get_file_content_strip_false():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"  test content  ")
        temp_file_path = temp_file.name

    try:
        result = get_file_content(temp_file_path, strip=False)
        assert result == "  test content  "
    finally:
        os.remove(temp_file_path)

def test_get_file_content_empty_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"")
        temp_file_path = temp_file.name

    try:
        result = get_file_content(temp_file_path, default="default content")
        assert result == "default content"
    finally:
        os.remove(temp_file_path)

def test_get_file_content_no_read_permission(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"test content")
        temp_file_path = temp_file.name

    os.chmod(temp_file_path, 0o000)  # Remove read permissions

    try:
        with mock.patch('os.access', return_value=False):
            result = get_file_content(temp_file_path, default="default content")
            assert result == "default content"
    finally:
        os.chmod(temp_file_path, 0o644)  # Restore permissions so we can delete the file
        os.remove(temp_file_path)

def test_get_file_content_fcntl_exception(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"test content")
        temp_file_path = temp_file.name

    def mock_fcntl(*args, **kwargs):
        raise Exception("Mocked fcntl exception")

    monkeypatch.setattr('fcntl.fcntl', mock_fcntl)

    try:
        result = get_file_content(temp_file_path, strip=True)
        assert result == "test content"
    finally:
        os.remove(temp_file_path)
