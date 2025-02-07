# file: tornado/httpclient.py:671-678
# asked: {"lines": [671, 672, 673, 674, 675, 676, 678], "branches": [[673, 674], [673, 675], [675, 676], [675, 678]]}
# gained: {"lines": [671, 672, 673, 674, 675, 676, 678], "branches": [[673, 674], [673, 675], [675, 676], [675, 678]]}

import pytest
from io import BytesIO
from tornado.httpclient import HTTPResponse, HTTPRequest
from tornado.httputil import HTTPHeaders

def test_http_response_body_with_none_buffer():
    request = HTTPRequest(url="http://example.com")
    response = HTTPResponse(request=request, code=200, buffer=None)
    assert response.body == b""

def test_http_response_body_with_empty_buffer():
    request = HTTPRequest(url="http://example.com")
    buffer = BytesIO()
    response = HTTPResponse(request=request, code=200, buffer=buffer)
    assert response.body == b""

def test_http_response_body_with_non_empty_buffer():
    request = HTTPRequest(url="http://example.com")
    buffer = BytesIO(b"test body")
    response = HTTPResponse(request=request, code=200, buffer=buffer)
    assert response.body == b"test body"
    assert response._body == b"test body"

def test_http_response_body_cached():
    request = HTTPRequest(url="http://example.com")
    buffer = BytesIO(b"test body")
    response = HTTPResponse(request=request, code=200, buffer=buffer)
    # Access body to cache it
    _ = response.body
    # Modify buffer to ensure cached body is returned
    buffer.write(b" modified")
    assert response.body == b"test body"
