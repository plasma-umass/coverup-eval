# file: httpie/output/streams.py:75-86
# asked: {"lines": [75, 76, 78, 79, 81, 82, 83, 85, 86], "branches": []}
# gained: {"lines": [75, 76, 78, 79, 81, 82, 83, 85, 86], "branches": []}

import pytest
from httpie.output.streams import RawStream
from httpie.models import HTTPMessage

class MockHTTPMessage(HTTPMessage):
    def __init__(self, orig):
        super().__init__(orig)
        self.body_content = b"test body content"

    def iter_body(self, chunk_size: int):
        for i in range(0, len(self.body_content), chunk_size):
            yield self.body_content[i:i + chunk_size]

@pytest.fixture
def mock_http_message():
    return MockHTTPMessage(orig=None)

def test_raw_stream_init(mock_http_message):
    stream = RawStream(msg=mock_http_message, chunk_size=2048)
    assert stream.chunk_size == 2048
    assert stream.msg == mock_http_message

def test_raw_stream_iter_body(mock_http_message):
    stream = RawStream(msg=mock_http_message, chunk_size=5)
    body_chunks = list(stream.iter_body())
    assert body_chunks == [b"test ", b"body ", b"conte", b"nt"]
