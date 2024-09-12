# file: flutils/pathutils.py:138-216
# asked: {"lines": [190, 195, 200, 201, 202, 203, 204, 208, 210, 211, 212, 213], "branches": [[189, 190], [194, 195], [199, 200], [201, 202], [201, 210], [202, 201], [202, 203], [210, 0], [210, 211], [212, 0], [212, 213], [215, 0]]}
# gained: {"lines": [190, 195, 200, 201, 202, 203, 210, 211, 212, 213], "branches": [[189, 190], [194, 195], [199, 200], [201, 202], [201, 210], [202, 203], [210, 0], [210, 211], [212, 213]]}

import os
import pwd
import grp
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from flutils.pathutils import chown, normalize_path, get_os_user, get_os_group

@pytest.fixture
def mock_get_os_user():
    with patch('flutils.pathutils.get_os_user') as mock:
        mock.return_value = pwd.struct_passwd(('testuser', 'x', 1001, 1001, '', '/home/testuser', '/bin/bash'))
        yield mock

@pytest.fixture
def mock_get_os_group():
    with patch('flutils.pathutils.get_os_group') as mock:
        mock.return_value = grp.struct_group(('testgroup', 'x', 1001, []))
        yield mock

@pytest.fixture
def mock_os_chown():
    with patch('os.chown') as mock:
        yield mock

@pytest.fixture
def mock_path_exists():
    with patch('pathlib.Path.exists') as mock:
        mock.return_value = True
        yield mock

@pytest.fixture
def mock_path_is_dir():
    with patch('pathlib.Path.is_dir') as mock:
        mock.return_value = True
        yield mock

@pytest.fixture
def mock_path_is_file():
    with patch('pathlib.Path.is_file') as mock:
        mock.return_value = True
        yield mock

@pytest.fixture
def mock_path_glob():
    with patch('pathlib.Path.glob') as mock:
        mock.return_value = iter([Path('/mocked/path/file1'), Path('/mocked/path/file2')])
        yield mock

def test_chown_uid_gid_as_str(mock_get_os_user, mock_get_os_group, mock_os_chown, mock_path_exists):
    chown('/mocked/path', user='-1', group='-1')
    mock_os_chown.assert_called_once_with('/mocked/path', -1, -1)

def test_chown_with_glob_pattern(mock_get_os_user, mock_get_os_group, mock_os_chown, mock_path_glob, mock_path_is_dir, mock_path_is_file):
    chown('/mocked/path/*', user='testuser', group='testgroup')
    assert mock_os_chown.call_count == 2
    mock_os_chown.assert_any_call('/mocked/path/file1', 1001, 1001)
    mock_os_chown.assert_any_call('/mocked/path/file2', 1001, 1001)

def test_chown_with_glob_pattern_include_parent(mock_get_os_user, mock_get_os_group, mock_os_chown, mock_path_glob, mock_path_is_dir, mock_path_is_file):
    chown('/mocked/path/*', user='testuser', group='testgroup', include_parent=True)
    assert mock_os_chown.call_count == 3
    mock_os_chown.assert_any_call('/mocked/path/file1', 1001, 1001)
    mock_os_chown.assert_any_call('/mocked/path/file2', 1001, 1001)
    mock_os_chown.assert_any_call('/mocked/path', 1001, 1001)

def test_chown_path_exists(mock_get_os_user, mock_get_os_group, mock_os_chown, mock_path_exists):
    chown('/mocked/path', user='testuser', group='testgroup')
    mock_os_chown.assert_called_once_with('/mocked/path', 1001, 1001)
