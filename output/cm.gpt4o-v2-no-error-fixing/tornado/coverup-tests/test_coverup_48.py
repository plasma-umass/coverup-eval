# file: tornado/simple_httpclient.py:611-620
# asked: {"lines": [611, 612, 613, 614, 615, 616, 617, 618, 620], "branches": [[612, 613], [612, 620]]}
# gained: {"lines": [611], "branches": []}

import pytest
from tornado.httputil import HTTPHeaders
from tornado.simple_httpclient import SimpleAsyncHTTPClient

class MockRequest:
    def __init__(self, follow_redirects, max_redirects):
        self.follow_redirects = follow_redirects
        self.max_redirects = max_redirects

class MockHTTPConnection:
    def __init__(self, request, code, headers):
        self.request = request
        self.code = code
        self.headers = headers

    def _should_follow_redirect(self):
        if self.request.follow_redirects:
            assert self.request.max_redirects is not None
            return (
                self.code in (301, 302, 303, 307, 308)
                and self.request.max_redirects > 0
                and self.headers is not None
                and self.headers.get("Location") is not None
            )
        return False

@pytest.mark.parametrize("follow_redirects, max_redirects, code, headers, expected", [
    (True, 1, 301, HTTPHeaders({"Location": "http://example.com"}), True),
    (True, 1, 302, HTTPHeaders({"Location": "http://example.com"}), True),
    (True, 1, 303, HTTPHeaders({"Location": "http://example.com"}), True),
    (True, 1, 307, HTTPHeaders({"Location": "http://example.com"}), True),
    (True, 1, 308, HTTPHeaders({"Location": "http://example.com"}), True),
    (True, 1, 200, HTTPHeaders({"Location": "http://example.com"}), False),
    (True, 0, 301, HTTPHeaders({"Location": "http://example.com"}), False),
    (True, 1, 301, HTTPHeaders(), False),
    (False, 1, 301, HTTPHeaders({"Location": "http://example.com"}), False),
])
def test_should_follow_redirect(follow_redirects, max_redirects, code, headers, expected):
    request = MockRequest(follow_redirects, max_redirects)
    connection = MockHTTPConnection(request, code, headers)
    assert connection._should_follow_redirect() == expected
