# file: httpie/uploads.py:23-34
# asked: {"lines": [23, 24, 26, 27, 29, 30, 31, 32, 33, 34], "branches": [[30, 31], [32, 33], [32, 34]]}
# gained: {"lines": [23, 24, 26, 27, 29, 30, 31, 32, 33, 34], "branches": [[30, 31], [32, 33], [32, 34]]}

import pytest
from requests_toolbelt import MultipartEncoder
from io import BytesIO
from httpie.uploads import ChunkedMultipartUploadStream

class MockMultipartEncoder:
    def __init__(self, content: bytes):
        self.stream = BytesIO(content)
        self.len = len(content)

    def read(self, size: int):
        return self.stream.read(size)

def test_chunked_multipart_upload_stream():
    content = b'a' * 250 * 1024  # 250 KB of data
    encoder = MockMultipartEncoder(content)
    upload_stream = ChunkedMultipartUploadStream(encoder)

    chunks = list(upload_stream)
    assert len(chunks) == 3  # 3 chunks of 100 KB, 100 KB, and 50 KB
    assert chunks[0] == b'a' * 100 * 1024
    assert chunks[1] == b'a' * 100 * 1024
    assert chunks[2] == b'a' * 50 * 1024

