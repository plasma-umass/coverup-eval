# file: tornado/httpclient.py:680-683
# asked: {"lines": [680, 682, 683], "branches": [[682, 0], [682, 683]]}
# gained: {"lines": [680, 682, 683], "branches": [[682, 0], [682, 683]]}

import pytest
from tornado.httpclient import HTTPResponse, HTTPError

class MockError(Exception):
    pass

@pytest.fixture
def http_response():
    class MockHTTPResponse(HTTPResponse):
        def __init__(self, error=None):
            self.error = error
    return MockHTTPResponse

def test_rethrow_no_error(http_response):
    response = http_response()
    response.rethrow()  # Should not raise any exception

def test_rethrow_with_error(http_response):
    error = MockError("Test error")
    response = http_response(error=error)
    with pytest.raises(MockError) as excinfo:
        response.rethrow()
    assert str(excinfo.value) == "Test error"
