# file: flutils/pathutils.py:138-216
# asked: {"lines": [138, 140, 141, 142, 188, 189, 190, 192, 194, 195, 197, 199, 200, 201, 202, 203, 204, 208, 210, 211, 212, 213, 215, 216], "branches": [[189, 190], [189, 192], [194, 195], [194, 197], [199, 200], [199, 215], [201, 202], [201, 210], [202, 201], [202, 203], [210, 0], [210, 211], [212, 0], [212, 213], [215, 0], [215, 216]]}
# gained: {"lines": [138, 140, 141, 142, 188, 189, 190, 192, 194, 195, 197, 199, 200, 201, 204, 208, 215, 216], "branches": [[189, 190], [189, 192], [194, 195], [194, 197], [199, 200], [199, 215], [215, 0], [215, 216]]}

import os
import pytest
from pathlib import Path
from flutils.pathutils import chown

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "testfile.txt"
    file.write_text("content")
    yield file
    file.unlink()

@pytest.fixture
def temp_dir(tmp_path):
    dir = tmp_path / "testdir"
    dir.mkdir()
    yield dir
    dir.rmdir()

@pytest.fixture
def mock_get_os_user(mocker):
    mock = mocker.patch('flutils.pathutils.get_os_user')
    mock.return_value.pw_uid = 1000
    return mock

@pytest.fixture
def mock_get_os_group(mocker):
    mock = mocker.patch('flutils.pathutils.get_os_group')
    mock.return_value.gr_gid = 1000
    return mock

def test_chown_file(temp_file, mock_get_os_user, mock_get_os_group):
    chown(temp_file, user='testuser', group='testgroup')
    assert temp_file.exists()

def test_chown_dir(temp_dir, mock_get_os_user, mock_get_os_group):
    chown(temp_dir, user='testuser', group='testgroup')
    assert temp_dir.exists()

def test_chown_glob_pattern(temp_dir, mock_get_os_user, mock_get_os_group):
    sub_file = temp_dir / "subfile.txt"
    sub_file.write_text("content")
    chown(str(temp_dir / "*"), user='testuser', group='testgroup')
    assert sub_file.exists()
    sub_file.unlink()

def test_chown_include_parent(temp_dir, mock_get_os_user, mock_get_os_group):
    sub_file = temp_dir / "subfile.txt"
    sub_file.write_text("content")
    chown(str(temp_dir / "*"), user='testuser', group='testgroup', include_parent=True)
    assert sub_file.exists()
    sub_file.unlink()

def test_chown_nonexistent_path(mocker, mock_get_os_user, mock_get_os_group):
    mocker.patch('flutils.pathutils.normalize_path', return_value=Path('/nonexistent/path'))
    chown('/nonexistent/path', user='testuser', group='testgroup')

def test_chown_user_group_as_int(temp_file, mock_get_os_user, mock_get_os_group):
    chown(temp_file, user=1000, group=1000)
    assert temp_file.exists()

def test_chown_user_group_as_str(temp_file, mock_get_os_user, mock_get_os_group):
    chown(temp_file, user='-1', group='-1')
    assert temp_file.exists()
