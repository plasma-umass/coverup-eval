# file: tornado/httpclient.py:569-571
# asked: {"lines": [569, 570, 571], "branches": []}
# gained: {"lines": [569, 570, 571], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.escape import utf8

class TestHTTPRequest:
    def test_body_setter_with_bytes(self):
        request = HTTPRequest(url="http://example.com")
        request.body = b"test"
        assert request._body == utf8(b"test")

    def test_body_setter_with_str(self):
        request = HTTPRequest(url="http://example.com")
        request.body = "test"
        assert request._body == utf8("test")
