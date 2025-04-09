# file: tornado/httpclient.py:680-683
# asked: {"lines": [680, 682, 683], "branches": [[682, 0], [682, 683]]}
# gained: {"lines": [680, 682, 683], "branches": [[682, 0], [682, 683]]}

import pytest
from tornado.httpclient import HTTPResponse, HTTPRequest, HTTPError
from tornado.httputil import HTTPHeaders
from io import BytesIO

def test_rethrow_no_error():
    request = HTTPRequest(url="http://example.com")
    response = HTTPResponse(request=request, code=200)
    # Should not raise an error
    response.rethrow()

def test_rethrow_with_error():
    request = HTTPRequest(url="http://example.com")
    error = HTTPError(500, message="Internal Server Error")
    response = HTTPResponse(request=request, code=500, error=error)
    with pytest.raises(HTTPError) as excinfo:
        response.rethrow()
    assert excinfo.value == error

def test_rethrow_error_from_response_code():
    request = HTTPRequest(url="http://example.com")
    response = HTTPResponse(request=request, code=404)
    with pytest.raises(HTTPError) as excinfo:
        response.rethrow()
    assert excinfo.value.code == 404
    assert excinfo.value.message == "Not Found"
