# file: tornado/httpclient.py:569-571
# asked: {"lines": [569, 570, 571], "branches": []}
# gained: {"lines": [569, 570, 571], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.escape import utf8

def test_http_request_body_setter_bytes():
    request = HTTPRequest(url="http://example.com")
    request.body = b"test body"
    assert request.body == utf8(b"test body")

def test_http_request_body_setter_str():
    request = HTTPRequest(url="http://example.com")
    request.body = "test body"
    assert request.body == utf8("test body")
