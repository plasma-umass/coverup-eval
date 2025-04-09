# file: httpie/output/writer.py:19-51
# asked: {"lines": [19, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 38, 40, 41, 42, 44, 45, 46, 47, 49, 51], "branches": [[26, 27], [26, 28], [41, 42], [41, 44], [47, 49], [47, 51]]}
# gained: {"lines": [19, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 37, 38, 40, 41, 42, 44, 45, 46, 47, 49, 51], "branches": [[26, 28], [41, 42], [41, 44], [47, 49], [47, 51]]}

import pytest
import argparse
import errno
from unittest.mock import Mock, patch
import requests
from httpie.context import Environment
from httpie.output.writer import write_message

@pytest.fixture
def mock_env():
    env = Mock(spec=Environment)
    env.is_windows = False
    env.stdout_isatty = False
    env.stdout = Mock()
    env.stderr = Mock()
    return env

@pytest.fixture
def mock_args():
    args = Mock(spec=argparse.Namespace)
    args.stream = False
    args.prettify = []
    args.debug = False
    args.traceback = False
    return args

@pytest.fixture
def mock_request():
    return Mock(spec=requests.PreparedRequest)

@pytest.fixture
def mock_response():
    return Mock(spec=requests.Response)

@patch('httpie.output.writer.build_output_stream_for_message')
@patch('httpie.output.writer.write_stream')
def test_write_message_with_body(mock_write_stream, mock_build_output_stream, mock_env, mock_args, mock_response):
    mock_build_output_stream.return_value = iter([b'test'])
    write_message(mock_response, mock_env, mock_args, with_body=True)
    mock_build_output_stream.assert_called_once_with(
        args=mock_args,
        env=mock_env,
        requests_message=mock_response,
        with_body=True,
        with_headers=False
    )
    mock_write_stream.assert_called_once()

@patch('httpie.output.writer.build_output_stream_for_message')
@patch('httpie.output.writer.write_stream')
def test_write_message_with_headers(mock_write_stream, mock_build_output_stream, mock_env, mock_args, mock_response):
    mock_build_output_stream.return_value = iter([b'test'])
    write_message(mock_response, mock_env, mock_args, with_headers=True)
    mock_build_output_stream.assert_called_once_with(
        args=mock_args,
        env=mock_env,
        requests_message=mock_response,
        with_body=False,
        with_headers=True
    )
    mock_write_stream.assert_called_once()

@patch('httpie.output.writer.build_output_stream_for_message')
@patch('httpie.output.writer.write_stream_with_colors_win_py3')
def test_write_message_windows_with_colors(mock_write_stream_with_colors, mock_build_output_stream, mock_env, mock_args, mock_response):
    mock_env.is_windows = True
    mock_args.prettify = ['colors']
    mock_build_output_stream.return_value = iter([b'test'])
    write_message(mock_response, mock_env, mock_args, with_body=True)
    mock_build_output_stream.assert_called_once_with(
        args=mock_args,
        env=mock_env,
        requests_message=mock_response,
        with_body=True,
        with_headers=False
    )
    mock_write_stream_with_colors.assert_called_once()

@patch('httpie.output.writer.build_output_stream_for_message')
@patch('httpie.output.writer.write_stream')
def test_write_message_ioerror_broken_pipe(mock_write_stream, mock_build_output_stream, mock_env, mock_args, mock_response):
    mock_write_stream.side_effect = IOError(errno.EPIPE, 'Broken pipe')
    write_message(mock_response, mock_env, mock_args, with_body=True)
    mock_env.stderr.write.assert_called_once_with('\n')

@patch('httpie.output.writer.build_output_stream_for_message')
@patch('httpie.output.writer.write_stream')
def test_write_message_ioerror_other(mock_write_stream, mock_build_output_stream, mock_env, mock_args, mock_response):
    mock_write_stream.side_effect = IOError(errno.EACCES, 'Permission denied')
    with pytest.raises(IOError):
        write_message(mock_response, mock_env, mock_args, with_body=True)
