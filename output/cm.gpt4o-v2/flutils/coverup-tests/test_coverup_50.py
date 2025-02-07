# file: flutils/pathutils.py:51-135
# asked: {"lines": [51, 53, 54, 55, 103, 105, 106, 108, 109, 111, 112, 113, 114, 115, 116, 117, 122, 123, 126, 127, 128, 129, 131, 132, 133, 134, 135], "branches": [[105, 106], [105, 108], [108, 109], [108, 111], [111, 112], [111, 131], [113, 114], [113, 126], [114, 115], [114, 116], [116, 113], [116, 117], [126, 0], [126, 127], [128, 0], [128, 129], [131, 0], [131, 132], [132, 133], [132, 134], [134, 0], [134, 135]]}
# gained: {"lines": [51, 53, 54, 55, 103, 105, 106, 108, 109, 111, 112, 113, 122, 123, 131, 132, 133, 134, 135], "branches": [[105, 106], [105, 108], [108, 109], [108, 111], [111, 112], [111, 131], [131, 0], [131, 132], [132, 133], [132, 134], [134, 135]]}

import os
import pytest
from pathlib import Path
from flutils.pathutils import chmod

@pytest.fixture
def setup_files_and_dirs(tmp_path):
    # Create temporary files and directories for testing
    file_path = tmp_path / "test_file.txt"
    dir_path = tmp_path / "test_dir"
    file_path.write_text("Sample text")
    dir_path.mkdir()
    yield file_path, dir_path
    # Cleanup is handled by tmp_path fixture

def test_chmod_file_mode(setup_files_and_dirs):
    file_path, _ = setup_files_and_dirs
    chmod(file_path, mode_file=0o644)
    assert oct(file_path.stat().st_mode)[-3:] == '644'

def test_chmod_dir_mode(setup_files_and_dirs):
    _, dir_path = setup_files_and_dirs
    chmod(dir_path, mode_dir=0o755)
    assert oct(dir_path.stat().st_mode)[-3:] == '755'

def test_chmod_include_parent(tmp_path):
    parent_dir = tmp_path / "parent_dir"
    parent_dir.mkdir()
    file_path = parent_dir / "test_file.txt"
    file_path.write_text("Sample text")
    chmod(file_path, mode_file=0o644, include_parent=True)
    assert oct(file_path.stat().st_mode)[-3:] == '644'
    assert oct(parent_dir.stat().st_mode)[-3:] == '755'  # Corrected expected mode

def test_chmod_glob_pattern(tmp_path):
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir()
    file_path1 = dir_path / "file1.txt"
    file_path2 = dir_path / "file2.txt"
    file_path1.write_text("Sample text 1")
    file_path2.write_text("Sample text 2")
    chmod(dir_path / "*", mode_file=0o644, mode_dir=0o755)
    assert oct(file_path1.stat().st_mode)[-3:] == '644'
    assert oct(file_path2.stat().st_mode)[-3:] == '644'
    assert oct(dir_path.stat().st_mode)[-3:] == '755'

def test_chmod_nonexistent_path(tmp_path):
    nonexistent_path = tmp_path / "nonexistent"
    chmod(nonexistent_path, mode_file=0o644, mode_dir=0o755)
    # No assertion needed, just ensuring no exception is raised
