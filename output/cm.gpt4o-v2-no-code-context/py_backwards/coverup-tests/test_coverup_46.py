# file: py_backwards/compiler.py:77-87
# asked: {"lines": [80, 81, 82, 83, 84, 85, 86, 87], "branches": [[83, 84], [83, 86]]}
# gained: {"lines": [80, 81, 82, 83, 84, 85, 86, 87], "branches": [[83, 84], [83, 86]]}

import pytest
from unittest.mock import patch, MagicMock
from py_backwards.compiler import compile_files, CompilationResult

class CompilationTarget:
    PY37 = 'py37'

@pytest.fixture
def mock_time(monkeypatch):
    mock_time = MagicMock()
    monkeypatch.setattr('py_backwards.compiler.time', mock_time)
    return mock_time

@pytest.fixture
def mock_get_input_output_paths(monkeypatch):
    mock_paths = MagicMock(return_value=[('input_path', 'output_path')])
    monkeypatch.setattr('py_backwards.compiler.get_input_output_paths', mock_paths)
    return mock_paths

@pytest.fixture
def mock_compile_file(monkeypatch):
    mock_compile = MagicMock(return_value={'dependency1', 'dependency2'})
    monkeypatch.setattr('py_backwards.compiler._compile_file', mock_compile)
    return mock_compile

def test_compile_files(mock_time, mock_get_input_output_paths, mock_compile_file):
    mock_time.side_effect = [1, 2]  # Simulate time() calls

    input_ = 'input_dir'
    output = 'output_dir'
    target = CompilationTarget.PY37
    result = compile_files(input_, output, target)

    assert result.files == 1
    assert result.time == 1
    assert result.target == target
    assert result.dependencies == ['dependency1', 'dependency2']

    mock_get_input_output_paths.assert_called_once_with(input_, output, None)
    mock_compile_file.assert_called_once_with(('input_path', 'output_path'), target)
