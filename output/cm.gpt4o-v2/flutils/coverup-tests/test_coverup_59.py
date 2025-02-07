# file: flutils/pathutils.py:574-621
# asked: {"lines": [615], "branches": [[603, 0], [610, 608], [614, 615], [618, 0]]}
# gained: {"lines": [615], "branches": [[603, 0], [614, 615]]}

import os
import pytest
from unittest import mock
from flutils.pathutils import path_absent

@pytest.fixture
def create_file(tmp_path):
    def _create_file(name):
        file_path = tmp_path / name
        file_path.touch()
        return file_path
    return _create_file

@pytest.fixture
def create_dir(tmp_path):
    def _create_dir(name):
        dir_path = tmp_path / name
        dir_path.mkdir()
        return dir_path
    return _create_dir

def test_path_absent_file(create_file):
    file_path = create_file("test_file")
    assert file_path.exists()
    path_absent(file_path)
    assert not file_path.exists()

def test_path_absent_symlink(create_file, tmp_path):
    target_file = create_file("target_file")
    symlink_path = tmp_path / "symlink"
    symlink_path.symlink_to(target_file)
    assert symlink_path.exists()
    path_absent(symlink_path)
    assert not symlink_path.exists()
    assert target_file.exists()

def test_path_absent_empty_dir(create_dir):
    dir_path = create_dir("empty_dir")
    assert dir_path.exists()
    path_absent(dir_path)
    assert not dir_path.exists()

def test_path_absent_dir_with_files(create_dir, create_file):
    dir_path = create_dir("dir_with_files")
    file1 = create_file(dir_path / "file1")
    file2 = create_file(dir_path / "file2")
    assert dir_path.exists()
    assert file1.exists()
    assert file2.exists()
    path_absent(dir_path)
    assert not dir_path.exists()
    assert not file1.exists()
    assert not file2.exists()

def test_path_absent_dir_with_symlinks(create_dir, create_file, tmp_path):
    dir_path = create_dir("dir_with_symlinks")
    target_file = create_file("target_file")
    symlink1 = dir_path / "symlink1"
    symlink2 = dir_path / "symlink2"
    symlink1.symlink_to(target_file)
    symlink2.symlink_to(target_file)
    assert dir_path.exists()
    assert symlink1.exists()
    assert symlink2.exists()
    path_absent(dir_path)
    assert not dir_path.exists()
    assert not symlink1.exists()
    assert not symlink2.exists()
    assert target_file.exists()

def test_path_absent_dir_with_subdirs(create_dir, create_file):
    dir_path = create_dir("dir_with_subdirs")
    subdir1 = create_dir(dir_path / "subdir1")
    subdir2 = create_dir(dir_path / "subdir2")
    file1 = create_file(subdir1 / "file1")
    file2 = create_file(subdir2 / "file2")
    assert dir_path.exists()
    assert subdir1.exists()
    assert subdir2.exists()
    assert file1.exists()
    assert file2.exists()
    path_absent(dir_path)
    assert not dir_path.exists()
    assert not subdir1.exists()
    assert not subdir2.exists()
    assert not file1.exists()
    assert not file2.exists()

def test_path_absent_dir_with_symlinked_dir(create_dir, tmp_path):
    dir_path = create_dir("dir_with_symlinked_dir")
    target_dir = create_dir("target_dir")
    symlink_dir = dir_path / "symlink_dir"
    symlink_dir.symlink_to(target_dir, target_is_directory=True)
    assert dir_path.exists()
    assert symlink_dir.exists()
    path_absent(dir_path)
    assert not dir_path.exists()
    assert not symlink_dir.exists()
    assert target_dir.exists()

def test_path_absent_nonexistent_path(tmp_path):
    nonexistent_path = tmp_path / "nonexistent_path"
    assert not nonexistent_path.exists()
    path_absent(nonexistent_path)
    assert not nonexistent_path.exists()
