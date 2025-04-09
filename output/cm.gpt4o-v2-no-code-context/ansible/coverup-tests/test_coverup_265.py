# file: lib/ansible/module_utils/facts/system/distribution.py:30-44
# asked: {"lines": [30, 32, 33, 36, 37, 40, 41, 44], "branches": [[32, 33], [32, 36], [36, 37], [36, 40], [40, 41], [40, 44]]}
# gained: {"lines": [30, 32, 33, 36, 37, 40, 41, 44], "branches": [[32, 33], [32, 36], [36, 37], [36, 40], [40, 41], [40, 44]]}

import os
import pytest
from unittest import mock

# Assuming the function _file_exists is part of a class or module, we need to import it correctly.
# For the sake of this example, let's assume it's a standalone function in a module named 'distribution'.
from ansible.module_utils.facts.system.distribution import _file_exists

def test_file_exists_path_does_not_exist(monkeypatch):
    def mock_exists(path):
        return False

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    assert _file_exists('/non/existent/path') is False

def test_file_exists_path_exists_allow_empty(monkeypatch):
    def mock_exists(path):
        return True

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    assert _file_exists('/existent/path', allow_empty=True) is True

def test_file_exists_path_exists_not_allow_empty_empty_file(monkeypatch):
    def mock_exists(path):
        return True

    def mock_getsize(path):
        return 0

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(os.path, 'getsize', mock_getsize)
    assert _file_exists('/existent/empty/file', allow_empty=False) is False

def test_file_exists_path_exists_not_allow_empty_non_empty_file(monkeypatch):
    def mock_exists(path):
        return True

    def mock_getsize(path):
        return 100

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    monkeypatch.setattr(os.path, 'getsize', mock_getsize)
    assert _file_exists('/existent/non_empty/file', allow_empty=False) is True
