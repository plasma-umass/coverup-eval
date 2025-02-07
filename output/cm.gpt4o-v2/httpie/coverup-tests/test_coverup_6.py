# file: httpie/models.py:89-138
# asked: {"lines": [89, 90, 92, 93, 95, 96, 98, 99, 100, 102, 103, 104, 105, 108, 109, 110, 112, 113, 114, 115, 117, 120, 121, 123, 125, 126, 128, 129, 130, 132, 133, 134, 135, 137, 138], "branches": [[109, 110], [109, 112], [123, 125], [123, 126], [135, 137], [135, 138]]}
# gained: {"lines": [89, 90, 92, 93, 95, 96, 98, 99, 100, 102, 103, 104, 105, 108, 109, 110, 112, 113, 114, 115, 117, 120, 121, 123, 126, 128, 129, 130, 132, 133, 134, 135, 137, 138], "branches": [[109, 110], [123, 126], [135, 137]]}

import pytest
from httpie.models import HTTPRequest
from requests.models import Request
from urllib.parse import urlsplit

class MockRequest:
    def __init__(self, method, url, headers=None, body=None):
        self.method = method
        self.url = url
        self.headers = headers or {}
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
    body = list(http_request.iter_body(1024))
    assert body == [b'{"key": "value"}']

def test_iter_lines(http_request):
    lines = list(http_request.iter_lines(1024))
    assert lines == [(b'{"key": "value"}', b'')]

def test_headers(http_request):
    headers = http_request.headers
    assert 'GET /path?query=1 HTTP/1.1' in headers
    assert 'User-Agent: test-agent' in headers
    assert 'Host: example.com' in headers

def test_encoding(http_request):
    assert http_request.encoding == 'utf8'

def test_body(http_request):
    assert http_request.body == b'{"key": "value"}'
