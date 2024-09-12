# file: tornado/httpclient.py:551-556
# asked: {"lines": [551, 552, 556], "branches": []}
# gained: {"lines": [551, 552, 556], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.httputil import HTTPHeaders

def test_http_request_headers_property():
    # Create an instance of HTTPRequest with HTTPHeaders
    headers = HTTPHeaders({"Content-Type": "application/json"})
    request = HTTPRequest(url="http://example.com", headers=headers)
    
    # Access the headers property to ensure the getter is called
    assert request.headers["Content-Type"] == "application/json"

    # Modify the headers to ensure the setter is called
    new_headers = HTTPHeaders({"Content-Type": "text/html"})
    request.headers = new_headers
    assert request.headers["Content-Type"] == "text/html"

    # Clean up
    del request

def test_http_request_headers_property_with_dict():
    # Create an instance of HTTPRequest with a dict for headers
    headers = {"Content-Type": "application/json"}
    request = HTTPRequest(url="http://example.com", headers=headers)
    
    # Access the headers property to ensure the getter is called
    assert request.headers["Content-Type"] == "application/json"

    # Modify the headers to ensure the setter is called
    new_headers = {"Content-Type": "text/html"}
    request.headers = new_headers
    assert request.headers["Content-Type"] == "text/html"

    # Clean up
    del request
