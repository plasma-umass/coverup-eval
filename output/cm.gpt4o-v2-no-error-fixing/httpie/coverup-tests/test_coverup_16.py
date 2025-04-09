# file: httpie/uploads.py:12-20
# asked: {"lines": [12, 13, 14, 15, 17, 18, 19, 20], "branches": [[18, 0], [18, 19]]}
# gained: {"lines": [12, 13, 14, 15, 17, 18, 19, 20], "branches": [[18, 0], [18, 19]]}

import pytest

from httpie.uploads import ChunkedUploadStream

def test_chunked_upload_stream():
    def mock_callback(chunk):
        assert chunk in [b'chunk1', b'chunk2', b'chunk3']
    
    stream = [b'chunk1', b'chunk2', b'chunk3']
    chunked_stream = ChunkedUploadStream(stream, mock_callback)
    
    result = list(chunked_stream)
    assert result == stream
