# file py_backwards/compiler.py:77-87
# lines [77, 78, 80, 81, 82, 83, 84, 85, 86, 87]
# branches ['83->84', '83->86']

import os
from unittest.mock import patch
from py_backwards.compiler import compile_files, CompilationResult
import pytest
from typing import NamedTuple

class MockCompilationTarget(NamedTuple):
    PY36 = ('py36',)

@pytest.fixture
def cleanup_files():
    created_files = []
    yield created_files
    for file in created_files:
        if os.path.exists(file):
            if os.path.isdir(file):
                os.rmdir(file)
            else:
                os.remove(file)

def test_compile_files(cleanup_files, mocker):
    input_dir = 'test_input_dir'
    output_dir = 'test_output_dir'
    target = MockCompilationTarget.PY36
    root = None

    # Create test directories and files
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    input_file = os.path.join(input_dir, 'test_file.py')
    output_file = os.path.join(output_dir, 'test_file.py')
    with open(input_file, 'w') as f:
        f.write('print("Hello, World!")')
    cleanup_files.extend([input_file, output_file, input_dir, output_dir])

    # Mock the _compile_file function to return an empty set
    mocker.patch('py_backwards.compiler._compile_file', return_value=set())

    # Run the compile_files function
    result = compile_files(input_=input_dir, output=output_dir, target=target, root=root)

    # Check the CompilationResult
    assert isinstance(result, CompilationResult)
    assert result.files == 1
    assert result.target == target
    assert result.dependencies == []
