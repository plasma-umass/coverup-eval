# file: tornado/httpclient.py:629-669
# asked: {"lines": [643, 651, 655, 664, 666], "branches": [[642, 643], [648, 651], [654, 655], [659, 666], [660, 664]]}
# gained: {"lines": [651, 655, 664, 666], "branches": [[648, 651], [654, 655], [659, 666], [660, 664]]}

import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse, HTTPError
from tornado.httputil import HTTPHeaders
from io import BytesIO
from unittest.mock import Mock

@pytest.fixture
def mock_request():
    return Mock(spec=HTTPRequest, url="http://example.com")

def test_http_response_initialization_with_all_params(mock_request):
    headers = HTTPHeaders({"Content-Type": "application/json"})
    buffer = BytesIO(b"test")
    effective_url = "http://example.com/redirect"
    error = HTTPError(404)
    request_time = 0.5
    time_info = {"start": 0.0, "end": 0.5}
    reason = "Not Found"
    start_time = 0.0

    response = HTTPResponse(
        request=mock_request,
        code=404,
        headers=headers,
        buffer=buffer,
        effective_url=effective_url,
        error=error,
        request_time=request_time,
        time_info=time_info,
        reason=reason,
        start_time=start_time,
    )

    assert response.request == mock_request
    assert response.code == 404
    assert response.headers == headers
    assert response.buffer == buffer
    assert response.effective_url == effective_url
    assert response.error == error
    assert response.request_time == request_time
    assert response.time_info == time_info
    assert response.reason == reason
    assert response.start_time == start_time

def test_http_response_initialization_with_defaults(mock_request):
    response = HTTPResponse(
        request=mock_request,
        code=200,
    )

    assert response.request == mock_request
    assert response.code == 200
    assert response.headers == HTTPHeaders()
    assert response.buffer is None
    assert response.effective_url == mock_request.url
    assert response.error is None
    assert response.request_time is None
    assert response.time_info == {}
    assert response.reason == "OK"
    assert response.start_time is None

def test_http_response_initialization_with_error_code(mock_request):
    response = HTTPResponse(
        request=mock_request,
        code=404,
    )

    assert response.request == mock_request
    assert response.code == 404
    assert response.headers == HTTPHeaders()
    assert response.buffer is None
    assert response.effective_url == mock_request.url
    assert isinstance(response.error, HTTPError)
    assert response.error.code == 404
    assert response.request_time is None
    assert response.time_info == {}
    assert response.reason == "Not Found"
    assert response.start_time is None
    assert response._error_is_response_code

def test_http_response_initialization_with_custom_reason(mock_request):
    response = HTTPResponse(
        request=mock_request,
        code=500,
        reason="Custom Error"
    )

    assert response.request == mock_request
    assert response.code == 500
    assert response.headers == HTTPHeaders()
    assert response.buffer is None
    assert response.effective_url == mock_request.url
    assert isinstance(response.error, HTTPError)
    assert response.error.code == 500
    assert response.request_time is None
    assert response.time_info == {}
    assert response.reason == "Custom Error"
    assert response.start_time is None
    assert response._error_is_response_code
