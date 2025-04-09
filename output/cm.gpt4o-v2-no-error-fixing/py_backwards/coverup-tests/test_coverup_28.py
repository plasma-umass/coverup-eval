# file: py_backwards/main.py:12-54
# asked: {"lines": [12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54], "branches": [[32, 33], [32, 53]]}
# gained: {"lines": [12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54], "branches": [[32, 33], [32, 53]]}

import pytest
from unittest.mock import patch, MagicMock
from py_backwards.main import main
from py_backwards import exceptions

def test_main_success(monkeypatch):
    mock_args = MagicMock()
    mock_args.input = ['input.py']
    mock_args.output = 'output.py'
    mock_args.target = '3.6'
    mock_args.root = None
    mock_args.debug = False

    monkeypatch.setattr('sys.argv', ['main', '-i', 'input.py', '-o', 'output.py', '-t', '3.6'])

    with patch('py_backwards.main.init_settings') as mock_init_settings, \
         patch('py_backwards.main.compile_files') as mock_compile_files, \
         patch('py_backwards.main.messages.compilation_result') as mock_compilation_result:
        
        mock_compile_files.return_value = MagicMock()
        mock_compilation_result.return_value = "Compilation succeed"

        result = main()

        mock_init_settings.assert_called_once()
        mock_compile_files.assert_called_once_with('input.py', 'output.py', (3, 6), None)
        mock_compilation_result.assert_called_once()
        assert result == 0

def test_main_compilation_error(monkeypatch):
    mock_args = MagicMock()
    mock_args.input = ['input.py']
    mock_args.output = 'output.py'
    mock_args.target = '3.6'
    mock_args.root = None
    mock_args.debug = False

    monkeypatch.setattr('sys.argv', ['main', '-i', 'input.py', '-o', 'output.py', '-t', '3.6'])

    with patch('py_backwards.main.init_settings'), \
         patch('py_backwards.main.compile_files', side_effect=exceptions.CompilationError('file.py', 'code', 1, 1)), \
         patch('py_backwards.main.messages.syntax_error') as mock_syntax_error:
        
        mock_syntax_error.return_value = "Syntax error"

        result = main()

        mock_syntax_error.assert_called_once()
        assert result == 1

def test_main_transformation_error(monkeypatch):
    mock_args = MagicMock()
    mock_args.input = ['input.py']
    mock_args.output = 'output.py'
    mock_args.target = '3.6'
    mock_args.root = None
    mock_args.debug = False

    monkeypatch.setattr('sys.argv', ['main', '-i', 'input.py', '-o', 'output.py', '-t', '3.6'])

    with patch('py_backwards.main.init_settings'), \
         patch('py_backwards.main.compile_files', side_effect=exceptions.TransformationError('file.py', MagicMock(), 'ast', 'traceback')), \
         patch('py_backwards.main.messages.transformation_error') as mock_transformation_error:
        
        mock_transformation_error.return_value = "Transformation error"

        result = main()

        mock_transformation_error.assert_called_once()
        assert result == 1

def test_main_input_doesnt_exist(monkeypatch):
    mock_args = MagicMock()
    mock_args.input = ['input.py']
    mock_args.output = 'output.py'
    mock_args.target = '3.6'
    mock_args.root = None
    mock_args.debug = False

    monkeypatch.setattr('sys.argv', ['main', '-i', 'input.py', '-o', 'output.py', '-t', '3.6'])

    with patch('py_backwards.main.init_settings'), \
         patch('py_backwards.main.compile_files', side_effect=exceptions.InputDoesntExists), \
         patch('py_backwards.main.messages.input_doesnt_exists') as mock_input_doesnt_exists:
        
        mock_input_doesnt_exists.return_value = "Input doesn't exist"

        result = main()

        mock_input_doesnt_exists.assert_called_once()
        assert result == 1

def test_main_invalid_input_output(monkeypatch):
    mock_args = MagicMock()
    mock_args.input = ['input.py']
    mock_args.output = 'output.py'
    mock_args.target = '3.6'
    mock_args.root = None
    mock_args.debug = False

    monkeypatch.setattr('sys.argv', ['main', '-i', 'input.py', '-o', 'output.py', '-t', '3.6'])

    with patch('py_backwards.main.init_settings'), \
         patch('py_backwards.main.compile_files', side_effect=exceptions.InvalidInputOutput), \
         patch('py_backwards.main.messages.invalid_output') as mock_invalid_output:
        
        mock_invalid_output.return_value = "Invalid output"

        result = main()

        mock_invalid_output.assert_called_once()
        assert result == 1

def test_main_permission_error(monkeypatch):
    mock_args = MagicMock()
    mock_args.input = ['input.py']
    mock_args.output = 'output.py'
    mock_args.target = '3.6'
    mock_args.root = None
    mock_args.debug = False

    monkeypatch.setattr('sys.argv', ['main', '-i', 'input.py', '-o', 'output.py', '-t', '3.6'])

    with patch('py_backwards.main.init_settings'), \
         patch('py_backwards.main.compile_files', side_effect=PermissionError), \
         patch('py_backwards.main.messages.permission_error') as mock_permission_error:
        
        mock_permission_error.return_value = "Permission denied"

        result = main()

        mock_permission_error.assert_called_once()
        assert result == 1
