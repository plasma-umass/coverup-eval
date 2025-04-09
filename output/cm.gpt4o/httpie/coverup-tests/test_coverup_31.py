# file httpie/output/writer.py:19-51
# lines [19, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 38, 40, 41, 42, 44, 45, 46, 47, 49, 51]
# branches ['26->27', '26->28', '41->42', '41->44', '47->49', '47->51']

import pytest
import argparse
import requests
import errno
from unittest.mock import Mock, patch
from httpie.output.writer import write_message
from httpie.context import Environment

@pytest.fixture
def mock_env(mocker):
    env = mocker.Mock(spec=Environment)
    env.stdout = mocker.Mock()
    env.stderr = mocker.Mock()
    env.stdout_isatty = False
    env.is_windows = False
    return env

@pytest.fixture
def mock_args(mocker):
    args = mocker.Mock(spec=argparse.Namespace)
    args.stream = False
    args.prettify = []
    args.debug = False
    args.traceback = False
    return args

def test_write_message_with_body(mock_env, mock_args, mocker):
    mock_request = mocker.Mock(spec=requests.PreparedRequest)
    mocker.patch('httpie.output.writer.build_output_stream_for_message', return_value=Mock())
    mock_write_stream = mocker.patch('httpie.output.writer.write_stream')

    write_message(mock_request, mock_env, mock_args, with_body=True)

    assert mock_write_stream.called

def test_write_message_with_headers(mock_env, mock_args, mocker):
    mock_request = mocker.Mock(spec=requests.PreparedRequest)
    mocker.patch('httpie.output.writer.build_output_stream_for_message', return_value=Mock())
    mock_write_stream = mocker.patch('httpie.output.writer.write_stream')

    write_message(mock_request, mock_env, mock_args, with_headers=True)

    assert mock_write_stream.called

def test_write_message_windows_with_colors(mock_env, mock_args, mocker):
    mock_request = mocker.Mock(spec=requests.PreparedRequest)
    mock_env.is_windows = True
    mock_args.prettify = ['colors']
    mocker.patch('httpie.output.writer.build_output_stream_for_message', return_value=Mock())
    mock_write_stream_with_colors = mocker.patch('httpie.output.writer.write_stream_with_colors_win_py3')

    write_message(mock_request, mock_env, mock_args, with_body=True)

    assert mock_write_stream_with_colors.called

def test_write_message_ioerror_broken_pipe(mock_env, mock_args, mocker):
    mock_request = mocker.Mock(spec=requests.PreparedRequest)
    mocker.patch('httpie.output.writer.build_output_stream_for_message', return_value=Mock())
    mocker.patch('httpie.output.writer.write_stream', side_effect=IOError(errno.EPIPE, 'Broken pipe'))

    write_message(mock_request, mock_env, mock_args, with_body=True)

    mock_env.stderr.write.assert_called_once_with('\n')

def test_write_message_ioerror_other(mock_env, mock_args, mocker):
    mock_request = mocker.Mock(spec=requests.PreparedRequest)
    mocker.patch('httpie.output.writer.build_output_stream_for_message', return_value=Mock())
    mocker.patch('httpie.output.writer.write_stream', side_effect=IOError(errno.EACCES, 'Permission denied'))

    with pytest.raises(IOError):
        write_message(mock_request, mock_env, mock_args, with_body=True)
