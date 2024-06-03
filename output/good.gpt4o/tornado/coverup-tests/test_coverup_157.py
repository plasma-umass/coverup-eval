# file tornado/httpclient.py:574-623
# lines [574, 575]
# branches []

import pytest
from tornado.httpclient import HTTPResponse
from tornado.httputil import HTTPHeaders
from io import BytesIO

@pytest.fixture
def mock_http_response():
    request = "mock_request"
    code = 200
    reason = "OK"
    headers = HTTPHeaders({"Content-Type": "text/html"})
    effective_url = "http://example.com"
    buffer = BytesIO(b"response body")
    error = None
    request_time = 0.5
    start_time = 0.0
    time_info = {"queue": 0.1}

    return HTTPResponse(
        request=request,
        code=code,
        reason=reason,
        headers=headers,
        effective_url=effective_url,
        buffer=buffer,
        error=error,
        request_time=request_time,
        start_time=start_time,
        time_info=time_info
    )

def test_http_response_attributes(mock_http_response):
    response = mock_http_response

    assert response.request == "mock_request"
    assert response.code == 200
    assert response.reason == "OK"
    assert response.headers["Content-Type"] == "text/html"
    assert response.effective_url == "http://example.com"
    assert response.buffer.getvalue() == b"response body"
    assert response.body == b"response body"
    assert response.error is None
    assert response.request_time == 0.5
    assert response.start_time == 0.0
    assert response.time_info["queue"] == 0.1

    # Clean up
    response.buffer.close()
