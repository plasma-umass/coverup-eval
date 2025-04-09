# file: tornado/httpclient.py:565-567
# asked: {"lines": [565, 566, 567], "branches": []}
# gained: {"lines": [565, 566, 567], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest

class TestHTTPRequest:
    def test_body_property(self):
        request = HTTPRequest(url="http://example.com")
        request._body = b"test body"
        assert request.body == b"test body"
