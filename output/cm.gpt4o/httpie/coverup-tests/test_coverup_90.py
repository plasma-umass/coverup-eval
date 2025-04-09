# file httpie/uploads.py:121-138
# lines [125, 126, 127, 128, 129, 131, 132, 133, 134, 135, 136, 137, 138]
# branches ['126->127', '126->128', '128->129', '128->131', '135->exit', '135->136']

import pytest
import requests
import zlib
from unittest.mock import MagicMock

# Assuming the compress_request function is imported from httpie.uploads
from httpie.uploads import compress_request

def test_compress_request_with_string_body():
    request = requests.PreparedRequest()
    request.body = "test string body"
    request.headers = {}

    compress_request(request, always=True)

    assert request.headers['Content-Encoding'] == 'deflate'
    assert 'Content-Length' in request.headers
    assert request.body != "test string body"

def test_compress_request_with_file_body(mocker):
    request = requests.PreparedRequest()
    mock_file = mocker.mock_open(read_data=b"test file body")
    request.body = mock_file()
    request.headers = {}

    compress_request(request, always=True)

    assert request.headers['Content-Encoding'] == 'deflate'
    assert 'Content-Length' in request.headers
    assert request.body != b"test file body"

def test_compress_request_with_bytes_body():
    request = requests.PreparedRequest()
    request.body = b"test bytes body"
    request.headers = {}

    compress_request(request, always=True)

    assert request.headers['Content-Encoding'] == 'deflate'
    assert 'Content-Length' in request.headers
    assert request.body != b"test bytes body"

def test_compress_request_not_economical():
    request = requests.PreparedRequest()
    request.body = b"short"
    request.headers = {}

    compress_request(request, always=False)

    assert 'Content-Encoding' not in request.headers
    assert 'Content-Length' not in request.headers
    assert request.body == b"short"
