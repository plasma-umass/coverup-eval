# file py_backwards/compiler.py:54-74
# lines [54, 56, 57, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74]
# branches []

import pytest
from unittest.mock import patch
from py_backwards.compiler import _compile_file, CompilationError

class InputOutput:
    def __init__(self, input_path, output_path):
        self.input = input_path
        self.output = output_path

class MockCompilationTarget:
    pass

@pytest.fixture
def mock_paths(tmp_path):
    input_path = tmp_path / "input.py"
    output_path = tmp_path / "output.py"
    input_path.write_text("print('Hello, world!')")
    return InputOutput(input_path, output_path)

@pytest.fixture
def mock_target():
    return MockCompilationTarget()

def test_compile_file_success(mock_paths, mock_target):
    with patch('py_backwards.compiler._transform', return_value=("transformed_code", ["dependency1"])) as mock_transform:
        dependencies = _compile_file(mock_paths, mock_target)
        assert dependencies == ["dependency1"]
        assert mock_paths.output.read_text() == "transformed_code"
        mock_transform.assert_called_once_with(mock_paths.input.as_posix(), "print('Hello, world!')", mock_target)

def test_compile_file_syntax_error(mock_paths, mock_target):
    with patch('py_backwards.compiler._transform', side_effect=SyntaxError("invalid syntax", ("", 1, 1, "print('Hello, world!')"))):
        with pytest.raises(CompilationError) as excinfo:
            _compile_file(mock_paths, mock_target)
        assert excinfo.value.filename == mock_paths.input.as_posix()
        assert excinfo.value.lineno == 1
        assert excinfo.value.offset == 1

def test_compile_file_output_dir_exists(mock_paths, mock_target):
    mock_paths.output.parent.mkdir(exist_ok=True)
    with patch('py_backwards.compiler._transform', return_value=("transformed_code", ["dependency1"])):
        dependencies = _compile_file(mock_paths, mock_target)
        assert dependencies == ["dependency1"]
        assert mock_paths.output.read_text() == "transformed_code"
