# file httpie/output/writer.py:19-51
# lines [19, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 38, 40, 41, 42, 44, 45, 46, 47, 49, 51]
# branches ['26->27', '26->28', '41->42', '41->44', '47->49', '47->51']

import argparse
import errno
import pytest
from httpie.output.writer import write_message
from httpie.context import Environment
from unittest.mock import Mock

@pytest.fixture
def mock_env(mocker):
    mock_env = Environment()
    mock_env.stdout = mocker.Mock()
    mock_env.stderr = mocker.Mock()
    mock_env.stdout_isatty = False
    mock_env.is_windows = False
    return mock_env

@pytest.fixture
def mock_args():
    args = argparse.Namespace()
    args.prettify = ''
    args.stream = False
    args.debug = False
    args.traceback = False
    return args

def test_write_message_ioerror_not_traceback_not_e_pipe(mock_env, mock_args, mocker):
    mock_env.is_windows = False
    mock_args.prettify = 'none'
    mock_requests_message = Mock()
    mocker.patch('httpie.output.writer.write_stream', side_effect=IOError(errno.EIO, 'mock IO error'))
    with pytest.raises(IOError):
        write_message(
            requests_message=mock_requests_message,
            env=mock_env,
            args=mock_args,
            with_headers=True,
            with_body=False
        )
    mock_env.stderr.write.assert_not_called()

def test_write_message_ioerror_not_traceback_e_pipe(mock_env, mock_args, mocker):
    mock_env.is_windows = False
    mock_args.prettify = 'none'
    mock_requests_message = Mock()
    mocker.patch('httpie.output.writer.write_stream', side_effect=IOError(errno.EPIPE, 'mock broken pipe'))
    write_message(
        requests_message=mock_requests_message,
        env=mock_env,
        args=mock_args,
        with_headers=True,
        with_body=False
    )
    mock_env.stderr.write.assert_called_once_with('\n')
