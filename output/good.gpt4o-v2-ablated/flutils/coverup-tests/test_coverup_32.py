# file: flutils/pathutils.py:138-216
# asked: {"lines": [138, 140, 141, 142, 188, 189, 190, 192, 194, 195, 197, 199, 200, 201, 202, 203, 204, 208, 210, 211, 212, 213, 215, 216], "branches": [[189, 190], [189, 192], [194, 195], [194, 197], [199, 200], [199, 215], [201, 202], [201, 210], [202, 201], [202, 203], [210, 0], [210, 211], [212, 0], [212, 213], [215, 0], [215, 216]]}
# gained: {"lines": [138, 140, 141, 142, 188, 189, 190, 192, 194, 195, 197, 199, 200, 201, 202, 203, 204, 208, 210, 211, 212, 213, 215, 216], "branches": [[189, 190], [189, 192], [194, 195], [194, 197], [199, 200], [199, 215], [201, 202], [201, 210], [202, 203], [210, 0], [210, 211], [212, 213], [215, 0], [215, 216]]}

import os
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from flutils.pathutils import chown

@pytest.fixture
def mock_get_os_user(monkeypatch):
    mock = MagicMock()
    mock.pw_uid = 1000
    monkeypatch.setattr('flutils.pathutils.get_os_user', lambda x: mock)
    return mock

@pytest.fixture
def mock_get_os_group(monkeypatch):
    mock = MagicMock()
    mock.gr_gid = 1000
    monkeypatch.setattr('flutils.pathutils.get_os_group', lambda x: mock)
    return mock

@pytest.fixture
def mock_normalize_path(monkeypatch):
    def mock_normalize(path):
        return Path(path).expanduser()
    monkeypatch.setattr('flutils.pathutils.normalize_path', mock_normalize)
    return mock_normalize

def test_chown_no_path_exists(mock_normalize_path, mock_get_os_user, mock_get_os_group):
    with patch('os.chown') as mock_chown:
        chown('~/nonexistent_path')
        mock_chown.assert_not_called()

def test_chown_with_user_group(mock_normalize_path, mock_get_os_user, mock_get_os_group):
    with patch('os.chown') as mock_chown:
        with patch('pathlib.Path.exists', return_value=True):
            chown('~/existent_path', user='testuser', group='testgroup')
            mock_chown.assert_called_once_with(str(Path('~/existent_path').expanduser()), 1000, 1000)

def test_chown_with_glob(mock_normalize_path, mock_get_os_user, mock_get_os_group):
    with patch('os.chown') as mock_chown:
        with patch('pathlib.Path.glob', return_value=[Path('~/file1'), Path('~/file2')]):
            with patch('pathlib.Path.is_file', return_value=True):
                chown('~/tmp/*', user='testuser', group='testgroup')
                assert mock_chown.call_count == 2

def test_chown_with_glob_include_parent(mock_normalize_path, mock_get_os_user, mock_get_os_group):
    with patch('os.chown') as mock_chown:
        with patch('pathlib.Path.glob', return_value=[Path('~/tmp/file1'), Path('~/tmp/file2')]):
            with patch('pathlib.Path.is_file', return_value=True):
                with patch('pathlib.Path.is_dir', return_value=True):
                    chown('~/tmp/*', user='testuser', group='testgroup', include_parent=True)
                    assert mock_chown.call_count == 3

def test_chown_with_glob_no_results(mock_normalize_path, mock_get_os_user, mock_get_os_group):
    with patch('os.chown') as mock_chown:
        with patch('pathlib.Path.glob', side_effect=NotImplementedError):
            chown('~/tmp/*', user='testuser', group='testgroup')
            mock_chown.assert_not_called()

def test_chown_user_group_as_dash_one(mock_normalize_path, mock_get_os_user, mock_get_os_group):
    with patch('os.chown') as mock_chown:
        with patch('pathlib.Path.exists', return_value=True):
            chown('~/existent_path', user='-1', group='-1')
            mock_chown.assert_called_once_with(str(Path('~/existent_path').expanduser()), -1, -1)
