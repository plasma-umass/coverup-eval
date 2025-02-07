# file: lib/ansible/config/manager.py:49-158
# asked: {"lines": [78, 116], "branches": [[77, 78], [115, 116]]}
# gained: {"lines": [78, 116], "branches": [[77, 78], [115, 116]]}

import os
import pytest
import tempfile
import atexit
from ansible.config.manager import ensure_type
from ansible.utils.path import makedirs_safe, cleanup_tmp_file

def test_ensure_type_basedir(monkeypatch):
    # Setup
    test_origin = tempfile.mkdtemp()
    test_value = "test_value"
    test_value_type = "str"

    # Ensure the directory is cleaned up after the test
    monkeypatch.setattr(atexit, 'register', lambda *args, **kwargs: None)

    # Test
    result = ensure_type(test_value, test_value_type, origin=test_origin)

    # Assert
    assert result == test_value

    # Cleanup
    os.rmdir(test_origin)

def test_ensure_type_tmppath(monkeypatch):
    # Setup
    test_origin = tempfile.mkdtemp()
    test_value = tempfile.mkdtemp(dir=test_origin)
    test_value_type = "tmppath"

    # Ensure the directory is cleaned up after the test
    monkeypatch.setattr(atexit, 'register', lambda *args, **kwargs: None)

    # Test
    result = ensure_type(test_value, test_value_type, origin=test_origin)

    # Assert
    assert os.path.exists(result)
    assert result.startswith(test_value)

    # Cleanup
    cleanup_tmp_file(result)
    os.rmdir(test_value)
    os.rmdir(test_origin)

def test_ensure_type_tmppath_creates_directory(monkeypatch):
    # Setup
    test_origin = tempfile.mkdtemp()
    test_value = os.path.join(test_origin, "non_existent_dir")
    test_value_type = "tmppath"

    # Ensure the directory is cleaned up after the test
    monkeypatch.setattr(atexit, 'register', lambda *args, **kwargs: None)
    monkeypatch.setattr('ansible.utils.path.makedirs_safe', lambda *args, **kwargs: os.makedirs(*args, **kwargs))

    # Test
    result = ensure_type(test_value, test_value_type, origin=test_origin)

    # Assert
    assert os.path.exists(result)
    assert result.startswith(test_value)

    # Cleanup
    cleanup_tmp_file(result)
    os.rmdir(test_value)
    os.rmdir(test_origin)
