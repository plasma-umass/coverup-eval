# file: py_backwards/compiler.py:54-74
# asked: {"lines": [54, 56, 57, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74], "branches": []}
# gained: {"lines": [54, 56, 57, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74], "branches": []}

import pytest
from unittest.mock import mock_open, patch
from pathlib import Path
from py_backwards.compiler import _compile_file
from py_backwards.files import InputOutput
from py_backwards.types import CompilationTarget
from py_backwards.exceptions import CompilationError

# Mock _transform function
def mock_transform(path, code, target):
    return ("transformed_code", ["dependency1", "dependency2"])

@pytest.fixture
def input_output(tmp_path):
    input_path = tmp_path / "input.py"
    output_path = tmp_path / "output.py"
    input_path.write_text("print('Hello, world!')")
    return InputOutput(input=input_path, output=output_path)

def test_compile_file_success(input_output, monkeypatch):
    monkeypatch.setattr("py_backwards.compiler._transform", mock_transform)
    
    dependencies = _compile_file(input_output, (3, 6))
    
    assert dependencies == ["dependency1", "dependency2"]
    assert input_output.output.read_text() == "transformed_code"

def test_compile_file_syntax_error(input_output, monkeypatch):
    def mock_transform_syntax_error(path, code, target):
        raise SyntaxError("invalid syntax", ("<string>", 1, 7, "print('Hello, world!')"))
    
    monkeypatch.setattr("py_backwards.compiler._transform", mock_transform_syntax_error)
    
    with pytest.raises(CompilationError) as excinfo:
        _compile_file(input_output, (3, 6))
    
    assert excinfo.value.filename == str(input_output.input)
    assert excinfo.value.lineno == 1
    assert excinfo.value.offset == 7

def test_compile_file_file_exists_error(input_output, monkeypatch):
    def mock_mkdir(self, parents=True, exist_ok=False):
        raise FileExistsError
    
    monkeypatch.setattr(Path, "mkdir", mock_mkdir)
    monkeypatch.setattr("py_backwards.compiler._transform", mock_transform)
    
    dependencies = _compile_file(input_output, (3, 6))
    
    assert dependencies == ["dependency1", "dependency2"]
    assert input_output.output.read_text() == "transformed_code"
