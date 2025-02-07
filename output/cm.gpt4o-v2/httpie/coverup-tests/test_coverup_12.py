# file: httpie/uploads.py:121-138
# asked: {"lines": [121, 125, 126, 127, 128, 129, 131, 132, 133, 134, 135, 136, 137, 138], "branches": [[126, 127], [126, 128], [128, 129], [128, 131], [135, 0], [135, 136]]}
# gained: {"lines": [121, 125, 126, 127, 128, 129, 131, 132, 133, 134, 135, 136, 137, 138], "branches": [[126, 127], [126, 128], [128, 129], [128, 131], [135, 0], [135, 136]]}

import pytest
import requests
from httpie.uploads import compress_request

def test_compress_request_with_string_body():
    request = requests.Request('POST', 'http://example.com', data='test body').prepare()
    compress_request(request, always=True)
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.headers['Content-Length'] == str(len(request.body))

def test_compress_request_with_file_body(tmp_path):
    file_path = tmp_path / "testfile.txt"
    file_path.write_text("test file content")
    with file_path.open('rb') as f:
        request = requests.Request('POST', 'http://example.com', data=f).prepare()
        compress_request(request, always=True)
        assert request.headers['Content-Encoding'] == 'deflate'
        assert request.headers['Content-Length'] == str(len(request.body))

def test_compress_request_with_bytes_body():
    request = requests.Request('POST', 'http://example.com', data=b'test bytes').prepare()
    compress_request(request, always=True)
    assert request.headers['Content-Encoding'] == 'deflate'
    assert request.headers['Content-Length'] == str(len(request.body))

def test_compress_request_not_economical():
    request = requests.Request('POST', 'http://example.com', data='short').prepare()
    original_length = len(request.body)
    compress_request(request, always=False)
    assert 'Content-Encoding' not in request.headers
    assert request.headers['Content-Length'] == str(original_length)
