# file tornado/httpclient.py:680-683
# lines [680, 682, 683]
# branches ['682->exit', '682->683']

import pytest
from tornado.httpclient import HTTPError

class HTTPResponse:
    def __init__(self, error=None):
        self.error = error

    def rethrow(self) -> None:
        """If there was an error on the request, raise an `HTTPError`."""
        if self.error:
            raise self.error

def test_http_response_rethrow_no_error():
    response = HTTPResponse()
    try:
        response.rethrow()
    except Exception as e:
        pytest.fail(f"rethrow() raised {e} unexpectedly!")

def test_http_response_rethrow_with_error():
    error = HTTPError(500, "Internal Server Error")
    response = HTTPResponse(error=error)
    with pytest.raises(HTTPError) as excinfo:
        response.rethrow()
    assert excinfo.value == error
