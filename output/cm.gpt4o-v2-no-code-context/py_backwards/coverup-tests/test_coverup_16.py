# file: py_backwards/files.py:12-38
# asked: {"lines": [12, 15, 16, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38], "branches": [[15, 16], [15, 18], [18, 19], [18, 21], [21, 22], [21, 32], [22, 23], [22, 25], [26, 27], [26, 29], [35, 0], [35, 36]]}
# gained: {"lines": [12, 15, 16, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38], "branches": [[15, 16], [15, 18], [18, 19], [18, 21], [21, 22], [21, 32], [22, 23], [22, 25], [26, 27], [26, 29], [35, 0], [35, 36]]}

import pytest
from pathlib import Path
from py_backwards.files import get_input_output_paths, InvalidInputOutput, InputDoesntExists, InputOutput

def test_get_input_output_paths_invalid_input_output():
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('input_dir', 'output.py', None))

def test_get_input_output_paths_input_doesnt_exist():
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('non_existent.py', 'output_dir', None))

def test_get_input_output_paths_single_file_to_file():
    input_file = 'test_input.py'
    output_file = 'test_output.py'
    Path(input_file).touch()
    try:
        result = list(get_input_output_paths(input_file, output_file, None))
        assert result == [InputOutput(Path(input_file), Path(output_file))]
    finally:
        Path(input_file).unlink()

def test_get_input_output_paths_single_file_to_dir():
    input_file = 'test_input.py'
    output_dir = 'test_output_dir'
    Path(input_file).touch()
    Path(output_dir).mkdir()
    try:
        result = list(get_input_output_paths(input_file, output_dir, None))
        assert result == [InputOutput(Path(input_file), Path(output_dir).joinpath(input_file))]
    finally:
        Path(input_file).unlink()
        Path(output_dir).rmdir()

def test_get_input_output_paths_single_file_to_dir_with_root():
    input_file = 'root_dir/test_input.py'
    output_dir = 'test_output_dir'
    root_dir = 'root_dir'
    Path(root_dir).mkdir()
    Path(input_file).touch()
    Path(output_dir).mkdir()
    try:
        result = list(get_input_output_paths(input_file, output_dir, root_dir))
        assert result == [InputOutput(Path(input_file), Path(output_dir).joinpath('test_input.py'))]
    finally:
        Path(input_file).unlink()
        Path(output_dir).rmdir()
        Path(root_dir).rmdir()

def test_get_input_output_paths_dir_to_dir():
    input_dir = 'test_input_dir'
    output_dir = 'test_output_dir'
    Path(input_dir).mkdir()
    Path(output_dir).mkdir()
    (Path(input_dir) / 'file1.py').touch()
    (Path(input_dir) / 'file2.py').touch()
    try:
        result = list(get_input_output_paths(input_dir, output_dir, None))
        expected = [
            InputOutput(Path(input_dir) / 'file1.py', Path(output_dir) / 'file1.py'),
            InputOutput(Path(input_dir) / 'file2.py', Path(output_dir) / 'file2.py')
        ]
        assert result == expected
    finally:
        for file in Path(input_dir).glob('*.py'):
            file.unlink()
        Path(input_dir).rmdir()
        Path(output_dir).rmdir()

def test_get_input_output_paths_dir_to_dir_with_root():
    input_dir = 'root_dir/test_input_dir'
    output_dir = 'test_output_dir'
    root_dir = 'root_dir'
    Path(root_dir).mkdir()
    Path(input_dir).mkdir(parents=True)
    Path(output_dir).mkdir()
    (Path(input_dir) / 'file1.py').touch()
    (Path(input_dir) / 'file2.py').touch()
    try:
        result = list(get_input_output_paths(input_dir, output_dir, root_dir))
        expected = [
            InputOutput(Path(input_dir) / 'file1.py', Path(output_dir) / 'test_input_dir/file1.py'),
            InputOutput(Path(input_dir) / 'file2.py', Path(output_dir) / 'test_input_dir/file2.py')
        ]
        assert result == expected
    finally:
        for file in Path(input_dir).glob('*.py'):
            file.unlink()
        Path(input_dir).rmdir()
        Path(output_dir).rmdir()
        Path(root_dir).rmdir()
