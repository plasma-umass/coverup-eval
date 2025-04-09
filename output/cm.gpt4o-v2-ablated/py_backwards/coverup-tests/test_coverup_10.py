# file: py_backwards/files.py:12-38
# asked: {"lines": [12, 15, 16, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38], "branches": [[15, 16], [15, 18], [18, 19], [18, 21], [21, 22], [21, 32], [22, 23], [22, 25], [26, 27], [26, 29], [35, 0], [35, 36]]}
# gained: {"lines": [12, 15, 16, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38], "branches": [[15, 16], [15, 18], [18, 19], [18, 21], [21, 22], [21, 32], [22, 23], [22, 25], [26, 27], [26, 29], [35, 0], [35, 36]]}

import pytest
from pathlib import Path
from py_backwards.files import get_input_output_paths, InvalidInputOutput, InputDoesntExists, InputOutput

def test_get_input_output_paths_invalid_input_output():
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('input_dir', 'output.py', None))

def test_get_input_output_paths_input_doesnt_exist(monkeypatch):
    def mock_path_exists(path):
        return False

    monkeypatch.setattr(Path, 'exists', mock_path_exists)
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('input.py', 'output_dir', None))

def test_get_input_output_paths_single_file_to_file(monkeypatch):
    def mock_path_exists(path):
        return True

    monkeypatch.setattr(Path, 'exists', mock_path_exists)
    input_output = list(get_input_output_paths('input.py', 'output.py', None))
    assert len(input_output) == 1
    assert input_output[0] == InputOutput(Path('input.py'), Path('output.py'))

def test_get_input_output_paths_single_file_to_dir(monkeypatch):
    def mock_path_exists(path):
        return True

    monkeypatch.setattr(Path, 'exists', mock_path_exists)
    input_output = list(get_input_output_paths('input.py', 'output_dir', None))
    assert len(input_output) == 1
    assert input_output[0] == InputOutput(Path('input.py'), Path('output_dir/input.py'))

def test_get_input_output_paths_single_file_to_dir_with_root(monkeypatch):
    def mock_path_exists(path):
        return True

    monkeypatch.setattr(Path, 'exists', mock_path_exists)
    input_output = list(get_input_output_paths('root/input.py', 'output_dir', 'root'))
    assert len(input_output) == 1
    assert input_output[0] == InputOutput(Path('root/input.py'), Path('output_dir/input.py'))

def test_get_input_output_paths_dir_to_dir(monkeypatch):
    def mock_path_exists(path):
        return True

    def mock_path_glob(path, pattern):
        return [Path('input_dir/file1.py'), Path('input_dir/subdir/file2.py')]

    monkeypatch.setattr(Path, 'exists', mock_path_exists)
    monkeypatch.setattr(Path, 'glob', mock_path_glob)
    input_output = list(get_input_output_paths('input_dir', 'output_dir', None))
    assert len(input_output) == 2
    assert input_output[0] == InputOutput(Path('input_dir/file1.py'), Path('output_dir/file1.py'))
    assert input_output[1] == InputOutput(Path('input_dir/subdir/file2.py'), Path('output_dir/subdir/file2.py'))

def test_get_input_output_paths_dir_to_dir_with_root(monkeypatch):
    def mock_path_exists(path):
        return True

    def mock_path_glob(path, pattern):
        return [Path('root/input_dir/file1.py'), Path('root/input_dir/subdir/file2.py')]

    monkeypatch.setattr(Path, 'exists', mock_path_exists)
    monkeypatch.setattr(Path, 'glob', mock_path_glob)
    input_output = list(get_input_output_paths('root/input_dir', 'output_dir', 'root'))
    assert len(input_output) == 2
    assert input_output[0] == InputOutput(Path('root/input_dir/file1.py'), Path('output_dir/input_dir/file1.py'))
    assert input_output[1] == InputOutput(Path('root/input_dir/subdir/file2.py'), Path('output_dir/input_dir/subdir/file2.py'))
