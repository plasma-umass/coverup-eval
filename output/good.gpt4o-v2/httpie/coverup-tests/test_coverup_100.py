# file: httpie/output/streams.py:89-115
# asked: {"lines": [111, 112, 113, 114, 115], "branches": [[111, 0], [111, 112], [112, 113], [112, 114]]}
# gained: {"lines": [111, 112, 113, 114, 115], "branches": [[111, 0], [111, 112], [112, 113], [112, 114]]}

import pytest
from httpie.output.streams import EncodedStream, BinarySuppressedError
from httpie.context import Environment
from httpie.models import HTTPMessage

class MockMessage:
    def __init__(self, lines, encoding='utf8'):
        self.lines = lines
        self.encoding = encoding

    def iter_lines(self, chunk_size):
        for line in self.lines:
            yield line, b'\n'

def test_iter_body_with_binary_data():
    msg = MockMessage([b'line1', b'line2\0binary'])
    stream = EncodedStream(msg=msg, env=Environment(stdout_isatty=False))
    
    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())

def test_iter_body_with_text_data():
    msg = MockMessage([b'line1', b'line2'], encoding='utf8')
    stream = EncodedStream(msg=msg, env=Environment(stdout_isatty=False))
    
    result = list(stream.iter_body())
    
    assert result == [b'line1\n', b'line2\n']

def test_iter_body_with_different_encoding():
    msg = MockMessage([b'caf\xc3\xa9', b'na\xc3\xafve'], encoding='latin1')
    stream = EncodedStream(msg=msg, env=Environment(stdout_isatty=False))
    
    result = list(stream.iter_body())
    
    assert result == [b'caf\xc3\xa9\n', b'na\xc3\xafve\n']

def test_iter_body_with_stdout_isatty(monkeypatch):
    msg = MockMessage([b'line1', b'line2'], encoding='utf8')
    env = Environment(stdout_isatty=True, stdout_encoding='utf8')
    stream = EncodedStream(msg=msg, env=env)
    
    result = list(stream.iter_body())
    
    assert result == [b'line1\n', b'line2\n']
