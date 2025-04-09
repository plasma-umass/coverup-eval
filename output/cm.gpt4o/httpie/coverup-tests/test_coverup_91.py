# file httpie/uploads.py:37-98
# lines [45, 47, 48, 50, 51, 52, 53, 55, 56, 57, 59, 60, 65, 67, 76, 78, 80, 81, 82, 83, 85, 87, 88, 89, 90, 93, 94, 95, 98]
# branches ['47->48', '47->50', '50->51', '50->55', '51->52', '51->53', '55->56', '55->65', '56->57', '56->98', '65->67', '65->78', '67->76', '67->87', '87->88', '87->98', '88->89', '88->93']

import pytest
from httpie.uploads import prepare_request_body, ChunkedUploadStream, ChunkedMultipartUploadStream, MultipartEncoder, RequestDataDict
from io import BytesIO

def test_prepare_request_body():
    def dummy_callback(data):
        return data

    # Test case for body as RequestDataDict
    body = RequestDataDict([('key', 'value')])
    result = prepare_request_body(body, dummy_callback, offline=True)
    assert result == 'key=value'

    # Test case for body as file-like object and offline
    body = BytesIO(b'test data')
    result = prepare_request_body(body, dummy_callback, offline=True)
    assert result == b'test data'

    # Test case for body as file-like object and chunked
    body = BytesIO(b'test data')
    result = prepare_request_body(body, dummy_callback, chunked=True)
    assert isinstance(result, ChunkedUploadStream)

    # Test case for body as file-like object with content length
    body = BytesIO(b'test data')
    result = prepare_request_body(body, dummy_callback, content_length_header_value=9)
    assert result.read() == b'test data'

    # Test case for body as MultipartEncoder and chunked
    body = MultipartEncoder(fields={'field': 'value'})
    result = prepare_request_body(body, dummy_callback, chunked=True)
    assert isinstance(result, ChunkedMultipartUploadStream)

    # Test case for body as string and chunked
    body = 'test data'
    result = prepare_request_body(body, dummy_callback, chunked=True)
    assert isinstance(result, ChunkedUploadStream)

    # Test case for body as string and not chunked
    body = 'test data'
    result = prepare_request_body(body, dummy_callback)
    assert result == 'test data'

    # Test case for body as file-like object with zero length and no content length
    body = BytesIO(b'')
    result = prepare_request_body(body, dummy_callback)
    assert result == b''

    # Test case for body as file-like object with zero length and chunked
    body = BytesIO(b'')
    result = prepare_request_body(body, dummy_callback, chunked=True)
    assert isinstance(result, ChunkedUploadStream)

    # Test case for body as file-like object with read callback
    body = BytesIO(b'test data')
    def callback(data):
        return data.upper()
    result = prepare_request_body(body, callback)
    assert result.read() == b'test data'

    # Test case for body as file-like object with read callback and chunked
    body = BytesIO(b'test data')
    result = prepare_request_body(body, callback, chunked=True)
    assert isinstance(result, ChunkedUploadStream)

    # Test case for body as file-like object with read callback and MultipartEncoder
    body = MultipartEncoder(fields={'field': 'value'})
    result = prepare_request_body(body, callback, chunked=True)
    assert isinstance(result, ChunkedMultipartUploadStream)
