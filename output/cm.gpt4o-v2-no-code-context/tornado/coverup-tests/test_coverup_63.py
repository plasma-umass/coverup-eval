# file: tornado/httpclient.py:558-563
# asked: {"lines": [558, 559, 560, 561, 563], "branches": [[560, 561], [560, 563]]}
# gained: {"lines": [558, 559, 560, 561, 563], "branches": [[560, 561], [560, 563]]}

import pytest
from tornado.httpclient import HTTPRequest
from tornado import httputil

def test_http_request_headers_setter_with_none():
    request = HTTPRequest(url="http://example.com")
    request.headers = None
    assert isinstance(request._headers, httputil.HTTPHeaders)

def test_http_request_headers_setter_with_dict():
    request = HTTPRequest(url="http://example.com")
    headers_dict = {"Content-Type": "application/json"}
    request.headers = headers_dict
    assert request._headers == headers_dict

def test_http_request_headers_setter_with_httpheaders():
    request = HTTPRequest(url="http://example.com")
    headers_http = httputil.HTTPHeaders({"Content-Type": "application/json"})
    request.headers = headers_http
    assert request._headers == headers_http
