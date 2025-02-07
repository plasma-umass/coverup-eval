# file: httpie/uploads.py:37-98
# asked: {"lines": [37, 40, 41, 42, 45, 47, 48, 50, 51, 52, 53, 55, 56, 57, 59, 60, 65, 67, 76, 78, 80, 81, 82, 83, 85, 87, 88, 89, 90, 93, 94, 95, 98], "branches": [[47, 48], [47, 50], [50, 51], [50, 55], [51, 52], [51, 53], [55, 56], [55, 65], [56, 57], [56, 98], [65, 67], [65, 78], [67, 76], [67, 87], [87, 88], [87, 98], [88, 89], [88, 93]]}
# gained: {"lines": [37, 40, 41, 42, 45, 47, 48, 50, 51, 52, 53, 55, 56, 57, 59, 60, 65, 67, 76, 78, 80, 81, 82, 83, 85, 87, 88, 89, 90, 93, 94, 95, 98], "branches": [[47, 48], [47, 50], [50, 51], [50, 55], [51, 52], [51, 53], [55, 56], [55, 65], [56, 57], [56, 98], [65, 67], [65, 78], [67, 76], [87, 88], [87, 98], [88, 89], [88, 93]]}

import pytest
from io import BytesIO
from requests_toolbelt import MultipartEncoder
from httpie.cli.dicts import RequestDataDict
from httpie.uploads import prepare_request_body, ChunkedUploadStream, ChunkedMultipartUploadStream

def test_prepare_request_body_with_request_data_dict():
    body = RequestDataDict([('key', 'value')])
    result = prepare_request_body(body, lambda x: x)
    assert result == 'key=value'

def test_prepare_request_body_offline_with_file_like():
    body = BytesIO(b'test data')
    result = prepare_request_body(body, lambda x: x, offline=True)
    assert result == b'test data'

def test_prepare_request_body_offline_with_non_file_like():
    body = 'test data'
    result = prepare_request_body(body, lambda x: x, offline=True)
    assert result == 'test data'

def test_prepare_request_body_chunked_with_non_file_like():
    body = 'test data'
    result = prepare_request_body(body, lambda x: x, chunked=True)
    assert isinstance(result, ChunkedUploadStream)

def test_prepare_request_body_with_empty_file_like_and_no_content_length():
    body = BytesIO(b'')
    result = prepare_request_body(body, lambda x: x)
    assert result == b''

def test_prepare_request_body_with_non_empty_file_like():
    body = BytesIO(b'test data')
    callback_called = False
    def callback(chunk):
        nonlocal callback_called
        callback_called = True
        return chunk
    result = prepare_request_body(body, callback)
    assert result.read() == b'test data'
    assert callback_called

def test_prepare_request_body_chunked_with_multipart_encoder():
    body = MultipartEncoder(fields={'field': 'value'})
    result = prepare_request_body(body, lambda x: x, chunked=True)
    assert isinstance(result, ChunkedMultipartUploadStream)

def test_prepare_request_body_chunked_with_file_like():
    body = BytesIO(b'test data')
    result = prepare_request_body(body, lambda x: x, chunked=True)
    assert isinstance(result, ChunkedUploadStream)
