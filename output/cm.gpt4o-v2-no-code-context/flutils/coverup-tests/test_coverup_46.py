# file: flutils/pathutils.py:51-135
# asked: {"lines": [51, 53, 54, 55, 103, 105, 106, 108, 109, 111, 112, 113, 114, 115, 116, 117, 122, 123, 126, 127, 128, 129, 131, 132, 133, 134, 135], "branches": [[105, 106], [105, 108], [108, 109], [108, 111], [111, 112], [111, 131], [113, 114], [113, 126], [114, 115], [114, 116], [116, 113], [116, 117], [126, 0], [126, 127], [128, 0], [128, 129], [131, 0], [131, 132], [132, 133], [132, 134], [134, 0], [134, 135]]}
# gained: {"lines": [51, 53, 54, 55, 103, 105, 106, 108, 109, 111, 112, 113, 122, 123, 131, 132, 133, 134, 135], "branches": [[105, 106], [105, 108], [108, 109], [108, 111], [111, 112], [111, 131], [131, 0], [131, 132], [132, 133], [132, 134], [134, 135]]}

import os
import pytest
import tempfile
from pathlib import Path
from flutils.pathutils import chmod

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield Path(tmpdirname)

def test_chmod_file(temp_dir):
    file_path = temp_dir / "test_file.txt"
    file_path.touch()
    chmod(file_path, mode_file=0o644)
    new_mode = file_path.stat().st_mode
    assert oct(new_mode & 0o777) == '0o644'

def test_chmod_dir(temp_dir):
    dir_path = temp_dir / "test_dir"
    dir_path.mkdir()
    chmod(dir_path, mode_dir=0o755)
    new_mode = dir_path.stat().st_mode
    assert oct(new_mode & 0o777) == '0o755'

def test_chmod_glob_pattern(temp_dir):
    (temp_dir / "test_dir").mkdir()
    (temp_dir / "test_dir" / "file1.txt").touch()
    (temp_dir / "test_dir" / "file2.txt").touch()
    chmod(temp_dir / "test_dir" / "*", mode_file=0o644, mode_dir=0o755)
    for item in (temp_dir / "test_dir").iterdir():
        if item.is_file():
            assert oct(item.stat().st_mode & 0o777) == '0o644'
        elif item.is_dir():
            assert oct(item.stat().st_mode & 0o777) == '0o755'

def test_chmod_include_parent(temp_dir):
    (temp_dir / "test_dir").mkdir()
    (temp_dir / "test_dir" / "file1.txt").touch()
    chmod(temp_dir / "test_dir" / "*", mode_file=0o644, mode_dir=0o755, include_parent=True)
    assert oct((temp_dir / "test_dir").stat().st_mode & 0o777) == '0o755'

def test_chmod_nonexistent_path(temp_dir):
    non_existent_path = temp_dir / "non_existent"
    chmod(non_existent_path, mode_file=0o644, mode_dir=0o755)
    assert not non_existent_path.exists()
