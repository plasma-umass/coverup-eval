# file: httpie/output/streams.py:89-115
# asked: {"lines": [100, 101, 103, 106, 108, 111, 112, 113, 114, 115], "branches": [[101, 103], [101, 106], [111, 0], [111, 112], [112, 113], [112, 114]]}
# gained: {"lines": [100, 101, 103, 106, 108, 111, 112, 113, 114, 115], "branches": [[101, 103], [101, 106], [111, 0], [111, 112], [112, 113], [112, 114]]}

import pytest
from httpie.output.streams import EncodedStream, BinarySuppressedError
from httpie.context import Environment
from unittest.mock import Mock

class MockMessage:
    def __init__(self, encoding='utf8'):
        self.encoding = encoding

    def iter_lines(self, chunk_size):
        return [
            (b'line1\n', b'\n'),
            (b'line2\0\n', b'\n'),  # This line contains a null byte
            (b'line3\n', b'\n')
        ]

def test_encoded_stream_stdout_isatty(monkeypatch):
    env = Environment()
    monkeypatch.setattr(env, 'stdout_isatty', True)
    monkeypatch.setattr(env, 'stdout_encoding', 'ascii')
    msg = MockMessage()
    stream = EncodedStream(env=env, msg=msg)
    
    assert stream.output_encoding == 'ascii'

def test_encoded_stream_stdout_not_isatty(monkeypatch):
    env = Environment()
    monkeypatch.setattr(env, 'stdout_isatty', False)
    msg = MockMessage(encoding='latin1')
    stream = EncodedStream(env=env, msg=msg)
    
    assert stream.output_encoding == 'latin1'

def test_encoded_stream_default_encoding(monkeypatch):
    env = Environment()
    monkeypatch.setattr(env, 'stdout_isatty', False)
    msg = MockMessage(encoding=None)
    stream = EncodedStream(env=env, msg=msg)
    
    assert stream.output_encoding == 'utf8'

def test_iter_body(monkeypatch):
    env = Environment()
    monkeypatch.setattr(env, 'stdout_isatty', False)
    msg = MockMessage()
    msg.iter_lines = Mock(return_value=[
        (b'line1\n', b'\n'),
        (b'line2\n', b'\n')
    ])
    stream = EncodedStream(env=env, msg=msg)
    
    body = list(stream.iter_body())
    assert body == [b'line1\n\n', b'line2\n\n']

def test_iter_body_binary_suppressed_error(monkeypatch):
    env = Environment()
    monkeypatch.setattr(env, 'stdout_isatty', False)
    msg = MockMessage()
    msg.iter_lines = Mock(return_value=[
        (b'line1\n', b'\n'),
        (b'line2\0\n', b'\n')  # This line contains a null byte
    ])
    stream = EncodedStream(env=env, msg=msg)
    
    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())
