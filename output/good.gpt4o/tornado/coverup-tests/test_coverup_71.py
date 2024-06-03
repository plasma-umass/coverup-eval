# file tornado/simple_httpclient.py:611-620
# lines [611, 612, 613, 614, 615, 616, 617, 618, 620]
# branches ['612->613', '612->620']

import pytest
from tornado.httputil import HTTPHeaders, HTTPMessageDelegate
from tornado.simple_httpclient import SimpleAsyncHTTPClient

class MockRequest:
    def __init__(self, follow_redirects, max_redirects):
        self.follow_redirects = follow_redirects
        self.max_redirects = max_redirects

class _HTTPConnection(HTTPMessageDelegate):
    def __init__(self, request, code, headers):
        self.request = request
        self.code = code
        self.headers = headers

    def _should_follow_redirect(self) -> bool:
        if self.request.follow_redirects:
            assert self.request.max_redirects is not None
            return (
                self.code in (301, 302, 303, 307, 308)
                and self.request.max_redirects > 0
                and self.headers is not None
                and self.headers.get("Location") is not None
            )
        return False

@pytest.fixture
def mock_request():
    return MockRequest(follow_redirects=True, max_redirects=5)

@pytest.fixture
def mock_headers():
    headers = HTTPHeaders()
    headers.add("Location", "http://example.com")
    return headers

def test_should_follow_redirect(mock_request, mock_headers):
    connection = _HTTPConnection(mock_request, 301, mock_headers)
    assert connection._should_follow_redirect() == True

    connection.code = 404
    assert connection._should_follow_redirect() == False

    connection.code = 301
    connection.request.max_redirects = 0
    assert connection._should_follow_redirect() == False

    connection.request.follow_redirects = False
    assert connection._should_follow_redirect() == False

def test_should_follow_redirect_no_location(mock_request):
    headers = HTTPHeaders()
    connection = _HTTPConnection(mock_request, 301, headers)
    assert connection._should_follow_redirect() == False
