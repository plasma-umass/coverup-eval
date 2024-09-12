# file: tornado/httpclient.py:558-563
# asked: {"lines": [558, 559, 560, 561, 563], "branches": [[560, 561], [560, 563]]}
# gained: {"lines": [558, 559, 560, 561, 563], "branches": [[560, 561], [560, 563]]}

import pytest
from tornado import httputil
from tornado.httpclient import HTTPRequest

def test_http_request_headers_setter_with_none():
    request = HTTPRequest("http://example.com")
    request.headers = None
    assert isinstance(request.headers, httputil.HTTPHeaders)

def test_http_request_headers_setter_with_dict():
    request = HTTPRequest("http://example.com")
    headers_dict = {"Content-Type": "application/json"}
    request.headers = headers_dict
    assert request.headers["Content-Type"] == "application/json"

def test_http_request_headers_setter_with_httpheaders():
    request = HTTPRequest("http://example.com")
    headers = httputil.HTTPHeaders({"Content-Type": "application/json"})
    request.headers = headers
    assert request.headers["Content-Type"] == "application/json"
