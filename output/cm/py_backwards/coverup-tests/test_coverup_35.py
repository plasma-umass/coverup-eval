# file py_backwards/main.py:12-54
# lines [12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54]
# branches ['32->33', '32->53']

import sys
from unittest.mock import patch, MagicMock
from py_backwards.main import main
import pytest
from py_backwards import exceptions, const, messages

@pytest.fixture
def mock_init_settings(mocker):
    return mocker.patch('py_backwards.main.init_settings')

@pytest.fixture
def mock_compile_files(mocker):
    return mocker.patch('py_backwards.main.compile_files')

@pytest.fixture
def mock_print(mocker):
    return mocker.patch('builtins.print')

def test_main_with_compilation_error(mock_init_settings, mock_compile_files, mock_print):
    mock_compile_files.side_effect = exceptions.CompilationError('test error', 'code', 1, 1)
    with patch.object(sys, 'argv', ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.5']):
        assert main() == 1
    mock_print.assert_called_with(messages.syntax_error(mock_compile_files.side_effect), file=sys.stderr)

def test_main_with_transformation_error(mock_init_settings, mock_compile_files, mock_print):
    transformer_mock = MagicMock()
    transformer_mock.__name__ = 'MockTransformer'
    mock_compile_files.side_effect = exceptions.TransformationError('test error', transformer_mock, 'ast', 'traceback')
    with patch.object(sys, 'argv', ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.5']):
        assert main() == 1
    mock_print.assert_called_with(messages.transformation_error(mock_compile_files.side_effect), file=sys.stderr)

def test_main_with_input_doesnt_exists(mock_init_settings, mock_compile_files, mock_print):
    mock_compile_files.side_effect = exceptions.InputDoesntExists()
    with patch.object(sys, 'argv', ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.5']):
        assert main() == 1
    mock_print.assert_called_with(messages.input_doesnt_exists(['input.py']), file=sys.stderr)

def test_main_with_invalid_input_output(mock_init_settings, mock_compile_files, mock_print):
    mock_compile_files.side_effect = exceptions.InvalidInputOutput()
    with patch.object(sys, 'argv', ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.5']):
        assert main() == 1
    mock_print.assert_called_with(messages.invalid_output(['input.py'], 'output.py'), file=sys.stderr)

def test_main_with_permission_error(mock_init_settings, mock_compile_files, mock_print):
    mock_compile_files.side_effect = PermissionError()
    with patch.object(sys, 'argv', ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.5']):
        assert main() == 1
    mock_print.assert_called_with(messages.permission_error('output.py'), file=sys.stderr)

def test_main_success(mock_init_settings, mock_compile_files, mock_print):
    mock_result = MagicMock(dependencies=[], compiled='', target=(3, 5), files=['output.py'], time=0.1)
    mock_compile_files.return_value = mock_result
    with patch.object(sys, 'argv', ['py-backwards', '-i', 'input.py', '-o', 'output.py', '-t', '3.5']):
        assert main() == 0
    mock_print.assert_called_with(messages.compilation_result(mock_result))
