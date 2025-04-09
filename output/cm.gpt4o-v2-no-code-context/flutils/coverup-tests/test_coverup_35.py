# file: flutils/pathutils.py:387-414
# asked: {"lines": [387, 412, 413, 414], "branches": []}
# gained: {"lines": [387, 412, 413, 414], "branches": []}

import pytest
from flutils.pathutils import find_paths
from flutils import normalize_path
from pathlib import Path
import os

@pytest.fixture
def setup_test_environment(tmp_path):
    # Create a temporary directory and files for testing
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    (test_dir / "file1.txt").write_text("content1")
    (test_dir / "file2.txt").write_text("content2")
    (test_dir / "subdir").mkdir()
    (test_dir / "subdir" / "file3.txt").write_text("content3")
    yield test_dir
    # Cleanup is handled by tmp_path fixture

def test_find_paths_with_glob_pattern(setup_test_environment, monkeypatch):
    test_dir = setup_test_environment

    def mock_normalize_path(path):
        return Path(path).expanduser()

    monkeypatch.setattr('flutils.pathutils.normalize_path', mock_normalize_path)

    pattern = str(test_dir / "*.txt")
    found_paths = list(find_paths(pattern))

    expected_paths = [
        test_dir / "file1.txt",
        test_dir / "file2.txt"
    ]

    assert sorted(found_paths) == sorted(expected_paths)

def test_find_paths_with_subdir_glob_pattern(setup_test_environment, monkeypatch):
    test_dir = setup_test_environment

    def mock_normalize_path(path):
        return Path(path).expanduser()

    monkeypatch.setattr('flutils.pathutils.normalize_path', mock_normalize_path)

    pattern = str(test_dir / "subdir" / "*.txt")
    found_paths = list(find_paths(pattern))

    expected_paths = [
        test_dir / "subdir" / "file3.txt"
    ]

    assert sorted(found_paths) == sorted(expected_paths)
