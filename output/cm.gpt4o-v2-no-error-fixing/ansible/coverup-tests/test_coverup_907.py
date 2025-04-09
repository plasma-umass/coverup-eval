# file: lib/ansible/config/manager.py:49-158
# asked: {"lines": [78, 116], "branches": [[77, 78], [115, 116]]}
# gained: {"lines": [78], "branches": [[77, 78]]}

import os
import pytest
import tempfile
from ansible.config.manager import ensure_type
from ansible.utils.path import makedirs_safe

def test_ensure_type_basedir(monkeypatch):
    # Create a temporary directory to act as the origin
    with tempfile.TemporaryDirectory() as tempdir:
        tempdir = os.path.abspath(tempdir)
        
        # Ensure the basedir is set correctly
        result = ensure_type("some_value", "string", origin=tempdir)
        assert result == "some_value"

def test_ensure_type_tmppath(monkeypatch):
    # Create a temporary directory to act as the base directory
    with tempfile.TemporaryDirectory() as tempdir:
        tempdir = os.path.abspath(tempdir)
        
        # Ensure the temporary path is created correctly
        result = ensure_type(tempdir, "tmppath")
        assert os.path.exists(result)
        assert result.startswith(tempdir)
        assert os.path.isdir(result)
        
        # Clean up the created temporary directory
        os.rmdir(result)
