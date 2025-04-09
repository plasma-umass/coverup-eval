# file: lib/ansible/module_utils/common/process.py:12-44
# asked: {"lines": [21, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44], "branches": [[25, 26], [25, 28], [26, 25], [26, 27], [31, 32], [31, 34], [32, 31], [32, 33], [34, 35], [34, 41], [35, 36], [35, 37], [38, 34], [38, 39], [41, 42], [41, 44]]}
# gained: {"lines": [21, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44], "branches": [[25, 26], [25, 28], [26, 27], [31, 32], [31, 34], [32, 33], [34, 35], [34, 41], [35, 37], [38, 34], [38, 39], [41, 42], [41, 44]]}

import os
import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.common.process import get_bin_path

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    def mock_exists(path):
        if path in ['/sbin', '/usr/sbin', '/usr/local/sbin', '/mocked_path', '/bin/ls']:
            return True
        return False
    monkeypatch.setattr(os.path, 'exists', mock_exists)

@pytest.fixture
def mock_os_environ(monkeypatch):
    monkeypatch.setattr(os, 'environ', {'PATH': '/bin:/usr/bin'})

@pytest.fixture
def mock_is_executable(monkeypatch):
    def mock_is_exec(path):
        return path == '/bin/ls'
    monkeypatch.setattr('ansible.module_utils.common.file.is_executable', mock_is_exec)

def test_get_bin_path_with_opt_dirs(mock_os_path_exists, mock_os_environ, mock_is_executable):
    result = get_bin_path('ls', opt_dirs=['/mocked_path'])
    assert result == '/bin/ls'

def test_get_bin_path_without_opt_dirs(mock_os_path_exists, mock_os_environ, mock_is_executable):
    result = get_bin_path('ls')
    assert result == '/bin/ls'

def test_get_bin_path_not_found(mock_os_path_exists, mock_os_environ, mock_is_executable):
    with pytest.raises(ValueError, match='Failed to find required executable "nonexistent"'):
        get_bin_path('nonexistent')
