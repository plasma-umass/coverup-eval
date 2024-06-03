# file flutils/pathutils.py:574-621
# lines [574, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 617, 618, 619, 621]
# branches ['603->exit', '603->604', '604->605', '604->606', '606->607', '606->621', '607->608', '607->618', '608->609', '608->612', '610->608', '610->611', '612->607', '612->613', '614->615', '614->617', '618->exit', '618->619']

import os
import pytest
from unittest.mock import patch
from flutils.pathutils import path_absent

@pytest.fixture
def temp_dir(tmp_path):
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    yield dir_path
    if dir_path.exists():
        for root, dirs, files in os.walk(dir_path, topdown=False):
            for name in files:
                os.unlink(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(dir_path)

@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("test content")
    yield file_path
    if file_path.exists():
        os.unlink(file_path)

@pytest.fixture
def temp_symlink(tmp_path):
    target_path = tmp_path / "target_file.txt"
    target_path.write_text("target content")
    symlink_path = tmp_path / "test_symlink"
    symlink_path.symlink_to(target_path)
    yield symlink_path
    if symlink_path.exists():
        os.unlink(symlink_path)
    if target_path.exists():
        os.unlink(target_path)

def test_path_absent_directory(temp_dir):
    path_absent(temp_dir)
    assert not temp_dir.exists()

def test_path_absent_file(temp_file):
    path_absent(temp_file)
    assert not temp_file.exists()

def test_path_absent_symlink(temp_symlink):
    path_absent(temp_symlink)
    assert not temp_symlink.exists()

def test_path_absent_nonexistent_path(tmp_path):
    nonexistent_path = tmp_path / "nonexistent"
    path_absent(nonexistent_path)
    assert not nonexistent_path.exists()

@patch('flutils.pathutils.normalize_path', side_effect=lambda x: x)
def test_path_absent_normalize_path(mock_normalize_path, temp_file):
    path_absent(temp_file)
    mock_normalize_path.assert_called_once_with(temp_file)
    assert not temp_file.exists()
