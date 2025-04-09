# file: httpie/context.py:60-86
# asked: {"lines": [60, 66, 67, 70, 71, 74, 75, 76, 77, 78, 79, 81, 82, 84, 85, 86], "branches": [[74, 75], [74, 77], [77, 0], [77, 78], [79, 81], [79, 85], [82, 84], [82, 85]]}
# gained: {"lines": [60, 66, 67, 70, 71, 74, 75, 76, 77, 78, 79, 81, 82, 84, 85, 86], "branches": [[74, 75], [77, 78], [79, 81], [79, 85], [82, 84]]}

import pytest
from unittest.mock import Mock, patch
from httpie.context import Environment
from httpie.compat import is_windows

@pytest.fixture
def mock_streams():
    stdin = Mock()
    stdout = Mock()
    stderr = Mock()
    stdin.isatty.return_value = True
    stdout.isatty.return_value = True
    stderr.isatty.return_value = True
    stdin.encoding = 'utf-8'
    stdout.encoding = 'utf-8'
    stderr.encoding = 'utf-8'
    return stdin, stdout, stderr

def test_environment_initialization(mock_streams):
    stdin, stdout, stderr = mock_streams
    env = Environment(stdin=stdin, stdout=stdout, stderr=stderr)
    assert env.stdin == stdin
    assert env.stdout == stdout
    assert env.stderr == stderr
    assert env.stdin_encoding == 'utf-8'
    assert env.stdout_encoding == 'utf-8'
    assert env._orig_stderr == stderr

def test_environment_initialization_with_kwargs(mock_streams):
    stdin, stdout, stderr = mock_streams
    env = Environment(stdin=stdin, stdout=stdout, stderr=stderr, program_name='test_http')
    assert env.program_name == 'test_http'

def test_environment_initialization_with_devnull(mock_streams):
    stdin, stdout, stderr = mock_streams
    devnull = Mock()
    env = Environment(stdin=stdin, stdout=stdout, stderr=stderr, devnull=devnull)
    assert env._devnull == devnull

@patch('httpie.context.is_windows', True)
def test_environment_initialization_windows(mock_streams):
    from colorama import AnsiToWin32
    stdin, stdout, stderr = mock_streams
    wrapped_stdout = AnsiToWin32(stdout)
    env = Environment(stdin=stdin, stdout=wrapped_stdout, stderr=stderr)
    assert env.stdout_encoding == 'utf-8'

@patch('httpie.context.is_windows', False)
def test_environment_initialization_non_windows(mock_streams):
    stdin, stdout, stderr = mock_streams
    env = Environment(stdin=stdin, stdout=stdout, stderr=stderr)
    assert env.stdout_encoding == 'utf-8'
