# file: py_backwards/main.py:12-54
# asked: {"lines": [12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54], "branches": [[32, 33], [32, 53]]}
# gained: {"lines": [12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54], "branches": [[32, 33], [32, 53]]}

import pytest
from unittest import mock
from py_backwards.main import main
from py_backwards import exceptions
from py_backwards.types import CompilationResult

def test_main_success(monkeypatch):
    mock_args = mock.Mock()
    mock_args.input = ['input.py']
    mock_args.output = 'output.py'
    mock_args.target = '3.6'
    mock_args.root = None
    mock_args.debug = False

    monkeypatch.setattr('sys.argv', ['main', '-i', 'input.py', '-o', 'output.py', '-t', '3.6'])
    monkeypatch.setattr('py_backwards.main.init_settings', lambda x: None)
    mock_result = CompilationResult(files=1, time=0.1, target=(3, 6), dependencies=[])
    monkeypatch.setattr('py_backwards.main.compile_files', lambda *args, **kwargs: mock_result)

    result = main()
    assert result == 0

def test_main_compilation_error(monkeypatch):
    mock_args = mock.Mock()
    mock_args.input = ['input.py']
    mock_args.output = 'output.py'
    mock_args.target = '3.6'
    mock_args.root = None
    mock_args.debug = False

    monkeypatch.setattr('sys.argv', ['main', '-i', 'input.py', '-o', 'output.py', '-t', '3.6'])
    monkeypatch.setattr('py_backwards.main.init_settings', lambda x: None)
    monkeypatch.setattr('py_backwards.main.compile_files', mock.Mock(side_effect=exceptions.CompilationError('file.py', 'code', 1, 1)))

    result = main()
    assert result == 1

def test_main_transformation_error(monkeypatch):
    mock_args = mock.Mock()
    mock_args.input = ['input.py']
    mock_args.output = 'output.py'
    mock_args.target = '3.6'
    mock_args.root = None
    mock_args.debug = False

    monkeypatch.setattr('sys.argv', ['main', '-i', 'input.py', '-o', 'output.py', '-t', '3.6'])
    monkeypatch.setattr('py_backwards.main.init_settings', lambda x: None)
    transformer_mock = mock.Mock()
    transformer_mock.__name__ = 'MockTransformer'
    monkeypatch.setattr('py_backwards.main.compile_files', mock.Mock(side_effect=exceptions.TransformationError('file.py', transformer_mock, 'ast', 'traceback')))

    result = main()
    assert result == 1

def test_main_input_doesnt_exist(monkeypatch):
    mock_args = mock.Mock()
    mock_args.input = ['input.py']
    mock_args.output = 'output.py'
    mock_args.target = '3.6'
    mock_args.root = None
    mock_args.debug = False

    monkeypatch.setattr('sys.argv', ['main', '-i', 'input.py', '-o', 'output.py', '-t', '3.6'])
    monkeypatch.setattr('py_backwards.main.init_settings', lambda x: None)
    monkeypatch.setattr('py_backwards.main.compile_files', mock.Mock(side_effect=exceptions.InputDoesntExists))

    result = main()
    assert result == 1

def test_main_invalid_input_output(monkeypatch):
    mock_args = mock.Mock()
    mock_args.input = ['input.py']
    mock_args.output = 'output.py'
    mock_args.target = '3.6'
    mock_args.root = None
    mock_args.debug = False

    monkeypatch.setattr('sys.argv', ['main', '-i', 'input.py', '-o', 'output.py', '-t', '3.6'])
    monkeypatch.setattr('py_backwards.main.init_settings', lambda x: None)
    monkeypatch.setattr('py_backwards.main.compile_files', mock.Mock(side_effect=exceptions.InvalidInputOutput))

    result = main()
    assert result == 1

def test_main_permission_error(monkeypatch):
    mock_args = mock.Mock()
    mock_args.input = ['input.py']
    mock_args.output = 'output.py'
    mock_args.target = '3.6'
    mock_args.root = None
    mock_args.debug = False

    monkeypatch.setattr('sys.argv', ['main', '-i', 'input.py', '-o', 'output.py', '-t', '3.6'])
    monkeypatch.setattr('py_backwards.main.init_settings', lambda x: None)
    monkeypatch.setattr('py_backwards.main.compile_files', mock.Mock(side_effect=PermissionError))

    result = main()
    assert result == 1
