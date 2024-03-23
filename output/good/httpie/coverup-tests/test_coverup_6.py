# file httpie/output/streams.py:89-115
# lines [89, 90, 97, 99, 100, 101, 103, 106, 108, 110, 111, 112, 113, 114, 115]
# branches ['101->103', '101->106', '111->exit', '111->112', '112->113', '112->114']

import pytest
from httpie.output.streams import EncodedStream, BinarySuppressedError
from httpie.context import Environment
from httpie.models import HTTPMessage

@pytest.fixture
def mock_env_stdout_isatty(mocker):
    mock_env = mocker.Mock(spec=Environment)
    mock_env.stdout_isatty = True
    mock_env.stdout_encoding = 'utf8'
    return mock_env

@pytest.fixture
def mock_env_stdout_not_isatty(mocker):
    mock_env = mocker.Mock(spec=Environment)
    mock_env.stdout_isatty = False
    mock_env.stdout_encoding = None
    return mock_env

@pytest.fixture
def mock_msg(mocker):
    mock_msg = mocker.Mock(spec=HTTPMessage)
    mock_msg.encoding = 'utf8'
    mock_msg.iter_lines.return_value = [(b'line', b'\n')]
    return mock_msg

def test_encoded_stream_with_tty(mock_env_stdout_isatty, mock_msg):
    stream = EncodedStream(env=mock_env_stdout_isatty, msg=mock_msg)
    body = list(stream.iter_body())
    assert body == [b'line\n']

def test_encoded_stream_without_tty(mock_env_stdout_not_isatty, mock_msg):
    stream = EncodedStream(env=mock_env_stdout_not_isatty, msg=mock_msg)
    body = list(stream.iter_body())
    assert body == [b'line\n']

def test_encoded_stream_raises_binary_suppressed_error(mock_env_stdout_isatty, mocker):
    mock_msg = mocker.Mock(spec=HTTPMessage)
    mock_msg.encoding = 'utf8'
    mock_msg.iter_lines.return_value = [(b'line\0', b'\n')]
    stream = EncodedStream(env=mock_env_stdout_isatty, msg=mock_msg)
    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())
