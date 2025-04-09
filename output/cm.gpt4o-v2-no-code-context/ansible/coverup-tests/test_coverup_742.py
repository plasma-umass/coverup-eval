# file: lib/ansible/plugins/filter/core.py:108-110
# asked: {"lines": [108, 110], "branches": []}
# gained: {"lines": [108, 110], "branches": []}

import pytest
import glob
import os

from ansible.plugins.filter.core import fileglob

@pytest.fixture
def mock_glob(monkeypatch):
    def mock_glob_func(pathname):
        return ['/path/to/file1', '/path/to/dir', '/path/to/file2']
    monkeypatch.setattr(glob, 'glob', mock_glob_func)

@pytest.fixture
def mock_isfile(monkeypatch):
    def mock_isfile_func(path):
        return path != '/path/to/dir'
    monkeypatch.setattr(os.path, 'isfile', mock_isfile_func)

def test_fileglob(mock_glob, mock_isfile):
    result = fileglob('/some/path/*')
    assert result == ['/path/to/file1', '/path/to/file2']
