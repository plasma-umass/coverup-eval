# file: httpie/models.py:89-138
# asked: {"lines": [125], "branches": [[109, 112], [123, 125]]}
# gained: {"lines": [], "branches": [[109, 112]]}

import pytest
from httpie.models import HTTPRequest
from requests.models import Request

@pytest.fixture
def mock_request():
    req = Request(
        method='GET',
        url='http://example.com/path?query=1',
        headers={'User-Agent': 'test-agent'}
    )
    req.body = 'test body'
    return req

def test_headers_with_host(mock_request):
    http_request = HTTPRequest(mock_request)
    headers = http_request.headers
    assert 'Host: example.com' in headers
    assert 'User-Agent: test-agent' in headers

def test_headers_without_host(mock_request):
    mock_request.headers['Host'] = 'example.com'
    http_request = HTTPRequest(mock_request)
    headers = http_request.headers
    assert 'Host: example.com' in headers
    assert 'User-Agent: test-agent' in headers

def test_headers_bytes_decoding(mock_request, monkeypatch):
    class MockHTTPRequest(HTTPRequest):
        @property
        def headers(self):
            headers = super().headers
            if isinstance(headers, str):
                headers = headers.encode('utf8')
            return headers

    http_request = MockHTTPRequest(mock_request)
    headers = http_request.headers
    assert isinstance(headers, bytes)
    headers = headers.decode('utf8')
    assert 'Host: example.com' in headers
    assert 'User-Agent: test-agent' in headers
