# file: flutils/pathutils.py:387-414
# asked: {"lines": [387, 412, 413, 414], "branches": []}
# gained: {"lines": [387, 412, 413, 414], "branches": []}

import pytest
from pathlib import Path
from flutils.pathutils import find_paths
from flutils import normalize_path

@pytest.fixture
def mock_normalize_path(monkeypatch):
    def mock_normalize(path):
        return Path(path).expanduser()
    monkeypatch.setattr('flutils.pathutils.normalize_path', mock_normalize)

def test_find_paths_no_match(mock_normalize_path, tmp_path):
    pattern = tmp_path / 'nonexistent*'
    result = list(find_paths(pattern))
    assert result == []

def test_find_paths_single_file(mock_normalize_path, tmp_path):
    file = tmp_path / 'file.txt'
    file.touch()
    pattern = tmp_path / 'file*'
    result = list(find_paths(pattern))
    assert result == [file]

def test_find_paths_multiple_files(mock_normalize_path, tmp_path):
    file1 = tmp_path / 'file1.txt'
    file2 = tmp_path / 'file2.txt'
    file1.touch()
    file2.touch()
    pattern = tmp_path / 'file*'
    result = list(find_paths(pattern))
    assert set(result) == {file1, file2}

def test_find_paths_subdirectories(mock_normalize_path, tmp_path):
    subdir = tmp_path / 'subdir'
    subdir.mkdir()
    file = subdir / 'file.txt'
    file.touch()
    pattern = tmp_path / '**' / 'file*'
    result = list(find_paths(pattern))
    assert result == [file]
