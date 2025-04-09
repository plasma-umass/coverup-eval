# file httpie/uploads.py:121-138
# lines [125, 126, 127, 128, 129, 131, 132, 133, 134, 135, 136, 137, 138]
# branches ['126->127', '126->128', '128->129', '128->131', '135->exit', '135->136']

import pytest
import requests
import zlib
from httpie.uploads import compress_request

class MockStream:
    def read(self):
        return b'streamed data'

@pytest.fixture
def prepared_request():
    req = requests.Request(method='POST', url='http://example.com')
    return req.prepare()

def test_compress_request_with_stream(prepared_request):
    # Mock a stream-like object
    mock_stream = MockStream()
    prepared_request.body = mock_stream

    # Call the function to test
    compress_request(prepared_request, always=True)

    # Assertions to verify postconditions
    assert 'Content-Encoding' in prepared_request.headers
    assert prepared_request.headers['Content-Encoding'] == 'deflate'
    assert 'Content-Length' in prepared_request.headers
    assert prepared_request.headers['Content-Length'] == str(len(prepared_request.body))
    assert isinstance(prepared_request.body, bytes)

    # Check if the data was actually compressed
    decompressor = zlib.decompressobj()
    decompressed_data = decompressor.decompress(prepared_request.body)
    decompressed_data += decompressor.flush()
    assert decompressed_data == mock_stream.read()

def test_compress_request_with_stream_not_economical(prepared_request):
    # Mock a stream-like object with data that does not compress well
    mock_stream = MockStream()
    prepared_request.body = mock_stream.read()  # Read the data from the stream

    # Call the function to test
    compress_request(prepared_request, always=False)

    # Assertions to verify postconditions
    # Since the data does not compress well, the original body should be kept
    assert 'Content-Encoding' not in prepared_request.headers or prepared_request.headers['Content-Encoding'] != 'deflate'
    assert prepared_request.body == mock_stream.read()  # This should be the raw data read from the stream
