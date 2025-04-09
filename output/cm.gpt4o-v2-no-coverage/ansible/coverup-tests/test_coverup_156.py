# file: lib/ansible/module_utils/facts/utils.py:23-60
# asked: {"lines": [23, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 46, 48, 49, 51, 52, 54, 56, 58, 60], "branches": [[34, 35], [34, 60], [48, 49], [48, 51], [51, 52], [51, 58]]}
# gained: {"lines": [23, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 46, 48, 49, 51, 52, 54, 56, 58, 60], "branches": [[34, 35], [34, 60], [48, 49], [48, 51], [51, 52], [51, 58]]}

import pytest
import os
import tempfile
from unittest import mock
import fcntl
from ansible.module_utils.facts.utils import get_file_content

def test_get_file_content_file_exists_and_readable():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"  test content  ")
        temp_file_path = temp_file.name

    try:
        result = get_file_content(temp_file_path, default="default content", strip=True)
        assert result == "test content"
    finally:
        os.remove(temp_file_path)

def test_get_file_content_file_exists_and_readable_no_strip():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"  test content  ")
        temp_file_path = temp_file.name

    try:
        result = get_file_content(temp_file_path, default="default content", strip=False)
        assert result == "  test content  "
    finally:
        os.remove(temp_file_path)

def test_get_file_content_file_exists_but_empty():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"")
        temp_file_path = temp_file.name

    try:
        result = get_file_content(temp_file_path, default="default content", strip=True)
        assert result == "default content"
    finally:
        os.remove(temp_file_path)

def test_get_file_content_file_does_not_exist():
    result = get_file_content("non_existent_file.txt", default="default content", strip=True)
    assert result == "default content"

def test_get_file_content_file_not_readable(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"test content")
        temp_file_path = temp_file.name

    try:
        monkeypatch.setattr(os, 'access', lambda path, mode: False)
        result = get_file_content(temp_file_path, default="default content", strip=True)
        assert result == "default content"
    finally:
        os.remove(temp_file_path)

def test_get_file_content_fcntl_exception(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"test content")
        temp_file_path = temp_file.name

    try:
        def mock_fcntl(*args, **kwargs):
            raise Exception("Mocked fcntl exception")
        
        monkeypatch.setattr('fcntl.fcntl', mock_fcntl)
        result = get_file_content(temp_file_path, default="default content", strip=True)
        assert result == "test content"
    finally:
        os.remove(temp_file_path)

def test_get_file_content_read_exception(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"test content")
        temp_file_path = temp_file.name

    try:
        def mock_read(*args, **kwargs):
            raise Exception("Mocked read exception")
        
        mock_open = mock.mock_open(read_data="test content")
        monkeypatch.setattr('builtins.open', mock_open)
        monkeypatch.setattr(mock_open.return_value, 'read', mock_read)
        result = get_file_content(temp_file_path, default="default content", strip=True)
        assert result == "default content"
    finally:
        os.remove(temp_file_path)
