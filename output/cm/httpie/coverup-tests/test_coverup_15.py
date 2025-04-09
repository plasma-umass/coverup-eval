# file httpie/uploads.py:12-20
# lines [12, 13, 14, 15, 17, 18, 19, 20]
# branches ['18->exit', '18->19']

import pytest
from httpie.uploads import ChunkedUploadStream
from unittest.mock import Mock

def test_chunked_upload_stream():
    # Setup a mock callback
    mock_callback = Mock()

    # Define a sample iterable stream
    sample_stream = [b'chunk1', b'chunk2', b'chunk3']

    # Create a ChunkedUploadStream instance with the mock callback
    chunked_stream = ChunkedUploadStream(sample_stream, mock_callback)

    # Iterate over the chunked_stream to trigger the callback
    for i, chunk in enumerate(chunked_stream):
        # Assert that the callback is called with the correct chunk
        mock_callback.assert_called_with(chunk)
        # Assert that the chunk is what we expect
        assert chunk == sample_stream[i]

    # Assert that the callback was called the correct number of times
    assert mock_callback.call_count == len(sample_stream)
