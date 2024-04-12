# file httpie/output/writer.py:19-51
# lines [27, 42]
# branches ['26->27', '41->42']

import argparse
import errno
import pytest
from httpie.output.writer import write_message
from httpie.context import Environment
from unittest.mock import Mock

@pytest.fixture
def mock_env_stdout(mocker):
    mock_stdout = mocker.patch('httpie.output.writer.Environment.stdout', new_callable=Mock)
    mock_stdout.isatty.return_value = True
    return mock_stdout

@pytest.fixture
def mock_env_stderr(mocker):
    mock_stderr = mocker.patch('httpie.output.writer.Environment.stderr', new_callable=Mock)
    return mock_stderr

@pytest.fixture
def mock_write_stream_with_colors_win_py3(mocker):
    return mocker.patch('httpie.output.writer.write_stream_with_colors_win_py3')

@pytest.fixture
def mock_write_stream(mocker):
    return mocker.patch('httpie.output.writer.write_stream')

@pytest.fixture
def mock_build_output_stream_for_message(mocker):
    return mocker.patch('httpie.output.writer.build_output_stream_for_message')

@pytest.fixture
def mock_requests_message(mocker):
    return mocker.Mock()

@pytest.fixture
def mock_args(mocker):
    args = argparse.Namespace()
    args.prettify = 'colors'
    args.stream = False
    args.debug = False
    args.traceback = False
    return args

@pytest.fixture
def mock_env(mock_env_stdout, mock_env_stderr):
    return Environment(stdout=mock_env_stdout, stderr=mock_env_stderr)

def test_write_message_no_body_no_headers(mock_env, mock_args, mock_requests_message):
    write_message(mock_requests_message, mock_env, mock_args)
    mock_env.stdout.write.assert_not_called()

def test_write_message_windows_colors(mock_env, mock_args, mock_requests_message, mock_write_stream_with_colors_win_py3, mock_build_output_stream_for_message):
    mock_args.prettify = 'colors'
    mock_env.is_windows = True
    write_message(mock_requests_message, mock_env, mock_args, with_headers=True)
    mock_write_stream_with_colors_win_py3.assert_called_once()

def test_write_message_broken_pipe(mock_env, mock_args, mock_requests_message, mock_write_stream, mock_build_output_stream_for_message):
    mock_write_stream.side_effect = OSError(errno.EPIPE, 'Broken pipe')
    mock_args.traceback = False
    write_message(mock_requests_message, mock_env, mock_args, with_headers=True)
    mock_env.stderr.write.assert_called_once_with('\n')
