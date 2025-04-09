# file: flutils/pathutils.py:51-135
# asked: {"lines": [51, 53, 54, 55, 103, 105, 106, 108, 109, 111, 112, 113, 114, 115, 116, 117, 122, 123, 126, 127, 128, 129, 131, 132, 133, 134, 135], "branches": [[105, 106], [105, 108], [108, 109], [108, 111], [111, 112], [111, 131], [113, 114], [113, 126], [114, 115], [114, 116], [116, 113], [116, 117], [126, 0], [126, 127], [128, 0], [128, 129], [131, 0], [131, 132], [132, 133], [132, 134], [134, 0], [134, 135]]}
# gained: {"lines": [51, 53, 54, 55, 103, 105, 106, 108, 109, 111, 112, 113, 122, 123, 131, 132, 133, 134, 135], "branches": [[105, 106], [105, 108], [108, 109], [108, 111], [111, 112], [111, 131], [131, 0], [131, 132], [132, 133], [132, 134], [134, 135]]}

import os
import pytest
from pathlib import Path
from flutils.pathutils import chmod

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test_file.txt"
    file.write_text("content")
    yield file
    file.unlink()

@pytest.fixture
def temp_dir(tmp_path):
    dir = tmp_path / "test_dir"
    dir.mkdir()
    yield dir
    dir.rmdir()

@pytest.fixture
def temp_symlink(tmp_path, temp_file):
    symlink = tmp_path / "test_symlink"
    symlink.symlink_to(temp_file)
    yield symlink
    symlink.unlink()

def test_chmod_file(temp_file):
    chmod(temp_file, 0o644)
    assert oct(temp_file.stat().st_mode)[-3:] == '644'

def test_chmod_dir(temp_dir):
    chmod(temp_dir, mode_dir=0o755)
    assert oct(temp_dir.stat().st_mode)[-3:] == '755'

def test_chmod_symlink(temp_symlink):
    original_mode = oct(temp_symlink.stat().st_mode)[-3:]
    chmod(temp_symlink, 0o644)
    assert oct(temp_symlink.stat().st_mode)[-3:] == original_mode

def test_chmod_nonexistent_path():
    non_existent_path = Path("/non/existent/path")
    chmod(non_existent_path, 0o644)  # Should not raise an error

def test_chmod_include_parent(tmp_path, temp_file):
    parent_dir = temp_file.parent
    chmod(temp_file, 0o644, include_parent=True)
    assert oct(parent_dir.stat().st_mode)[-3:] == '700'  # Default mode_dir is 0o700

def test_chmod_glob_pattern(tmp_path):
    (tmp_path / "file1.txt").write_text("content")
    (tmp_path / "file2.txt").write_text("content")
    chmod(tmp_path / "*.txt", 0o644)
    for file in tmp_path.glob("*.txt"):
        assert oct(file.stat().st_mode)[-3:] == '644'
