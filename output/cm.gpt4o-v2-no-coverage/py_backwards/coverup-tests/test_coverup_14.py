# file: py_backwards/files.py:12-38
# asked: {"lines": [12, 15, 16, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38], "branches": [[15, 16], [15, 18], [18, 19], [18, 21], [21, 22], [21, 32], [22, 23], [22, 25], [26, 27], [26, 29], [35, 0], [35, 36]]}
# gained: {"lines": [12, 15, 16, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38], "branches": [[15, 16], [15, 18], [18, 19], [18, 21], [21, 22], [21, 32], [22, 23], [22, 25], [26, 27], [26, 29], [35, 0], [35, 36]]}

import pytest
from pathlib import Path
from py_backwards.files import get_input_output_paths
from py_backwards.exceptions import InvalidInputOutput, InputDoesntExists
from py_backwards.types import InputOutput

def test_get_input_output_paths_invalid_input_output():
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths("input_dir", "output.py", None))

def test_get_input_output_paths_input_doesnt_exist(tmp_path):
    non_existent_path = tmp_path / "non_existent.py"
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths(str(non_existent_path), "output_dir", None))

def test_get_input_output_paths_single_file_to_file(tmp_path):
    input_file = tmp_path / "input.py"
    output_file = tmp_path / "output.py"
    input_file.touch()
    result = list(get_input_output_paths(str(input_file), str(output_file), None))
    assert result == [InputOutput(input_file, output_file)]

def test_get_input_output_paths_single_file_to_dir(tmp_path):
    input_file = tmp_path / "input.py"
    output_dir = tmp_path / "output_dir"
    output_dir.mkdir()
    input_file.touch()
    result = list(get_input_output_paths(str(input_file), str(output_dir), None))
    assert result == [InputOutput(input_file, output_dir / "input.py")]

def test_get_input_output_paths_single_file_to_dir_with_root(tmp_path):
    input_file = tmp_path / "root" / "input.py"
    output_dir = tmp_path / "output_dir"
    input_file.parent.mkdir()
    output_dir.mkdir()
    input_file.touch()
    result = list(get_input_output_paths(str(input_file), str(output_dir), str(tmp_path / "root")))
    assert result == [InputOutput(input_file, output_dir / "input.py")]

def test_get_input_output_paths_dir_to_dir(tmp_path):
    input_dir = tmp_path / "input_dir"
    output_dir = tmp_path / "output_dir"
    input_dir.mkdir()
    output_dir.mkdir()
    (input_dir / "file1.py").touch()
    (input_dir / "subdir" / "file2.py").mkdir(parents=True, exist_ok=True)
    (input_dir / "subdir" / "file2.py").touch()
    result = list(get_input_output_paths(str(input_dir), str(output_dir), None))
    expected = [
        InputOutput(input_dir / "file1.py", output_dir / "file1.py"),
        InputOutput(input_dir / "subdir" / "file2.py", output_dir / "subdir" / "file2.py")
    ]
    assert result == expected
