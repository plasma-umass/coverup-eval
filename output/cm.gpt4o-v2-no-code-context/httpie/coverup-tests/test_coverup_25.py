# file: httpie/uploads.py:121-138
# asked: {"lines": [121, 125, 126, 127, 128, 129, 131, 132, 133, 134, 135, 136, 137, 138], "branches": [[126, 127], [126, 128], [128, 129], [128, 131], [135, 0], [135, 136]]}
# gained: {"lines": [121, 125, 126, 127, 128, 129, 131, 132, 133, 134, 135, 136, 137, 138], "branches": [[126, 127], [126, 128], [128, 129], [128, 131], [135, 0], [135, 136]]}

import pytest
import requests
import zlib
from io import BytesIO
from httpie.uploads import compress_request

@pytest.fixture
def prepared_request():
    return requests.Request('POST', 'http://example.com').prepare()

def test_compress_request_with_string_body(prepared_request):
    prepared_request.body = "test string body"
    compress_request(prepared_request, always=False)
    deflater = zlib.compressobj()
    body_bytes = "test string body".encode()
    deflated_data = deflater.compress(body_bytes) + deflater.flush()
    is_economical = len(deflated_data) < len(body_bytes)
    if is_economical:
        assert prepared_request.headers['Content-Encoding'] == 'deflate'
        assert prepared_request.headers['Content-Length'] == str(len(deflated_data))
    else:
        assert 'Content-Encoding' not in prepared_request.headers

def test_compress_request_with_file_body(prepared_request):
    prepared_request.body = BytesIO(b"test file body")
    compress_request(prepared_request, always=False)
    deflater = zlib.compressobj()
    body_bytes = b"test file body"
    deflated_data = deflater.compress(body_bytes) + deflater.flush()
    is_economical = len(deflated_data) < len(body_bytes)
    if is_economical:
        assert prepared_request.headers['Content-Encoding'] == 'deflate'
        assert prepared_request.headers['Content-Length'] == str(len(deflated_data))
    else:
        assert 'Content-Encoding' not in prepared_request.headers

def test_compress_request_with_bytes_body(prepared_request):
    prepared_request.body = b"test bytes body"
    compress_request(prepared_request, always=False)
    deflater = zlib.compressobj()
    body_bytes = b"test bytes body"
    deflated_data = deflater.compress(body_bytes) + deflater.flush()
    is_economical = len(deflated_data) < len(body_bytes)
    if is_economical:
        assert prepared_request.headers['Content-Encoding'] == 'deflate'
        assert prepared_request.headers['Content-Length'] == str(len(deflated_data))
    else:
        assert 'Content-Encoding' not in prepared_request.headers

def test_compress_request_always_true(prepared_request):
    prepared_request.body = "test string body"
    compress_request(prepared_request, always=True)
    deflater = zlib.compressobj()
    body_bytes = "test string body".encode()
    deflated_data = deflater.compress(body_bytes) + deflater.flush()
    assert prepared_request.headers['Content-Encoding'] == 'deflate'
    assert prepared_request.headers['Content-Length'] == str(len(deflated_data))
