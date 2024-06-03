# file py_backwards/files.py:12-38
# lines [12, 15, 16, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38]
# branches ['15->16', '15->18', '18->19', '18->21', '21->22', '21->32', '22->23', '22->25', '26->27', '26->29', '35->exit', '35->36']

import pytest
from pathlib import Path
from py_backwards.files import get_input_output_paths, InvalidInputOutput, InputDoesntExists, InputOutput

def test_get_input_output_paths_invalid_input_output():
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths('input_dir', 'output.py', None))

def test_get_input_output_paths_input_doesnt_exist(mocker):
    mocker.patch('py_backwards.files.Path.exists', return_value=False)
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths('non_existent.py', 'output.py', None))

def test_get_input_output_paths_file_to_file(mocker):
    mocker.patch('py_backwards.files.Path.exists', return_value=True)
    result = list(get_input_output_paths('input.py', 'output.py', None))
    assert result == [InputOutput(Path('input.py'), Path('output.py'))]

def test_get_input_output_paths_file_to_dir_no_root(mocker):
    mocker.patch('py_backwards.files.Path.exists', return_value=True)
    result = list(get_input_output_paths('input.py', 'output_dir', None))
    assert result == [InputOutput(Path('input.py'), Path('output_dir/input.py'))]

def test_get_input_output_paths_file_to_dir_with_root(mocker):
    mocker.patch('py_backwards.files.Path.exists', return_value=True)
    result = list(get_input_output_paths('root/input.py', 'output_dir', 'root'))
    assert result == [InputOutput(Path('root/input.py'), Path('output_dir/input.py'))]

def test_get_input_output_paths_dir_to_dir(mocker):
    mocker.patch('py_backwards.files.Path.exists', return_value=True)
    mocker.patch('py_backwards.files.Path.glob', return_value=[Path('input_dir/file1.py'), Path('input_dir/subdir/file2.py')])
    result = list(get_input_output_paths('input_dir', 'output_dir', None))
    assert result == [
        InputOutput(Path('input_dir/file1.py'), Path('output_dir/file1.py')),
        InputOutput(Path('input_dir/subdir/file2.py'), Path('output_dir/subdir/file2.py'))
    ]

def test_get_input_output_paths_dir_to_dir_with_root(mocker):
    mocker.patch('py_backwards.files.Path.exists', return_value=True)
    mocker.patch('py_backwards.files.Path.glob', return_value=[Path('root/input_dir/file1.py'), Path('root/input_dir/subdir/file2.py')])
    result = list(get_input_output_paths('root/input_dir', 'output_dir', 'root'))
    assert result == [
        InputOutput(Path('root/input_dir/file1.py'), Path('output_dir/input_dir/file1.py')),
        InputOutput(Path('root/input_dir/subdir/file2.py'), Path('output_dir/input_dir/subdir/file2.py'))
    ]
