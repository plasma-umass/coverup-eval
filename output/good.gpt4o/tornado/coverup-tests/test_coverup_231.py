# file tornado/httpclient.py:629-669
# lines [666]
# branches ['659->666']

import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse, HTTPError
from tornado.httputil import HTTPHeaders
from io import BytesIO

def test_http_response_with_error():
    request = HTTPRequest(url="http://example.com")
    error = HTTPError(599, "Custom Error")
    response = HTTPResponse(
        request=request,
        code=599,
        error=error,
        reason="Custom Error"
    )
    
    assert response.error == error
    assert response.code == 599
    assert response.reason == "Custom Error"
    assert response.request == request
    assert response.effective_url == "http://example.com"
    assert response._error_is_response_code == False
