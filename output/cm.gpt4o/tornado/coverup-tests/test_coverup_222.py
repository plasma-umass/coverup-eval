# file tornado/httpclient.py:680-683
# lines [682, 683]
# branches ['682->exit', '682->683']

import pytest
from tornado.httpclient import HTTPResponse, HTTPError

class MockHTTPResponse(HTTPResponse):
    def __init__(self, error=None):
        self.error = error

def test_rethrow_with_error():
    error = HTTPError(500, "Internal Server Error")
    response = MockHTTPResponse(error=error)
    
    with pytest.raises(HTTPError) as excinfo:
        response.rethrow()
    
    assert excinfo.value == error

def test_rethrow_without_error():
    response = MockHTTPResponse(error=None)
    
    # Should not raise any exception
    response.rethrow()
