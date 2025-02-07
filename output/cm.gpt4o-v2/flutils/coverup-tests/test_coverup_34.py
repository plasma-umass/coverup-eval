# file: flutils/pathutils.py:574-621
# asked: {"lines": [574, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 617, 618, 619, 621], "branches": [[603, 0], [603, 604], [604, 605], [604, 606], [606, 607], [606, 621], [607, 608], [607, 618], [608, 609], [608, 612], [610, 608], [610, 611], [612, 607], [612, 613], [614, 615], [614, 617], [618, 0], [618, 619]]}
# gained: {"lines": [574, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 617, 618, 619, 621], "branches": [[603, 604], [604, 605], [604, 606], [606, 607], [606, 621], [607, 608], [607, 618], [608, 609], [608, 612], [610, 611], [612, 607], [612, 613], [614, 617], [618, 619]]}

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
    dir_path = create_dir("test_dir")
    assert dir_path.exists()
    path_absent(dir_path)
    assert not dir_path.exists()

def test_path_absent_dir_with_files(create_dir, create_file):
    dir_path = create_dir("test_dir")
    file_path = create_file("test_dir/test_file")
    assert dir_path.exists()
    assert file_path.exists()
    path_absent(dir_path)
    assert not dir_path.exists()
    assert not file_path.exists()

def test_path_absent_dir_with_symlinks(create_dir, create_file, tmp_path):
    dir_path = create_dir("test_dir")
    target_file = create_file("test_dir/target_file")
    symlink_path = tmp_path / "test_dir/symlink"
    symlink_path.symlink_to(target_file)
    assert dir_path.exists()
    assert target_file.exists()
    assert symlink_path.exists()
    path_absent(dir_path)
    assert not dir_path.exists()
    assert not target_file.exists()
    assert not symlink_path.exists()

def test_path_absent_nested_dir(create_dir, create_file):
    parent_dir = create_dir("parent_dir")
    child_dir = create_dir("parent_dir/child_dir")
    file_path = create_file("parent_dir/child_dir/test_file")
    assert parent_dir.exists()
    assert child_dir.exists()
    assert file_path.exists()
    path_absent(parent_dir)
    assert not parent_dir.exists()
    assert not child_dir.exists()
    assert not file_path.exists()
