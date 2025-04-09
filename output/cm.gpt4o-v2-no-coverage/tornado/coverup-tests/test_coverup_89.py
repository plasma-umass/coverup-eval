# file: tornado/httpclient.py:558-563
# asked: {"lines": [558, 559, 560, 561, 563], "branches": [[560, 561], [560, 563]]}
# gained: {"lines": [558, 559, 560, 561, 563], "branches": [[560, 561], [560, 563]]}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.httputil import HTTPHeaders

def test_http_request_headers_setter_with_none():
    request = HTTPRequest(url="http://example.com")
    request.headers = None
    assert isinstance(request.headers, HTTPHeaders)
    assert len(request.headers) == 0

def test_http_request_headers_setter_with_dict():
    request = HTTPRequest(url="http://example.com")
    headers_dict = {'Content-Type': 'application/json'}
    request.headers = headers_dict
    assert isinstance(request.headers, dict)
    assert request.headers['Content-Type'] == 'application/json'

def test_http_request_headers_setter_with_httpheaders():
    request = HTTPRequest(url="http://example.com")
    headers = HTTPHeaders({'Content-Type': 'application/json'})
    request.headers = headers
    assert isinstance(request.headers, HTTPHeaders)
    assert request.headers['Content-Type'] == 'application/json'
