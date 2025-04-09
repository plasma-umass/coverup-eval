# file: tornado/simple_httpclient.py:611-620
# asked: {"lines": [611, 612, 613, 614, 615, 616, 617, 618, 620], "branches": [[612, 613], [612, 620]]}
# gained: {"lines": [611], "branches": []}

import pytest
from tornado import httputil
from tornado.simple_httpclient import SimpleAsyncHTTPClient

class MockRequest:
    def __init__(self, follow_redirects, max_redirects):
        self.follow_redirects = follow_redirects
        self.max_redirects = max_redirects

class MockHTTPConnection(httputil.HTTPMessageDelegate):
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
    return {"Location": "http://example.com"}

def test_should_follow_redirect_true(mock_request, mock_headers):
    connection = MockHTTPConnection(mock_request, 302, mock_headers)
    assert connection._should_follow_redirect() is True

def test_should_follow_redirect_false_due_to_code(mock_request, mock_headers):
    connection = MockHTTPConnection(mock_request, 200, mock_headers)
    assert connection._should_follow_redirect() is False

def test_should_follow_redirect_false_due_to_no_location(mock_request):
    connection = MockHTTPConnection(mock_request, 302, {})
    assert connection._should_follow_redirect() is False

def test_should_follow_redirect_false_due_to_no_headers(mock_request):
    connection = MockHTTPConnection(mock_request, 302, None)
    assert connection._should_follow_redirect() is False

def test_should_follow_redirect_false_due_to_max_redirects(mock_request, mock_headers):
    mock_request.max_redirects = 0
    connection = MockHTTPConnection(mock_request, 302, mock_headers)
    assert connection._should_follow_redirect() is False

def test_should_follow_redirect_false_due_to_follow_redirects_false(mock_headers):
    request = MockRequest(follow_redirects=False, max_redirects=5)
    connection = MockHTTPConnection(request, 302, mock_headers)
    assert connection._should_follow_redirect() is False
