# file: py_backwards/main.py:12-54
# asked: {"lines": [12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54], "branches": [[32, 33], [32, 53]]}
# gained: {"lines": [12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54], "branches": [[32, 33], [32, 53]]}

import pytest
from unittest.mock import patch, MagicMock
from py_backwards.main import main
import sys

@pytest.fixture
def mock_init_settings():
    with patch('py_backwards.main.init_settings') as mock:
        yield mock

@pytest.fixture
def mock_compile_files():
    with patch('py_backwards.main.compile_files') as mock:
        yield mock

@pytest.fixture
def mock_const_targets():
    with patch('py_backwards.main.const.TARGETS', {'3.6': 'target_3.6'}):
        yield

@pytest.fixture
def mock_messages():
    with patch('py_backwards.main.messages') as mock:
        yield mock

@pytest.fixture
def mock_exceptions():
    with patch('py_backwards.main.exceptions') as mock:
        mock.CompilationError = type('CompilationError', (Exception,), {})
        mock.TransformationError = type('TransformationError', (Exception,), {})
        mock.InputDoesntExists = type('InputDoesntExists', (Exception,), {})
        mock.InvalidInputOutput = type('InvalidInputOutput', (Exception,), {})
        yield mock

def test_main_success(mock_init_settings, mock_compile_files, mock_const_targets, mock_messages):
    test_args = ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.6']
    with patch.object(sys, 'argv', test_args):
        mock_compile_files.return_value = 'success'
        result = main()
        assert result == 0
        mock_compile_files.assert_called_once_with('input.py', 'output.py', 'target_3.6', None)
        mock_messages.compilation_result.assert_called_once_with('success')

def test_main_compilation_error(mock_init_settings, mock_compile_files, mock_const_targets, mock_messages, mock_exceptions):
    test_args = ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.6']
    with patch.object(sys, 'argv', test_args):
        mock_compile_files.side_effect = mock_exceptions.CompilationError('error')
        result = main()
        assert result == 1
        mock_messages.syntax_error.assert_called_once()

def test_main_transformation_error(mock_init_settings, mock_compile_files, mock_const_targets, mock_messages, mock_exceptions):
    test_args = ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.6']
    with patch.object(sys, 'argv', test_args):
        mock_compile_files.side_effect = mock_exceptions.TransformationError('error')
        result = main()
        assert result == 1
        mock_messages.transformation_error.assert_called_once()

def test_main_input_doesnt_exist(mock_init_settings, mock_compile_files, mock_const_targets, mock_messages, mock_exceptions):
    test_args = ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.6']
    with patch.object(sys, 'argv', test_args):
        mock_compile_files.side_effect = mock_exceptions.InputDoesntExists()
        result = main()
        assert result == 1
        mock_messages.input_doesnt_exists.assert_called_once()

def test_main_invalid_input_output(mock_init_settings, mock_compile_files, mock_const_targets, mock_messages, mock_exceptions):
    test_args = ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.6']
    with patch.object(sys, 'argv', test_args):
        mock_compile_files.side_effect = mock_exceptions.InvalidInputOutput()
        result = main()
        assert result == 1
        mock_messages.invalid_output.assert_called_once()

def test_main_permission_error(mock_init_settings, mock_compile_files, mock_const_targets, mock_messages):
    test_args = ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.6']
    with patch.object(sys, 'argv', test_args):
        mock_compile_files.side_effect = PermissionError()
        result = main()
        assert result == 1
        mock_messages.permission_error.assert_called_once()
