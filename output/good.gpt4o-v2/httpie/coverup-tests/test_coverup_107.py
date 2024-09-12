# file: httpie/output/writer.py:19-51
# asked: {"lines": [27], "branches": [[26, 27]]}
# gained: {"lines": [27], "branches": [[26, 27]]}

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
    env.stdout = Mock()
    env.stderr = Mock()
    env.stdout_isatty = False
    env.is_windows = False
    return env

@pytest.fixture
def mock_args():
    args = Mock(spec=argparse.Namespace)
    args.stream = False
    args.prettify = []
    args.debug = False
    args.traceback = False
    return args

def test_write_message_no_headers_no_body(mock_env, mock_args):
    request_message = Mock(spec=requests.PreparedRequest)
    write_message(request_message, mock_env, mock_args, with_headers=False, with_body=False)
    mock_env.stdout.write.assert_not_called()
    mock_env.stderr.write.assert_not_called()

def test_write_message_with_headers(mock_env, mock_args):
    request_message = Mock(spec=requests.PreparedRequest)
    with patch('httpie.output.writer.build_output_stream_for_message', return_value=Mock()) as mock_build_stream, \
         patch('httpie.output.writer.write_stream') as mock_write_stream:
        write_message(request_message, mock_env, mock_args, with_headers=True, with_body=False)
        mock_build_stream.assert_called_once()
        mock_write_stream.assert_called_once()

def test_write_message_with_body(mock_env, mock_args):
    request_message = Mock(spec=requests.PreparedRequest)
    with patch('httpie.output.writer.build_output_stream_for_message', return_value=Mock()) as mock_build_stream, \
         patch('httpie.output.writer.write_stream') as mock_write_stream:
        write_message(request_message, mock_env, mock_args, with_headers=False, with_body=True)
        mock_build_stream.assert_called_once()
        mock_write_stream.assert_called_once()

def test_write_message_ioerror_broken_pipe(mock_env, mock_args):
    request_message = Mock(spec=requests.PreparedRequest)
    with patch('httpie.output.writer.build_output_stream_for_message', return_value=Mock()) as mock_build_stream, \
         patch('httpie.output.writer.write_stream', side_effect=IOError(errno.EPIPE, "Broken pipe")) as mock_write_stream:
        write_message(request_message, mock_env, mock_args, with_headers=True, with_body=False)
        mock_env.stderr.write.assert_called_once_with('\n')

def test_write_message_ioerror_other(mock_env, mock_args):
    request_message = Mock(spec=requests.PreparedRequest)
    with patch('httpie.output.writer.build_output_stream_for_message', return_value=Mock()) as mock_build_stream, \
         patch('httpie.output.writer.write_stream', side_effect=IOError(errno.EACCES, "Permission denied")) as mock_write_stream:
        with pytest.raises(IOError):
            write_message(request_message, mock_env, mock_args, with_headers=True, with_body=False)
