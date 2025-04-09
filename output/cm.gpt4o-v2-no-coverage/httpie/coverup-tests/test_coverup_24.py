# file: httpie/uploads.py:12-20
# asked: {"lines": [12, 13, 14, 15, 17, 18, 19, 20], "branches": [[18, 0], [18, 19]]}
# gained: {"lines": [12, 13, 14, 15, 17, 18, 19, 20], "branches": [[18, 0], [18, 19]]}

import pytest
from httpie.uploads import ChunkedUploadStream

class TestChunkedUploadStream:
    def test_init(self):
        stream = iter([b"chunk1", b"chunk2"])
        callback = lambda x: x
        chunked_stream = ChunkedUploadStream(stream, callback)
        
        assert chunked_stream.stream == stream
        assert chunked_stream.callback == callback

    def test_iter(self):
        chunks = [b"chunk1", b"chunk2"]
        stream = iter(chunks)
        called_chunks = []

        def callback(chunk):
            called_chunks.append(chunk)

        chunked_stream = ChunkedUploadStream(stream, callback)
        result_chunks = list(chunked_stream)

        assert result_chunks == chunks
        assert called_chunks == chunks
