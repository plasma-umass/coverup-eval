# file: flutils/pathutils.py:387-414
# asked: {"lines": [387, 412, 413, 414], "branches": []}
# gained: {"lines": [387, 412, 413, 414], "branches": []}

import pytest
from pathlib import Path
from flutils.pathutils import find_paths
from flutils.pathutils import normalize_path

def test_find_paths(monkeypatch, tmp_path):
    # Setup temporary directory and files
    (tmp_path / "file_one").write_text("content")
    (tmp_path / "file_two").write_text("content")
    (tmp_path / "dir_one").mkdir()
    (tmp_path / "dir_one" / "file_three").write_text("content")

    # Mock normalize_path to return the tmp_path
    def mock_normalize_path(path):
        return tmp_path / path

    monkeypatch.setattr("flutils.pathutils.normalize_path", mock_normalize_path)

    # Test find_paths
    result = list(find_paths("*"))
    expected = [
        tmp_path / "file_one",
        tmp_path / "file_two",
        tmp_path / "dir_one",
    ]
    assert sorted(result) == sorted(expected)

    result = list(find_paths("dir_one/*"))
    expected = [
        tmp_path / "dir_one" / "file_three",
    ]
    assert sorted(result) == sorted(expected)
