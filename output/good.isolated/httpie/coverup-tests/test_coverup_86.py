# file httpie/uploads.py:37-98
# lines [48, 51, 52, 53, 56, 57, 59, 60, 78, 80, 81, 82, 83, 85, 89, 90]
# branches ['47->48', '50->51', '51->52', '51->53', '55->56', '56->57', '56->98', '65->78', '88->89']

import io
import pytest
from httpie.uploads import prepare_request_body, RequestDataDict, MultipartEncoder, ChunkedUploadStream, ChunkedMultipartUploadStream
from urllib.parse import urlencode

class TestPrepareRequestBody:

    def test_prepare_request_body_coverage(self, mocker):
        # Mock the callback to simply return the chunk
        body_read_callback = mocker.Mock(return_value=lambda chunk: chunk)

        # Test RequestDataDict branch
        body_dict = RequestDataDict({'key': 'value'})
        result = prepare_request_body(body_dict, body_read_callback)
        assert result == urlencode(body_dict, doseq=True)

        # Test offline with file-like object branch
        file_like_body = io.StringIO('file-like content')
        result = prepare_request_body(file_like_body, body_read_callback, offline=True)
        assert result == 'file-like content'

        # Test offline with non-file-like object branch
        non_file_like_body = 'non-file-like content'
        result = prepare_request_body(non_file_like_body, body_read_callback, offline=True)
        assert result == 'non-file-like content'

        # Test chunked with non-file-like object branch
        result = prepare_request_body(non_file_like_body, body_read_callback, chunked=True)
        assert isinstance(result, ChunkedUploadStream)

        # Test zero-length file-like object with content_length_header_value is None and not chunked
        empty_file_like_body = io.StringIO('')
        result = prepare_request_body(empty_file_like_body, body_read_callback)
        assert result == ''

        # Test file-like object with chunked transfer
        file_like_body = io.StringIO('file-like content')
        result = prepare_request_body(file_like_body, body_read_callback, chunked=True)
        assert isinstance(result, ChunkedUploadStream)

        # Test MultipartEncoder with chunked transfer
        multipart_encoder = MultipartEncoder(fields={'key': 'value'})
        result = prepare_request_body(multipart_encoder, body_read_callback, chunked=True)
        assert isinstance(result, ChunkedMultipartUploadStream)

        # Cleanup
        mocker.stopall()
