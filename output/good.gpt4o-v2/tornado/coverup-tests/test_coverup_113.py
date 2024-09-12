# file: tornado/httpclient.py:685-687
# asked: {"lines": [685, 686, 687], "branches": []}
# gained: {"lines": [685, 686, 687], "branches": []}

import pytest
from tornado.httpclient import HTTPResponse
from tornado.httpclient import HTTPRequest
from tornado.httputil import HTTPHeaders
from io import BytesIO

def test_http_response_repr():
    request = HTTPRequest(url="http://example.com")
    headers = HTTPHeaders({"Content-Type": "text/html"})
    buffer = BytesIO(b"response body")
    response = HTTPResponse(
        request=request,
        code=200,
        headers=headers,
        buffer=buffer,
        effective_url="http://example.com",
        error=None,
        request_time=0.5,
        time_info={"queue": 0.1},
        reason="OK",
        start_time=0.0
    )
    repr_str = repr(response)
    assert repr_str.startswith("HTTPResponse(")
    assert "request=<tornado.httpclient.HTTPRequest" in repr_str
    assert "code=200" in repr_str
    assert "headers=<tornado.httputil.HTTPHeaders" in repr_str
    assert "buffer=<_io.BytesIO" in repr_str
    assert "effective_url='http://example.com'" in repr_str
    assert "error=None" in repr_str
    assert "request_time=0.5" in repr_str
    assert "time_info={'queue': 0.1}" in repr_str
    assert "reason='OK'" in repr_str
    assert "start_time=0.0" in repr_str
