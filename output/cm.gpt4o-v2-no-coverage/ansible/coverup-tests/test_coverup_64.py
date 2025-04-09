# file: lib/ansible/module_utils/common/process.py:12-44
# asked: {"lines": [12, 21, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44], "branches": [[25, 26], [25, 28], [26, 25], [26, 27], [31, 32], [31, 34], [32, 31], [32, 33], [34, 35], [34, 41], [35, 36], [35, 37], [38, 34], [38, 39], [41, 42], [41, 44]]}
# gained: {"lines": [12, 21, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44], "branches": [[25, 26], [25, 28], [26, 25], [31, 32], [31, 34], [32, 33], [34, 35], [34, 41], [35, 37], [38, 34], [38, 39], [41, 42], [41, 44]]}

import os
import stat
import pytest
from unittest.mock import patch, mock_open, MagicMock
from ansible.module_utils.common.process import get_bin_path

@pytest.fixture
def mock_os_path_exists(monkeypatch):
    def mock_exists(path):
        if path in ["/mock/bin/executable", "/sbin", "/usr/sbin", "/usr/local/sbin"]:
            return True
        return False
    monkeypatch.setattr(os.path, "exists", mock_exists)

@pytest.fixture
def mock_os_path_isdir(monkeypatch):
    def mock_isdir(path):
        return False
    monkeypatch.setattr(os.path, "isdir", mock_isdir)

@pytest.fixture
def mock_is_executable(monkeypatch):
    def mock_is_exec(path):
        return True
    monkeypatch.setattr("ansible.module_utils.common.file.is_executable", mock_is_exec)

@pytest.fixture
def mock_os_environ(monkeypatch):
    monkeypatch.setattr(os, "environ", {"PATH": "/mock/bin"})

@pytest.fixture
def mock_os_stat(monkeypatch):
    mock_stat = MagicMock()
    mock_stat.st_mode = stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
    monkeypatch.setattr(os, "stat", lambda path: mock_stat)

def test_get_bin_path_found_in_opt_dirs(mock_os_path_exists, mock_os_path_isdir, mock_is_executable, mock_os_environ, mock_os_stat):
    opt_dirs = ["/mock/bin"]
    result = get_bin_path("executable", opt_dirs=opt_dirs)
    assert result == "/mock/bin/executable"

def test_get_bin_path_found_in_path(mock_os_path_exists, mock_os_path_isdir, mock_is_executable, mock_os_environ, mock_os_stat):
    result = get_bin_path("executable")
    assert result == "/mock/bin/executable"

def test_get_bin_path_not_found(mock_os_path_exists, mock_os_path_isdir, mock_is_executable, monkeypatch):
    monkeypatch.setattr(os, "environ", {"PATH": "/nonexistent"})
    with pytest.raises(ValueError, match='Failed to find required executable "executable" in paths: /nonexistent:/sbin:/usr/sbin:/usr/local/sbin'):
        get_bin_path("executable")

def test_get_bin_path_with_empty_opt_dirs(mock_os_path_exists, mock_os_path_isdir, mock_is_executable, mock_os_environ, mock_os_stat):
    result = get_bin_path("executable", opt_dirs=[])
    assert result == "/mock/bin/executable"

def test_get_bin_path_with_none_opt_dirs(mock_os_path_exists, mock_os_path_isdir, mock_is_executable, mock_os_environ, mock_os_stat):
    result = get_bin_path("executable", opt_dirs=None)
    assert result == "/mock/bin/executable"
