# file: httpie/output/streams.py:89-115
# asked: {"lines": [111, 112, 113, 114, 115], "branches": [[111, 0], [111, 112], [112, 113], [112, 114]]}
# gained: {"lines": [111, 112, 113, 114, 115], "branches": [[111, 0], [111, 112], [112, 113], [112, 114]]}

import pytest
from httpie.output.streams import EncodedStream, BinarySuppressedError
from httpie.context import Environment
from httpie.models import HTTPMessage

class MockHTTPMessage:
    def __init__(self, encoding='utf8'):
        self.encoding = encoding

    def iter_lines(self, chunk_size):
        return [
            (b'line1\n', b'\n'),
            (b'line3\n', b'\n')
        ]

class MockHTTPMessageWithBinary:
    def __init__(self, encoding='utf8'):
        self.encoding = encoding

    def iter_lines(self, chunk_size):
        return [
            (b'line1\n', b'\n'),
            (b'line2\0\n', b'\n'),  # This line contains a null byte to trigger BinarySuppressedError
            (b'line3\n', b'\n')
        ]

def test_encoded_stream_stdout_isatty(monkeypatch):
    env = Environment(stdout_isatty=True, stdout_encoding='ascii')
    msg = MockHTTPMessage()
    stream = EncodedStream(env=env, msg=msg)

    assert stream.output_encoding == 'ascii'

def test_encoded_stream_stdout_not_isatty(monkeypatch):
    env = Environment(stdout_isatty=False)
    msg = MockHTTPMessage(encoding='latin1')
    stream = EncodedStream(env=env, msg=msg)

    assert stream.output_encoding == 'latin1'

def test_iter_body_no_binary_data(monkeypatch):
    env = Environment(stdout_isatty=True, stdout_encoding='ascii')
    msg = MockHTTPMessage()
    stream = EncodedStream(env=env, msg=msg)

    body = list(stream.iter_body())
    assert body == [b'line1\n\n', b'line3\n\n']

def test_iter_body_with_binary_data(monkeypatch):
    env = Environment(stdout_isatty=True, stdout_encoding='ascii')
    msg = MockHTTPMessageWithBinary()
    stream = EncodedStream(env=env, msg=msg)

    with pytest.raises(BinarySuppressedError):
        body = list(stream.iter_body())
