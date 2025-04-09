# file flutils/pathutils.py:51-135
# lines [51, 53, 54, 55, 103, 105, 106, 108, 109, 111, 112, 113, 114, 115, 116, 117, 122, 123, 126, 127, 128, 129, 131, 132, 133, 134, 135]
# branches ['105->106', '105->108', '108->109', '108->111', '111->112', '111->131', '113->114', '113->126', '114->115', '114->116', '116->113', '116->117', '126->exit', '126->127', '128->exit', '128->129', '131->exit', '131->132', '132->133', '132->134', '134->exit', '134->135']

import os
import pytest
from pathlib import Path
from flutils.pathutils import chmod

@pytest.fixture
def setup_files_and_dirs(tmp_path):
    # Create a temporary directory and files for testing
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    test_file = test_dir / "test_file.txt"
    test_file.touch()
    test_subdir = test_dir / "subdir"
    test_subdir.mkdir()
    test_subfile = test_subdir / "subfile.txt"
    test_subfile.touch()
    yield test_dir, test_file, test_subdir, test_subfile
    # Cleanup is handled by tmp_path fixture

def test_chmod_include_parent(setup_files_and_dirs):
    test_dir, test_file, test_subdir, test_subfile = setup_files_and_dirs

    # Change mode of files and directories including parent
    chmod(test_dir / "*", mode_file=0o644, mode_dir=0o755, include_parent=True)

    # Assert the modes have been changed correctly
    assert oct(test_file.stat().st_mode & 0o777) == '0o644'
    assert oct(test_subdir.stat().st_mode & 0o777) == '0o755'
    assert oct(test_subfile.stat().st_mode & 0o777) == '0o644'
    assert oct(test_dir.stat().st_mode & 0o777) == '0o755'

def test_chmod_no_glob_pattern(setup_files_and_dirs):
    test_dir, test_file, test_subdir, test_subfile = setup_files_and_dirs

    # Change mode of a specific file
    chmod(test_file, mode_file=0o600)

    # Assert the mode has been changed correctly
    assert oct(test_file.stat().st_mode & 0o777) == '0o600'

    # Change mode of a specific directory
    chmod(test_subdir, mode_dir=0o700)

    # Assert the mode has been changed correctly
    assert oct(test_subdir.stat().st_mode & 0o777) == '0o700'

def test_chmod_nonexistent_path():
    # Create a path that does not exist
    nonexistent_path = Path("/nonexistent/path")

    # Ensure no exception is raised and nothing is done
    chmod(nonexistent_path, mode_file=0o600, mode_dir=0o700)

    # Since the path does not exist, there's nothing to assert
    # Just ensuring no exception is raised

def test_chmod_symlink(tmp_path):
    # Create a temporary directory and files for testing
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    test_file = test_dir / "test_file.txt"
    test_file.touch()
    symlink = test_dir / "symlink"
    symlink.symlink_to(test_file)

    # Change mode of files and directories including symlink
    chmod(test_dir / "*", mode_file=0o644, mode_dir=0o755, include_parent=True)

    # Assert the modes have been changed correctly
    assert oct(test_file.stat().st_mode & 0o777) == '0o644'
    assert oct(symlink.lstat().st_mode & 0o777) == '0o777'  # Symlink mode should not change
    assert oct(test_dir.stat().st_mode & 0o777) == '0o755'
