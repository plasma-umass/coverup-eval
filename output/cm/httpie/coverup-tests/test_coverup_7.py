# file httpie/uploads.py:37-98
# lines [37, 40, 41, 42, 45, 47, 48, 50, 51, 52, 53, 55, 56, 57, 59, 60, 65, 67, 76, 78, 80, 81, 82, 83, 85, 87, 88, 89, 90, 93, 94, 95, 98]
# branches ['47->48', '47->50', '50->51', '50->55', '51->52', '51->53', '55->56', '55->65', '56->57', '56->98', '65->67', '65->78', '67->76', '67->87', '87->88', '87->98', '88->89', '88->93']

import io
import pytest
from httpie.uploads import prepare_request_body, ChunkedUploadStream

class DummyStream(io.BytesIO):
    def __len__(self):
        return 0

@pytest.fixture
def cleanup():
    # Fixture to perform cleanup after tests
    yield
    # No cleanup actions needed for this test case

def test_prepare_request_body_with_zero_length_file_like_object(cleanup, mocker):
    # Mock the super_len function to return 0
    mocker.patch('httpie.uploads.super_len', return_value=0)

    # Create a file-like object with zero length
    file_like_object = DummyStream()

    # Define a dummy callback function
    def dummy_callback(chunk):
        return chunk

    # Call the function with the file-like object
    result = prepare_request_body(
        body=file_like_object,
        body_read_callback=dummy_callback,
        content_length_header_value=None,
        chunked=False,
        offline=False
    )

    # Assert that the result is the content of the file-like object
    assert result == b''

    # Now test with chunked=True
    result_chunked = prepare_request_body(
        body=file_like_object,
        body_read_callback=dummy_callback,
        content_length_header_value=None,
        chunked=True,
        offline=False
    )

    # Assert that the result is a ChunkedUploadStream
    assert isinstance(result_chunked, ChunkedUploadStream)

    # Read from the chunked stream to trigger the callback
    assert next(iter(result_chunked.stream), b'') == b''
