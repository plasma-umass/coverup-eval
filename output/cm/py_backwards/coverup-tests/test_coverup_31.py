# file py_backwards/files.py:12-38
# lines [12, 15, 16, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38]
# branches ['15->16', '15->18', '18->19', '18->21', '21->22', '21->32', '22->23', '22->25', '26->27', '26->29', '35->exit', '35->36']

import os
import pytest
from pathlib import Path
from py_backwards.files import get_input_output_paths, InputOutput, InvalidInputOutput, InputDoesntExists

def test_get_input_output_paths_directory_to_directory_without_root(tmp_path):
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    output_dir.mkdir()

    # Create a Python file in the input directory
    input_file = input_dir / "test.py"
    input_file.touch()

    # Create a nested Python file in the input directory
    nested_dir = input_dir / "nested"
    nested_dir.mkdir()
    nested_input_file = nested_dir / "nested_test.py"
    nested_input_file.touch()

    # Call the function with directory paths
    paths = list(get_input_output_paths(str(input_dir), str(output_dir), None))

    # Check that the paths are correct
    expected_output_file = output_dir / "test.py"
    expected_nested_output_file = output_dir / "nested" / "nested_test.py"
    assert paths == [
        InputOutput(input_file, expected_output_file),
        InputOutput(nested_input_file, expected_nested_output_file)
    ]

def test_get_input_output_paths_directory_to_directory_with_root(tmp_path):
    root_dir = tmp_path
    input_dir = root_dir / "input"
    output_dir = root_dir / "output"
    input_dir.mkdir()
    output_dir.mkdir()

    # Create a Python file in the input directory
    input_file = input_dir / "test.py"
    input_file.touch()

    # Create a nested Python file in the input directory
    nested_dir = input_dir / "nested"
    nested_dir.mkdir()
    nested_input_file = nested_dir / "nested_test.py"
    nested_input_file.touch()

    # Call the function with directory paths and a root
    paths = list(get_input_output_paths(str(input_dir), str(output_dir), str(root_dir)))

    # Check that the paths are correct
    expected_output_file = output_dir / "input" / "test.py"
    expected_nested_output_file = output_dir / "input" / "nested" / "nested_test.py"
    assert paths == [
        InputOutput(input_file, expected_output_file),
        InputOutput(nested_input_file, expected_nested_output_file)
    ]

def test_get_input_output_paths_invalid_input_output_combination(tmp_path):
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.py"
    input_file.touch()

    with pytest.raises(InvalidInputOutput):
        next(get_input_output_paths(str(input_file), str(output_file), None))

def test_get_input_output_paths_input_does_not_exist(tmp_path):
    input_file = tmp_path / "nonexistent.py"
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    with pytest.raises(InputDoesntExists):
        next(get_input_output_paths(str(input_file), str(output_dir), None))
