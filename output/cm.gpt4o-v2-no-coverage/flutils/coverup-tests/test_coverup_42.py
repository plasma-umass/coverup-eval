# file: flutils/pathutils.py:387-414
# asked: {"lines": [387, 412, 413, 414], "branches": []}
# gained: {"lines": [387, 412, 413, 414], "branches": []}

import pytest
from pathlib import Path
from flutils.pathutils import find_paths, normalize_path

def test_find_paths_with_glob_pattern(monkeypatch, tmp_path):
    # Setup temporary directory and files
    (tmp_path / "file_one").touch()
    (tmp_path / "file_two").touch()
    (tmp_path / "dir_one").mkdir()
    (tmp_path / "dir_one" / "file_three").touch()

    # Mock the home directory to the temporary path
    monkeypatch.setenv("HOME", str(tmp_path))

    # Test the find_paths function
    result = list(find_paths('~/file_*'))
    expected = [tmp_path / "file_one", tmp_path / "file_two"]
    assert sorted(result) == sorted(expected)

    result = list(find_paths('~/dir_one/*'))
    expected = [tmp_path / "dir_one" / "file_three"]
    assert sorted(result) == sorted(expected)

def test_find_paths_with_absolute_path(monkeypatch, tmp_path):
    # Setup temporary directory and files
    (tmp_path / "file_one").touch()
    (tmp_path / "file_two").touch()

    # Test the find_paths function with absolute path
    result = list(find_paths(str(tmp_path / "file_*")))
    expected = [tmp_path / "file_one", tmp_path / "file_two"]
    assert sorted(result) == sorted(expected)

def test_find_paths_with_relative_path(monkeypatch, tmp_path):
    # Setup temporary directory and files
    (tmp_path / "file_one").touch()
    (tmp_path / "file_two").touch()

    # Change the current working directory to the temporary path
    monkeypatch.chdir(tmp_path)

    # Test the find_paths function with relative path
    result = list(find_paths('file_*'))
    expected = [tmp_path / "file_one", tmp_path / "file_two"]
    assert sorted(result) == sorted(expected)

def test_normalize_path_with_bytes():
    path = b'~/tmp/foo/../bar'
    expected = Path.home() / 'tmp' / 'bar'
    assert normalize_path(path) == expected

def test_normalize_path_with_str():
    path = '~/tmp/foo/../bar'
    expected = Path.home() / 'tmp' / 'bar'
    assert normalize_path(path) == expected

def test_normalize_path_with_pathlib_path():
    path = Path('~/tmp/foo/../bar')
    expected = Path.home() / 'tmp' / 'bar'
    assert normalize_path(path) == expected

def test_normalize_path_with_env_variable(monkeypatch):
    monkeypatch.setenv('TEST_PATH', 'tmp/foo')
    path = '$TEST_PATH/../bar'
    expected = Path.cwd() / 'tmp' / 'bar'
    assert normalize_path(path) == expected

def test_normalize_path_with_relative_path(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    path = 'foo/../bar'
    expected = tmp_path / 'bar'
    assert normalize_path(path) == expected
