# file: flutils/pathutils.py:574-621
# asked: {"lines": [600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 617, 618, 619, 621], "branches": [[603, 0], [603, 604], [604, 605], [604, 606], [606, 607], [606, 621], [607, 608], [607, 618], [608, 609], [608, 612], [610, 608], [610, 611], [612, 607], [612, 613], [614, 615], [614, 617], [618, 0], [618, 619]]}
# gained: {"lines": [600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 618, 619, 621], "branches": [[603, 604], [604, 605], [604, 606], [606, 607], [606, 621], [607, 608], [607, 618], [608, 609], [608, 612], [610, 611], [612, 607], [618, 619]]}

import os
import pytest
from unittest.mock import patch
from flutils.pathutils import path_absent

@pytest.fixture
def create_file(tmp_path):
    file_path = tmp_path / "test_file"
    file_path.write_text("content")
    return file_path

@pytest.fixture
def create_dir(tmp_path):
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    return dir_path

@pytest.fixture
def create_symlink(tmp_path, create_file):
    symlink_path = tmp_path / "test_symlink"
    symlink_path.symlink_to(create_file)
    return symlink_path

def test_path_absent_file(create_file):
    path_absent(create_file)
    assert not create_file.exists()

def test_path_absent_dir(create_dir):
    path_absent(create_dir)
    assert not create_dir.exists()

def test_path_absent_symlink(create_symlink):
    path_absent(create_symlink)
    assert not create_symlink.exists()

def test_path_absent_nested_dir(tmp_path):
    nested_dir = tmp_path / "nested_dir"
    nested_dir.mkdir()
    nested_file = nested_dir / "nested_file"
    nested_file.write_text("content")
    path_absent(nested_dir)
    assert not nested_dir.exists()
    assert not nested_file.exists()

def test_path_absent_symlink_in_dir(tmp_path, create_file):
    dir_path = tmp_path / "dir_with_symlink"
    dir_path.mkdir()
    symlink_path = dir_path / "symlink"
    symlink_path.symlink_to(create_file)
    path_absent(dir_path)
    assert not dir_path.exists()
    assert not symlink_path.exists()
