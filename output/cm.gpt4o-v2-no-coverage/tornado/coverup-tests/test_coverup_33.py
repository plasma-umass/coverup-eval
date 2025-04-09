# file: tornado/httpclient.py:690-729
# asked: {"lines": [690, 691, 711, 714, 715, 717, 718, 719, 720, 722, 723, 729], "branches": []}
# gained: {"lines": [690, 691, 711, 714, 715, 717, 718, 719, 720, 722, 723, 729], "branches": []}

import pytest
from tornado.httpclient import HTTPClientError, HTTPResponse
from tornado.httputil import HTTPHeaders

def test_http_client_error_initialization():
    response = HTTPResponse(
        request=None,
        code=404,
        headers=HTTPHeaders(),
        buffer=None,
        effective_url="http://example.com",
        error=None,
        request_time=0.5,
        time_info={"queue": 0.1},
        reason="Not Found",
        start_time=0.0
    )
    error = HTTPClientError(code=404, message="Not Found", response=response)
    assert error.code == 404
    assert error.message == "Not Found"
    assert error.response == response

def test_http_client_error_default_message():
    error = HTTPClientError(code=599)
    assert error.code == 599
    assert error.message == "Unknown"
    assert error.response is None

def test_http_client_error_str():
    error = HTTPClientError(code=500, message="Internal Server Error")
    assert str(error) == "HTTP 500: Internal Server Error"

def test_http_client_error_repr():
    error = HTTPClientError(code=400, message="Bad Request")
    assert repr(error) == "HTTP 400: Bad Request"
