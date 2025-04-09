# file py_backwards/files.py:12-38
# lines [23, 27]
# branches ['22->23', '26->27']

import pytest
from py_backwards.files import get_input_output_paths, InputOutput, InvalidInputOutput, InputDoesntExists
from pathlib import Path
from unittest.mock import MagicMock

@pytest.fixture
def mock_path_exists(mocker):
    mocker.patch.object(Path, 'exists', return_value=True)

def test_get_input_output_paths_single_file_to_dir(mock_path_exists, tmp_path):
    input_file = tmp_path / 'input.py'
    input_file.touch()
    output_dir = tmp_path / 'output'
    output_dir.mkdir()
    root = None

    paths = list(get_input_output_paths(str(input_file), str(output_dir), root))

    assert len(paths) == 1
    assert paths[0].input == input_file
    assert paths[0].output == output_dir / 'input.py'

def test_get_input_output_paths_single_file_to_dir_with_root(mock_path_exists, tmp_path):
    root_dir = tmp_path / 'root'
    root_dir.mkdir()
    input_file = root_dir / 'input.py'
    input_file.touch()
    output_dir = tmp_path / 'output'
    output_dir.mkdir()
    root = str(root_dir)

    paths = list(get_input_output_paths(str(input_file), str(output_dir), root))

    assert len(paths) == 1
    assert paths[0].input == input_file
    assert paths[0].output == output_dir / 'input.py'
