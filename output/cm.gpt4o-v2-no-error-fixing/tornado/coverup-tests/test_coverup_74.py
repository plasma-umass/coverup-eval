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
    try:
        response.rethrow()
    except Exception:
        pytest.fail("rethrow() raised Exception unexpectedly!")

def test_rethrow_with_error():
    request = HTTPRequest(url="http://example.com")
    error = HTTPError(500, message="Internal Server Error")
    response = HTTPResponse(request=request, code=500, error=error)
    with pytest.raises(HTTPError) as excinfo:
        response.rethrow()
    assert excinfo.value == error
