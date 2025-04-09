# file tornado/httpclient.py:574-623
# lines [574, 575]
# branches []

import pytest
from tornado.httpclient import HTTPResponse
from tornado.httputil import HTTPHeaders
from io import BytesIO

@pytest.fixture
def http_response():
    request = object()  # Mock request object
    code = 200
    reason = 'OK'
    headers = HTTPHeaders()
    effective_url = 'http://example.com'
    buffer = BytesIO(b"response body")
    error = None
    request_time = 1.0
    start_time = 1234567890.0
    time_info = {'namelookup': 0.1, 'connect': 0.2, 'appconnect': 0.3, 'pretransfer': 0.4, 'starttransfer': 0.5, 'total': 1.0}
    
    response = HTTPResponse(request, code, reason=reason, headers=headers, effective_url=effective_url, buffer=buffer, error=error, request_time=request_time, start_time=start_time, time_info=time_info)
    return response

def test_http_response(http_response):
    assert http_response.request is not None
    assert http_response.code == 200
    assert http_response.reason == 'OK'
    assert isinstance(http_response.headers, HTTPHeaders)
    assert http_response.effective_url == 'http://example.com'
    assert http_response.buffer.getvalue() == b"response body"
    assert http_response.body == b"response body"
    assert http_response.error is None
    assert http_response.request_time == 1.0
    assert http_response.start_time == 1234567890.0
    assert http_response.time_info == {'namelookup': 0.1, 'connect': 0.2, 'appconnect': 0.3, 'pretransfer': 0.4, 'starttransfer': 0.5, 'total': 1.0}
