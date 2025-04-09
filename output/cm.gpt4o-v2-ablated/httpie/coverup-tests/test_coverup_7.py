# file: httpie/output/writer.py:19-51
# asked: {"lines": [19, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 38, 40, 41, 42, 44, 45, 46, 47, 49, 51], "branches": [[26, 27], [26, 28], [41, 42], [41, 44], [47, 49], [47, 51]]}
# gained: {"lines": [19, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 38, 40, 41, 42, 44, 45, 46, 47, 49, 51], "branches": [[26, 27], [26, 28], [41, 42], [41, 44], [47, 49], [47, 51]]}

import pytest
import argparse
import requests
import errno
from unittest.mock import Mock, patch
from httpie.output.writer import write_message

@pytest.fixture
def env():
    mock_env = Mock()
    mock_env.is_windows = False
    mock_env.stdout_isatty = False
    mock_env.stdout = Mock()
    mock_env.stderr = Mock()
    return mock_env

@pytest.fixture
def args():
    mock_args = Mock()
    mock_args.stream = False
    mock_args.prettify = []
    mock_args.debug = False
    mock_args.traceback = False
    return mock_args

@pytest.fixture
def request_message():
    return Mock(spec=requests.PreparedRequest)

@pytest.fixture
def response_message():
    return Mock(spec=requests.Response)

def test_write_message_no_body_no_headers(env, args, request_message):
    write_message(request_message, env, args, with_headers=False, with_body=False)
    env.stdout.write.assert_not_called()

def test_write_message_with_body(env, args, request_message):
    with patch('httpie.output.writer.build_output_stream_for_message') as mock_build_stream, \
         patch('httpie.output.writer.write_stream') as mock_write_stream:
        mock_build_stream.return_value = Mock()
        write_message(request_message, env, args, with_headers=False, with_body=True)
        mock_write_stream.assert_called_once()

def test_write_message_with_headers(env, args, request_message):
    with patch('httpie.output.writer.build_output_stream_for_message') as mock_build_stream, \
         patch('httpie.output.writer.write_stream') as mock_write_stream:
        mock_build_stream.return_value = Mock()
        write_message(request_message, env, args, with_headers=True, with_body=False)
        mock_write_stream.assert_called_once()

def test_write_message_windows_with_colors(env, args, request_message):
    env.is_windows = True
    args.prettify = ['colors']
    with patch('httpie.output.writer.build_output_stream_for_message') as mock_build_stream, \
         patch('httpie.output.writer.write_stream_with_colors_win_py3') as mock_write_stream_with_colors:
        mock_build_stream.return_value = Mock()
        write_message(request_message, env, args, with_headers=True, with_body=False)
        mock_write_stream_with_colors.assert_called_once()

def test_write_message_ioerror_broken_pipe(env, args, request_message):
    with patch('httpie.output.writer.build_output_stream_for_message') as mock_build_stream, \
         patch('httpie.output.writer.write_stream', side_effect=IOError(errno.EPIPE, 'Broken pipe')):
        mock_build_stream.return_value = Mock()
        write_message(request_message, env, args, with_headers=True, with_body=False)
        env.stderr.write.assert_called_once_with('\n')

def test_write_message_ioerror_other(env, args, request_message):
    with patch('httpie.output.writer.build_output_stream_for_message') as mock_build_stream, \
         patch('httpie.output.writer.write_stream', side_effect=IOError(errno.EACCES, 'Permission denied')):
        mock_build_stream.return_value = Mock()
        with pytest.raises(IOError):
            write_message(request_message, env, args, with_headers=True, with_body=False)
