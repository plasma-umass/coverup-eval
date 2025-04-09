# file: flutils/pathutils.py:574-621
# asked: {"lines": [574, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 617, 618, 619, 621], "branches": [[603, 0], [603, 604], [604, 605], [604, 606], [606, 607], [606, 621], [607, 608], [607, 618], [608, 609], [608, 612], [610, 608], [610, 611], [612, 607], [612, 613], [614, 615], [614, 617], [618, 0], [618, 619]]}
# gained: {"lines": [574, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 617, 618, 619, 621], "branches": [[603, 0], [603, 604], [604, 605], [604, 606], [606, 607], [606, 621], [607, 608], [607, 618], [608, 609], [608, 612], [610, 611], [612, 607], [612, 613], [614, 617], [618, 619]]}

import os
import pytest
from unittest import mock
from flutils.pathutils import path_absent, normalize_path

@pytest.fixture
def temp_dir(tmp_path):
    return tmp_path

def test_path_absent_file(temp_dir):
    # Create a temporary file
    temp_file = temp_dir / "temp_file.txt"
    temp_file.write_text("Temporary file content")

    # Ensure the file exists
    assert temp_file.exists()

    # Call the function to remove the file
    path_absent(temp_file)

    # Ensure the file is removed
    assert not temp_file.exists()

def test_path_absent_directory(temp_dir):
    # Create a temporary directory with files and subdirectories
    temp_subdir = temp_dir / "subdir"
    temp_subdir.mkdir()
    temp_file = temp_subdir / "temp_file.txt"
    temp_file.write_text("Temporary file content")
    temp_subsubdir = temp_subdir / "subsubdir"
    temp_subsubdir.mkdir()
    temp_subsubfile = temp_subsubdir / "temp_subsubfile.txt"
    temp_subsubfile.write_text("Temporary subsubfile content")

    # Ensure the directory and its contents exist
    assert temp_subdir.exists()
    assert temp_file.exists()
    assert temp_subsubdir.exists()
    assert temp_subsubfile.exists()

    # Call the function to remove the directory
    path_absent(temp_subdir)

    # Ensure the directory and its contents are removed
    assert not temp_subdir.exists()
    assert not temp_file.exists()
    assert not temp_subsubdir.exists()
    assert not temp_subsubfile.exists()

def test_path_absent_symlink(temp_dir):
    # Create a temporary file and a symlink to it
    temp_file = temp_dir / "temp_file.txt"
    temp_file.write_text("Temporary file content")
    temp_symlink = temp_dir / "temp_symlink"
    temp_symlink.symlink_to(temp_file)

    # Ensure the symlink exists
    assert temp_symlink.exists()

    # Call the function to remove the symlink
    path_absent(temp_symlink)

    # Ensure the symlink is removed but the original file remains
    assert not temp_symlink.exists()
    assert temp_file.exists()

def test_path_absent_nonexistent_path(temp_dir):
    # Create a path that does not exist
    nonexistent_path = temp_dir / "nonexistent_path"

    # Ensure the path does not exist
    assert not nonexistent_path.exists()

    # Call the function to ensure it handles nonexistent paths gracefully
    path_absent(nonexistent_path)

    # Ensure the path still does not exist
    assert not nonexistent_path.exists()
