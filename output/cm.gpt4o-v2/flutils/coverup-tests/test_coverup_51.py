# file: flutils/pathutils.py:387-414
# asked: {"lines": [387, 412, 413, 414], "branches": []}
# gained: {"lines": [387, 412, 413, 414], "branches": []}

import pytest
from pathlib import Path
from flutils.pathutils import find_paths, normalize_path

def test_find_paths(monkeypatch, tmp_path):
    # Setup temporary directory and files
    (tmp_path / "file_one").write_text("content")
    (tmp_path / "dir_one").mkdir()
    (tmp_path / "dir_one" / "file_two").write_text("content")

    # Mock normalize_path to return the tmp_path with a wildcard pattern
    def mock_normalize_path(path):
        return tmp_path / path

    monkeypatch.setattr("flutils.pathutils.normalize_path", mock_normalize_path)

    # Test find_paths
    result = list(find_paths("*/*"))
    expected = [
        tmp_path / "dir_one" / "file_two"
    ]

    assert sorted(result) == sorted(expected)

    # Cleanup
    for item in tmp_path.iterdir():
        if item.is_dir():
            for sub_item in item.iterdir():
                sub_item.unlink()
            item.rmdir()
        else:
            item.unlink()
