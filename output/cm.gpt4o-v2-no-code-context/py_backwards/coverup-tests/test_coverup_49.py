# file: py_backwards/compiler.py:54-74
# asked: {"lines": [56, 57, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74], "branches": []}
# gained: {"lines": [56, 57, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74], "branches": []}

import pytest
from unittest.mock import patch
from py_backwards.compiler import _compile_file, CompilationError
from py_backwards.types import InputOutput
from pathlib import Path

@pytest.fixture
def mock_paths(tmp_path):
    input_path = tmp_path / "input.py"
    output_path = tmp_path / "output.py"
    input_path.write_text("print('Hello, world!')")
    return InputOutput(input=input_path, output=output_path)

def test_compile_file_success(mock_paths):
    target = (3, 6)
    with patch("py_backwards.compiler._transform", return_value=("transformed_code", ["dep1", "dep2"])):
        dependencies = _compile_file(mock_paths, target)
        assert dependencies == ["dep1", "dep2"]
        assert mock_paths.output.read_text() == "transformed_code"

def test_compile_file_syntax_error(mock_paths):
    target = (3, 6)
    with patch("py_backwards.compiler._transform", side_effect=SyntaxError("invalid syntax", ("", 1, 1, ""))):
        with pytest.raises(CompilationError) as excinfo:
            _compile_file(mock_paths, target)
        assert excinfo.value.filename == mock_paths.input.as_posix()
        assert excinfo.value.lineno == 1
        assert excinfo.value.offset == 1

def test_compile_file_output_dir_exists(mock_paths):
    target = (3, 6)
    mock_paths.output.parent.mkdir(exist_ok=True)
    with patch("py_backwards.compiler._transform", return_value=("transformed_code", ["dep1", "dep2"])):
        dependencies = _compile_file(mock_paths, target)
        assert dependencies == ["dep1", "dep2"]
        assert mock_paths.output.read_text() == "transformed_code"
