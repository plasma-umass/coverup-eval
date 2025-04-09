# file: py_backwards/compiler.py:77-87
# asked: {"lines": [77, 78, 80, 81, 82, 83, 84, 85, 86, 87], "branches": [[83, 84], [83, 86]]}
# gained: {"lines": [77, 78, 80, 81, 82, 83, 84, 85, 86, 87], "branches": [[83, 84], [83, 86]]}

import pytest
from unittest.mock import patch, mock_open, MagicMock
from py_backwards.compiler import compile_files
from py_backwards.types import CompilationTarget, CompilationResult
from py_backwards.exceptions import CompilationError

@pytest.fixture
def mock_get_input_output_paths():
    with patch('py_backwards.compiler.get_input_output_paths') as mock:
        yield mock

@pytest.fixture
def mock_compile_file():
    with patch('py_backwards.compiler._compile_file') as mock:
        yield mock

def test_compile_files_single_file(mock_get_input_output_paths, mock_compile_file):
    mock_get_input_output_paths.return_value = [MagicMock(input='input.py', output='output.py')]
    mock_compile_file.return_value = ['dependency1', 'dependency2']
    
    result = compile_files('input.py', 'output.py', (3, 6))
    
    assert result.files == 1
    assert result.target == (3, 6)
    assert result.dependencies == ['dependency1', 'dependency2']
    assert result.time > 0

def test_compile_files_multiple_files(mock_get_input_output_paths, mock_compile_file):
    mock_get_input_output_paths.return_value = [
        MagicMock(input='input1.py', output='output1.py'),
        MagicMock(input='input2.py', output='output2.py')
    ]
    mock_compile_file.side_effect = [['dependency1'], ['dependency2']]
    
    result = compile_files('input_dir', 'output_dir', (3, 6))
    
    assert result.files == 2
    assert result.target == (3, 6)
    assert result.dependencies == ['dependency1', 'dependency2']
    assert result.time > 0

def test_compile_files_no_files(mock_get_input_output_paths, mock_compile_file):
    mock_get_input_output_paths.return_value = []
    
    result = compile_files('input_dir', 'output_dir', (3, 6))
    
    assert result.files == 0
    assert result.target == (3, 6)
    assert result.dependencies == []
    assert result.time > 0

def test_compile_files_with_root(mock_get_input_output_paths, mock_compile_file):
    mock_get_input_output_paths.return_value = [MagicMock(input='root/input.py', output='output.py')]
    mock_compile_file.return_value = ['dependency1']
    
    result = compile_files('root/input.py', 'output.py', (3, 6), root='root')
    
    assert result.files == 1
    assert result.target == (3, 6)
    assert result.dependencies == ['dependency1']
    assert result.time > 0

def test_compile_files_compilation_error(mock_get_input_output_paths, mock_compile_file):
    mock_get_input_output_paths.return_value = [MagicMock(input='input.py', output='output.py')]
    mock_compile_file.side_effect = CompilationError('input.py', 'code', 1, 1)
    
    with pytest.raises(CompilationError):
        compile_files('input.py', 'output.py', (3, 6))
