# file: tornado/httpclient.py:551-556
# asked: {"lines": [551, 552, 556], "branches": []}
# gained: {"lines": [551, 552, 556], "branches": []}

import pytest
from tornado import httputil
from tornado.httpclient import HTTPRequest

class MockHTTPRequest(HTTPRequest):
    def __init__(self, headers):
        self._headers = headers

def test_http_request_headers_with_http_headers():
    headers = httputil.HTTPHeaders({"Content-Type": "application/json"})
    request = MockHTTPRequest(headers)
    assert request.headers["Content-Type"] == "application/json"

def test_http_request_headers_with_dict():
    headers = {"Content-Type": "application/json"}
    request = MockHTTPRequest(headers)
    assert request.headers["Content-Type"] == "application/json"
