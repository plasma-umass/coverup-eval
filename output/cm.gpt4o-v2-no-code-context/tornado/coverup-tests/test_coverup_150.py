# file: tornado/httpclient.py:685-687
# asked: {"lines": [685, 686, 687], "branches": []}
# gained: {"lines": [685, 686, 687], "branches": []}

import pytest
from tornado.httpclient import HTTPResponse, HTTPRequest
from io import BytesIO

def test_httpresponse_repr():
    request = HTTPRequest(url="http://example.com")
    buffer = BytesIO(b"Test body")
    response = HTTPResponse(request=request, code=200, buffer=buffer)
    response.headers = {"Content-Type": "text/plain"}
    
    repr_str = repr(response)
    
    assert repr_str.startswith("HTTPResponse(")
    assert "code=200" in repr_str
    assert "headers={'Content-Type': 'text/plain'}" in repr_str
    assert "buffer=<_io.BytesIO" in repr_str
