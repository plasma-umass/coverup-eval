# file: httpie/uploads.py:37-98
# asked: {"lines": [], "branches": [[56, 98], [67, 87]]}
# gained: {"lines": [], "branches": [[56, 98]]}

import pytest
from io import BytesIO
from requests_toolbelt import MultipartEncoder
from httpie.cli.dicts import RequestDataDict
from httpie.uploads import prepare_request_body, ChunkedUploadStream, ChunkedMultipartUploadStream

def test_prepare_request_body_with_request_data_dict():
    body = RequestDataDict([('key', 'value')])
    body_read_callback = lambda x: x
    result = prepare_request_body(body, body_read_callback)
    assert result == 'key=value'

def test_prepare_request_body_with_offline_file_like():
    body = BytesIO(b'test data')
    body_read_callback = lambda x: x
    result = prepare_request_body(body, body_read_callback, offline=True)
    assert result == b'test data'

def test_prepare_request_body_with_offline_non_file_like():
    body = 'test data'
    body_read_callback = lambda x: x
    result = prepare_request_body(body, body_read_callback, offline=True)
    assert result == 'test data'

def test_prepare_request_body_with_chunked_non_file_like():
    body = 'test data'
    body_read_callback = lambda x: x
    result = prepare_request_body(body, body_read_callback, chunked=True)
    assert isinstance(result, ChunkedUploadStream)
    assert list(result.stream) == [b'test data']

def test_prepare_request_body_with_zero_length_file_like(monkeypatch):
    body = BytesIO(b'')
    body_read_callback = lambda x: x
    monkeypatch.setattr(body, 'read', lambda: b'')
    result = prepare_request_body(body, body_read_callback)
    assert result == b''

def test_prepare_request_body_with_non_zero_length_file_like(monkeypatch):
    body = BytesIO(b'test data')
    body_read_callback = lambda x: x
    def mock_read(*args):
        return BytesIO(b'test data').read(*args)
    monkeypatch.setattr(body, 'read', mock_read)
    result = prepare_request_body(body, body_read_callback)
    assert result.read() == b'test data'

def test_prepare_request_body_with_chunked_multipart_encoder():
    body = MultipartEncoder(fields={'field': 'value'})
    body_read_callback = lambda x: x
    result = prepare_request_body(body, body_read_callback, chunked=True)
    assert isinstance(result, ChunkedMultipartUploadStream)
    assert result.encoder == body
