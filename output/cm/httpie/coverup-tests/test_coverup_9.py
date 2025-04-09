# file httpie/models.py:89-138
# lines [89, 90, 92, 93, 95, 96, 98, 99, 100, 102, 103, 104, 105, 108, 109, 110, 112, 113, 114, 115, 117, 120, 121, 123, 125, 126, 128, 129, 130, 132, 133, 134, 135, 137, 138]
# branches ['109->110', '109->112', '123->125', '123->126', '135->137', '135->138']

import pytest
from httpie.models import HTTPRequest
from requests.models import Request
from urllib.parse import urlsplit

@pytest.fixture
def mock_request():
    request = Request()
    request.method = 'GET'
    request.url = 'http://example.com/path?query=123'
    request.headers = {'User-Agent': 'test-agent'}
    request.body = 'test-body'
    return request

def test_http_request_headers_without_host(mock_request):
    http_request = HTTPRequest(mock_request)
    headers = http_request.headers
    assert 'Host: example.com' in headers
    assert 'GET /path?query=123 HTTP/1.1' in headers
    assert 'User-Agent: test-agent' in headers

def test_http_request_headers_with_host(mock_request):
    mock_request.headers['Host'] = 'example.com'
    http_request = HTTPRequest(mock_request)
    headers = http_request.headers
    assert 'Host: example.com' in headers
    assert 'GET /path?query=123 HTTP/1.1' in headers
    assert 'User-Agent: test-agent' in headers

def test_http_request_body_str(mock_request):
    mock_request.body = 'test-body'
    http_request = HTTPRequest(mock_request)
    assert http_request.body == b'test-body'

def test_http_request_body_bytes(mock_request):
    mock_request.body = b'test-body'
    http_request = HTTPRequest(mock_request)
    assert http_request.body == b'test-body'

def test_http_request_body_none(mock_request):
    mock_request.body = None
    http_request = HTTPRequest(mock_request)
    assert http_request.body == b''

def test_http_request_iter_body(mock_request):
    http_request = HTTPRequest(mock_request)
    body_chunks = list(http_request.iter_body(chunk_size=1024))
    assert body_chunks == [b'test-body']

def test_http_request_iter_lines(mock_request):
    http_request = HTTPRequest(mock_request)
    lines = list(http_request.iter_lines(chunk_size=1024))
    assert lines == [(b'test-body', b'')]

def test_http_request_encoding(mock_request):
    http_request = HTTPRequest(mock_request)
    assert http_request.encoding == 'utf8'
