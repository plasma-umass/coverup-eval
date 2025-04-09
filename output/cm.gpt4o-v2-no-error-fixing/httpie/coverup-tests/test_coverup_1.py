# file: httpie/uploads.py:23-34
# asked: {"lines": [23, 24, 26, 27, 29, 30, 31, 32, 33, 34], "branches": [[30, 31], [32, 33], [32, 34]]}
# gained: {"lines": [23, 24, 26, 27, 29, 30, 31, 32, 33, 34], "branches": [[30, 31], [32, 33], [32, 34]]}

import pytest
from requests_toolbelt import MultipartEncoder
from io import BytesIO
from httpie.uploads import ChunkedMultipartUploadStream

@pytest.fixture
def encoder():
    fields = {
        'field': 'value'
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
