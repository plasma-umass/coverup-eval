# file httpie/models.py:89-138
# lines [89, 90, 92, 93, 95, 96, 98, 99, 100, 102, 103, 104, 105, 108, 109, 110, 112, 113, 114, 115, 117, 120, 121, 123, 125, 126, 128, 129, 130, 132, 133, 134, 135, 137, 138]
# branches ['109->110', '109->112', '123->125', '123->126', '135->137', '135->138']

import pytest
from unittest.mock import Mock
from httpie.models import HTTPRequest
from urllib.parse import urlsplit

class MockRequest:
    def __init__(self, method, url, headers, body):
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

@pytest.fixture
def mock_request():
    return MockRequest(
        method='GET',
        url='http://example.com/path?query=1',
        headers={'User-Agent': 'test-agent'},
        body='{"key": "value"}'
    )

@pytest.fixture
def http_request(mock_request):
    return HTTPRequest(mock_request)

def test_iter_body(http_request):
    body = next(http_request.iter_body(1024))
    assert body == b'{"key": "value"}'

def test_iter_lines(http_request):
    body, empty = next(http_request.iter_lines(1024))
    assert body == b'{"key": "value"}'
    assert empty == b''

def test_headers(http_request):
    headers = http_request.headers
    assert 'GET /path?query=1 HTTP/1.1' in headers
    assert 'User-Agent: test-agent' in headers
    assert 'Host: example.com' in headers

def test_encoding(http_request):
    assert http_request.encoding == 'utf8'

def test_body(http_request):
    body = http_request.body
    assert body == b'{"key": "value"}'

@pytest.fixture
def mock_request_no_host():
    return MockRequest(
        method='POST',
        url='http://example.com/path',
        headers={},
        body='{"key": "value"}'
    )

@pytest.fixture
def http_request_no_host(mock_request_no_host):
    return HTTPRequest(mock_request_no_host)

def test_headers_no_host(http_request_no_host):
    headers = http_request_no_host.headers
    assert 'POST /path HTTP/1.1' in headers
    assert 'Host: example.com' in headers
