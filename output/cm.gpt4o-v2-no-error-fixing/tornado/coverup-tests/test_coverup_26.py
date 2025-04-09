# file: tornado/httpclient.py:690-729
# asked: {"lines": [690, 691, 711, 714, 715, 717, 718, 719, 720, 722, 723, 729], "branches": []}
# gained: {"lines": [690, 691, 711, 714, 715, 717, 718, 719, 720, 722, 723, 729], "branches": []}

import pytest
from tornado.httpclient import HTTPClientError
from tornado.httpclient import HTTPResponse
from tornado.httputil import HTTPHeaders
from tornado import httputil

def test_http_client_error_init():
    response = HTTPResponse(
        request=None,
        code=404,
        headers=HTTPHeaders({"Content-Type": "text/html"}),
        buffer=None,
        effective_url="http://example.com",
    )
    error = HTTPClientError(404, "Not Found", response)
    assert error.code == 404
    assert error.message == "Not Found"
    assert error.response == response

def test_http_client_error_default_message():
    error = HTTPClientError(599)
    assert error.code == 599
    assert error.message == httputil.responses.get(599, "Unknown")
    assert error.response is None

def test_http_client_error_str():
    error = HTTPClientError(404, "Not Found")
    assert str(error) == "HTTP 404: Not Found"

def test_http_client_error_repr():
    error = HTTPClientError(404, "Not Found")
    assert repr(error) == "HTTP 404: Not Found"
