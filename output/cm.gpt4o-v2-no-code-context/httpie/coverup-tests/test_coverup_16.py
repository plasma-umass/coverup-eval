# file: httpie/models.py:89-138
# asked: {"lines": [89, 90, 92, 93, 95, 96, 98, 99, 100, 102, 103, 104, 105, 108, 109, 110, 112, 113, 114, 115, 117, 120, 121, 123, 125, 126, 128, 129, 130, 132, 133, 134, 135, 137, 138], "branches": [[109, 110], [109, 112], [123, 125], [123, 126], [135, 137], [135, 138]]}
# gained: {"lines": [89, 90, 92, 93, 95, 96, 98, 99, 100, 102, 103, 104, 105, 108, 109, 110, 112, 113, 114, 115, 117, 120, 121, 123, 126, 128, 129, 130, 132, 133, 134, 135, 137, 138], "branches": [[109, 110], [123, 126], [135, 137], [135, 138]]}

import pytest
from httpie.models import HTTPRequest
from requests.models import Request, PreparedRequest

@pytest.fixture
def mock_request():
    req = Request(
        method='GET',
        url='http://example.com/path?query=1',
        headers={'User-Agent': 'test-agent'},
        data='test body'
    )
    prepared_req = req.prepare()
    return prepared_req

def test_iter_body(mock_request):
    http_request = HTTPRequest(mock_request)
    body = next(http_request.iter_body(1024))
    assert body == b'test body'

def test_iter_lines(mock_request):
    http_request = HTTPRequest(mock_request)
    lines = next(http_request.iter_lines(1024))
    assert lines == (b'test body', b'')

def test_headers_with_host(mock_request):
    http_request = HTTPRequest(mock_request)
    headers = http_request.headers
    assert 'GET /path?query=1 HTTP/1.1' in headers
    assert 'User-Agent: test-agent' in headers
    assert 'Host: example.com' in headers

def test_headers_without_host(monkeypatch, mock_request):
    monkeypatch.delitem(mock_request.headers, 'User-Agent')
    http_request = HTTPRequest(mock_request)
    headers = http_request.headers
    assert 'GET /path?query=1 HTTP/1.1' in headers
    assert 'Host: example.com' in headers

def test_encoding(mock_request):
    http_request = HTTPRequest(mock_request)
    assert http_request.encoding == 'utf8'

def test_body(mock_request):
    http_request = HTTPRequest(mock_request)
    body = http_request.body
    assert body == b'test body'

def test_body_empty(mock_request):
    mock_request.body = None
    http_request = HTTPRequest(mock_request)
    body = http_request.body
    assert body == b''
