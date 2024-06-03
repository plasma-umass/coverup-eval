# file tornado/httpclient.py:558-563
# lines [558, 559, 560, 561, 563]
# branches ['560->561', '560->563']

import pytest
from tornado.httpclient import HTTPRequest
from tornado import httputil

def test_http_request_headers_setter():
    # Test setting headers to None
    request = HTTPRequest(url="http://example.com")
    request.headers = None
    assert isinstance(request._headers, httputil.HTTPHeaders)

    # Test setting headers to a dictionary
    headers_dict = {'Content-Type': 'application/json'}
    request.headers = headers_dict
    assert request._headers == headers_dict

    # Test setting headers to an instance of httputil.HTTPHeaders
    headers_instance = httputil.HTTPHeaders({'Content-Type': 'application/json'})
    request.headers = headers_instance
    assert request._headers == headers_instance
