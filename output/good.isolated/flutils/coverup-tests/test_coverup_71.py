# file flutils/pathutils.py:574-621
# lines [615]
# branches ['610->608', '614->615', '618->exit']

import os
import pytest
from pathlib import Path
from flutils.pathutils import path_absent

@pytest.fixture
def directory_with_nested_symlinks(tmp_path):
    # Create a directory with a nested structure and symlinks
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    nested_dir_path = dir_path / "nested_dir"
    nested_dir_path.mkdir()
    file_path = nested_dir_path / "test_file.txt"
    file_path.touch()
    symlink_to_file_path = nested_dir_path / "symlink_to_file"
    symlink_to_file_path.symlink_to(file_path)
    symlink_to_dir_path = dir_path / "symlink_to_dir"
    symlink_to_dir_path.symlink_to(nested_dir_path)
    # Return the paths to be used in the test
    return dir_path, nested_dir_path, file_path, symlink_to_file_path, symlink_to_dir_path

def test_path_absent_with_nested_symlinks(directory_with_nested_symlinks):
    dir_path, nested_dir_path, file_path, symlink_to_file_path, symlink_to_dir_path = directory_with_nested_symlinks
    # Ensure the file and symlinks exist before calling path_absent
    assert file_path.exists()
    assert symlink_to_file_path.is_symlink()
    assert symlink_to_dir_path.is_symlink()
    # Call path_absent which should remove the file, symlinks, and directories
    path_absent(dir_path)
    # Assert that the file, symlinks, and directories have been removed
    assert not file_path.exists()
    assert not symlink_to_file_path.exists()
    assert not symlink_to_dir_path.exists()
    assert not nested_dir_path.exists()
    assert not dir_path.exists()

def test_path_absent_with_symlink_to_itself(tmp_path):
    # Create a symlink that points to itself
    symlink_path = tmp_path / "test_symlink"
    symlink_path.symlink_to(symlink_path)
    # Ensure the symlink exists before calling path_absent
    assert symlink_path.is_symlink()
    # Call path_absent which should remove the symlink
    path_absent(symlink_path)
    # Assert that the symlink has been removed
    assert not symlink_path.exists()
