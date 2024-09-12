# file: httpie/output/streams.py:75-86
# asked: {"lines": [75, 76, 78, 79, 81, 82, 83, 85, 86], "branches": []}
# gained: {"lines": [75, 76, 78, 79, 81, 82, 83, 85, 86], "branches": []}

import pytest
from unittest.mock import Mock
from httpie.output.streams import RawStream
from httpie.models import HTTPMessage

class MockHTTPMessage(HTTPMessage):
    def __init__(self):
        super().__init__(orig=None)
    
    def iter_body(self, chunk_size):
        yield b'test_chunk'

@pytest.fixture
def mock_http_message():
    return MockHTTPMessage()

def test_raw_stream_init(mock_http_message):
    stream = RawStream(msg=mock_http_message)
    assert stream.chunk_size == RawStream.CHUNK_SIZE

def test_raw_stream_iter_body(mock_http_message):
    stream = RawStream(msg=mock_http_message)
    body_chunks = list(stream.iter_body())
    assert body_chunks == [b'test_chunk']
