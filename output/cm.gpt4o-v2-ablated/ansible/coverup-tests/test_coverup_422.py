# file: lib/ansible/module_utils/facts/system/distribution.py:30-44
# asked: {"lines": [32, 33, 36, 37, 40, 41, 44], "branches": [[32, 33], [32, 36], [36, 37], [36, 40], [40, 41], [40, 44]]}
# gained: {"lines": [32, 33, 36, 37, 40, 41, 44], "branches": [[32, 33], [32, 36], [36, 37], [36, 40], [40, 41], [40, 44]]}

import os
import pytest
from unittest.mock import patch

# Import the function to be tested
from ansible.module_utils.facts.system.distribution import _file_exists

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    def mock_exists(path):
        return path in existing_files
    monkeypatch.setattr(os.path, 'exists', mock_exists)

@pytest.fixture
def mock_os_path_getsize(monkeypatch):
    def mock_getsize(path):
        return file_sizes.get(path, 0)
    monkeypatch.setattr(os.path, 'getsize', mock_getsize)

def test_file_does_not_exist(mock_os_path_exists):
    global existing_files
    existing_files = []
    assert not _file_exists('/non/existent/path')

def test_file_exists_and_allow_empty(mock_os_path_exists):
    global existing_files
    existing_files = ['/existent/path']
    assert _file_exists('/existent/path', allow_empty=True)

def test_file_exists_and_not_allow_empty_but_is_empty(mock_os_path_exists, mock_os_path_getsize):
    global existing_files, file_sizes
    existing_files = ['/existent/empty/path']
    file_sizes = {'/existent/empty/path': 0}
    assert not _file_exists('/existent/empty/path', allow_empty=False)

def test_file_exists_and_not_allow_empty_and_is_not_empty(mock_os_path_exists, mock_os_path_getsize):
    global existing_files, file_sizes
    existing_files = ['/existent/nonempty/path']
    file_sizes = {'/existent/nonempty/path': 100}
    assert _file_exists('/existent/nonempty/path', allow_empty=False)
