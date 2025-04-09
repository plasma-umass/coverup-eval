# file flutils/pathutils.py:504-560
# lines [504, 505, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560]
# branches ['553->554', '553->555']

import os
import pytest
from pathlib import Path
from unittest import mock
from flutils.pathutils import normalize_path

@pytest.fixture
def mock_home_dir(monkeypatch):
    home_dir = '/mock/home'
    monkeypatch.setenv('HOME', home_dir)
    return home_dir

@pytest.fixture
def mock_cwd(monkeypatch):
    cwd = '/mock/cwd'
    monkeypatch.setattr(os, 'getcwd', lambda: cwd)
    return cwd

def test_normalize_path_str(mock_home_dir, mock_cwd):
    path = '~/tmp/foo/../bar'
    expected = Path('/mock/home/tmp/bar')
    result = normalize_path(path)
    assert result == expected

def test_normalize_path_bytes(mock_home_dir, mock_cwd):
    path = b'~/tmp/foo/../bar'
    expected = Path('/mock/home/tmp/bar')
    result = normalize_path(path)
    assert result == expected

def test_normalize_path_posixpath(mock_home_dir, mock_cwd):
    path = Path('~/tmp/foo/../bar')
    expected = Path('/mock/home/tmp/bar')
    result = normalize_path(path)
    assert result == expected

def test_normalize_path_relative(mock_home_dir, mock_cwd):
    path = 'relative/path'
    expected = Path('/mock/cwd/relative/path')
    result = normalize_path(path)
    assert result == expected

def test_normalize_path_absolute(mock_home_dir, mock_cwd):
    path = '/absolute/path'
    expected = Path('/absolute/path')
    result = normalize_path(path)
    assert result == expected

def test_normalize_path_with_env_var(monkeypatch, mock_home_dir, mock_cwd):
    monkeypatch.setenv('TEST_VAR', 'test_value')
    path = '$TEST_VAR/path'
    expected = Path('/mock/cwd/test_value/path')
    result = normalize_path(path)
    assert result == expected
