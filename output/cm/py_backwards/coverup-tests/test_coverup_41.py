# file py_backwards/files.py:12-38
# lines [22, 23, 25, 26, 27, 29, 30]
# branches ['21->22', '22->23', '22->25', '26->27', '26->29']

import pytest
from pathlib import Path
from py_backwards.files import get_input_output_paths, InputOutput, InvalidInputOutput, InputDoesntExists

def test_get_input_output_paths_single_file_to_dir_with_root(mocker, tmp_path):
    # Setup: create a temporary input file, output directory, and root directory within tmp_path
    tmp_root_dir = tmp_path / 'temp_root_dir'
    tmp_root_dir.mkdir()  # Create the root directory
    tmp_input_file = tmp_root_dir / 'temp_input.py'
    tmp_output_dir = tmp_path / 'temp_output_dir'
    tmp_input_file.touch()  # Create the file
    tmp_output_dir.mkdir()  # Create the output directory

    # Mock the Path.exists method to always return True
    mocker.patch.object(Path, 'exists', return_value=True)

    # Test: Call the function with a single .py file, a directory as output, and a root directory
    result = list(get_input_output_paths(str(tmp_input_file), str(tmp_output_dir), str(tmp_root_dir)))

    # Verify: Check that the result is as expected
    expected_output_path = tmp_output_dir.joinpath(tmp_input_file.relative_to(tmp_root_dir))
    assert result == [InputOutput(tmp_input_file, expected_output_path)]

    # Cleanup is handled by pytest using the tmp_path fixture
