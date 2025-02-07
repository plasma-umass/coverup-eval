# file: py_backwards/compiler.py:54-74
# asked: {"lines": [54, 56, 57, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74], "branches": []}
# gained: {"lines": [54, 56, 57, 59, 60, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74], "branches": []}

import pytest
from pathlib import Path
from py_backwards.compiler import _compile_file
from py_backwards.files import InputOutput
from py_backwards.exceptions import CompilationError

def test_compile_file_success(tmp_path):
    input_file = tmp_path / "input.py"
    output_file = tmp_path / "output.py"
    input_file.write_text("print('Hello, World!')")

    paths = InputOutput(input=input_file, output=output_file)
    target = (3, 6)  # CompilationTarget is a tuple, not a class

    dependencies = _compile_file(paths, target)

    assert output_file.exists()
    assert output_file.read_text() == "print('Hello, World!')\n"
    assert dependencies == []

def test_compile_file_syntax_error(tmp_path):
    input_file = tmp_path / "input.py"
    output_file = tmp_path / "output.py"
    input_file.write_text("print('Hello, World!'\n")

    paths = InputOutput(input=input_file, output=output_file)
    target = (3, 6)  # CompilationTarget is a tuple, not a class

    with pytest.raises(CompilationError) as excinfo:
        _compile_file(paths, target)

    assert excinfo.value.filename == str(input_file)
    assert excinfo.value.lineno == 1

def test_compile_file_output_dir_exists(tmp_path):
    input_file = tmp_path / "input.py"
    output_file = tmp_path / "output_dir/output.py"
    input_file.write_text("print('Hello, World!')")

    output_file.parent.mkdir()
    paths = InputOutput(input=input_file, output=output_file)
    target = (3, 6)  # CompilationTarget is a tuple, not a class

    dependencies = _compile_file(paths, target)

    assert output_file.exists()
    assert output_file.read_text() == "print('Hello, World!')\n"
    assert dependencies == []
