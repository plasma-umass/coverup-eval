# file: httpie/output/streams.py:89-115
# asked: {"lines": [89, 90, 97, 99, 100, 101, 103, 106, 108, 110, 111, 112, 113, 114, 115], "branches": [[101, 103], [101, 106], [111, 0], [111, 112], [112, 113], [112, 114]]}
# gained: {"lines": [89, 90, 97, 99, 100, 101, 103, 106, 108, 110, 111, 112, 113, 114, 115], "branches": [[101, 103], [101, 106], [111, 0], [111, 112], [112, 113], [112, 114]]}

import pytest
from httpie.output.streams import EncodedStream, BinarySuppressedError
from httpie.context import Environment
from unittest.mock import Mock

class MockMessage:
    def __init__(self, lines, encoding='utf8'):
        self.lines = lines
        self.encoding = encoding

    def iter_lines(self, chunk_size):
        for line in self.lines:
            yield line, b'\n'

@pytest.fixture
def mock_env():
    env = Mock(spec=Environment)
    env.stdout_isatty = True
    env.stdout_encoding = 'utf8'
    return env

@pytest.fixture
def mock_msg():
    return MockMessage([b'line1', b'line2'])

def test_encoded_stream_tty(mock_env, mock_msg):
    stream = EncodedStream(env=mock_env, msg=mock_msg)
    body = list(stream.iter_body())
    assert body == [b'line1\n', b'line2\n']
    assert stream.output_encoding == 'utf8'

def test_encoded_stream_non_tty(mock_msg):
    env = Mock(spec=Environment)
    env.stdout_isatty = False
    stream = EncodedStream(env=env, msg=mock_msg)
    body = list(stream.iter_body())
    assert body == [b'line1\n', b'line2\n']
    assert stream.output_encoding == 'utf8'

def test_encoded_stream_binary_suppressed_error(mock_msg):
    mock_msg.lines = [b'line1', b'line2\0']
    env = Mock(spec=Environment)
    env.stdout_isatty = False
    stream = EncodedStream(env=env, msg=mock_msg)
    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())
