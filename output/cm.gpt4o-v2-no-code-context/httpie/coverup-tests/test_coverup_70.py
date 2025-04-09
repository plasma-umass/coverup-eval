# file: httpie/uploads.py:23-34
# asked: {"lines": [27, 30, 31, 32, 33, 34], "branches": [[30, 31], [32, 33], [32, 34]]}
# gained: {"lines": [27, 30, 31, 32, 33, 34], "branches": [[30, 31], [32, 33], [32, 34]]}

import pytest
from httpie.uploads import ChunkedMultipartUploadStream
from requests_toolbelt.multipart.encoder import MultipartEncoder
import io

@pytest.fixture
def encoder():
    fields = {
        'field1': 'value1',
        'field2': 'value2',
    }
    return MultipartEncoder(fields=fields)

def test_chunked_multipart_upload_stream_init(encoder):
    stream = ChunkedMultipartUploadStream(encoder)
    assert stream.encoder == encoder

def test_chunked_multipart_upload_stream_iter(encoder):
    stream = ChunkedMultipartUploadStream(encoder)
    chunks = list(stream)
    assert len(chunks) > 0
    assert all(isinstance(chunk, bytes) for chunk in chunks)

def test_chunked_multipart_upload_stream_empty(monkeypatch):
    class MockEncoder:
        def read(self, chunk_size):
            return b''

    mock_encoder = MockEncoder()
    stream = ChunkedMultipartUploadStream(mock_encoder)
    chunks = list(stream)
    assert chunks == []
