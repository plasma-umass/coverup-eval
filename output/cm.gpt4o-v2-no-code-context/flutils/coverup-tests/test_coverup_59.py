# file: flutils/pathutils.py:138-216
# asked: {"lines": [202, 203, 210, 211, 212, 213], "branches": [[201, 202], [201, 210], [202, 201], [202, 203], [210, 0], [210, 211], [212, 0], [212, 213]]}
# gained: {"lines": [202, 203, 210, 211, 212, 213], "branches": [[201, 202], [201, 210], [202, 203], [210, 0], [210, 211], [212, 213]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from flutils.pathutils import chown

@pytest.fixture
def mock_normalize_path(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('flutils.pathutils.normalize_path', mock)
    return mock

@pytest.fixture
def mock_get_os_user(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('flutils.pathutils.get_os_user', mock)
    return mock

@pytest.fixture
def mock_get_os_group(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('flutils.pathutils.get_os_group', mock)
    return mock

@pytest.fixture
def mock_path(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('flutils.pathutils.Path', mock)
    return mock

@pytest.fixture
def mock_os_chown(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('os.chown', mock)
    return mock

def test_chown_with_glob_pattern(mock_normalize_path, mock_get_os_user, mock_get_os_group, mock_path, mock_os_chown):
    mock_normalize_path.return_value = MagicMock(as_posix=lambda: '/some/path/*')
    mock_get_os_user.return_value.pw_uid = 1000
    mock_get_os_group.return_value.gr_gid = 1000

    mock_sub_path = MagicMock()
    mock_sub_path.is_dir.return_value = True
    mock_sub_path.as_posix.return_value = '/some/path/file1'
    mock_path().glob.return_value = [mock_sub_path]

    chown('/some/path/*', user='user', group='group')

    mock_os_chown.assert_called_with('/some/path/file1', 1000, 1000)

def test_chown_with_include_parent(mock_normalize_path, mock_get_os_user, mock_get_os_group, mock_path, mock_os_chown):
    mock_normalize_path.return_value = MagicMock(as_posix=lambda: '/some/path/*')
    mock_get_os_user.return_value.pw_uid = 1000
    mock_get_os_group.return_value.gr_gid = 1000

    mock_sub_path = MagicMock()
    mock_sub_path.is_dir.return_value = True
    mock_sub_path.as_posix.return_value = '/some/path/file1'
    mock_path().glob.return_value = [mock_sub_path]

    mock_parent_path = MagicMock()
    mock_parent_path.is_dir.return_value = True
    mock_parent_path.as_posix.return_value = '/some'
    mock_normalize_path.return_value.parent = mock_parent_path

    chown('/some/path/*', user='user', group='group', include_parent=True)

    mock_os_chown.assert_any_call('/some/path/file1', 1000, 1000)
    mock_os_chown.assert_any_call('/some', 1000, 1000)
