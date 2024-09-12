# file: httpie/uploads.py:37-98
# asked: {"lines": [], "branches": [[67, 87]]}
# gained: {"lines": [], "branches": [[67, 87]]}

import io
import pytest
from httpie.uploads import prepare_request_body, ChunkedUploadStream, ChunkedMultipartUploadStream
from requests_toolbelt import MultipartEncoder
from httpie.cli.dicts import RequestDataDict

def test_prepare_request_body_with_chunked_and_multipartencoder():
    body = MultipartEncoder(fields={'field': 'value'})
    body_read_callback = lambda x: x
    chunked = True
    offline = False

    result = prepare_request_body(body, body_read_callback, chunked=chunked, offline=offline)

    assert isinstance(result, ChunkedMultipartUploadStream)

def test_prepare_request_body_with_chunked_and_file_like():
    body = io.BytesIO(b"test data")
    body_read_callback = lambda x: x
    chunked = True
    offline = False

    result = prepare_request_body(body, body_read_callback, chunked=chunked, offline=offline)

    assert isinstance(result, ChunkedUploadStream)

def test_prepare_request_body_with_file_like_and_no_content_length():
    body = io.BytesIO(b"")
    body_read_callback = lambda x: x
    chunked = False
    offline = False

    result = prepare_request_body(body, body_read_callback, chunked=chunked, offline=offline)

    assert isinstance(result, bytes)
    assert result == b""

def test_prepare_request_body_with_requestdatadict():
    body = RequestDataDict([('key', 'value')])
    body_read_callback = lambda x: x
    chunked = False
    offline = False

    result = prepare_request_body(body, body_read_callback, chunked=chunked, offline=offline)

    assert isinstance(result, str)
    assert result == "key=value"

def test_prepare_request_body_with_file_like_and_chunked():
    body = io.BytesIO(b"")
    body_read_callback = lambda x: x
    chunked = True
    offline = False

    result = prepare_request_body(body, body_read_callback, chunked=chunked, offline=offline)

    assert isinstance(result, ChunkedUploadStream)
