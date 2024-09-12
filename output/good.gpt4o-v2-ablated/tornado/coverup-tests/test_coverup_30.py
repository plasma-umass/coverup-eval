# file: tornado/httpclient.py:690-729
# asked: {"lines": [690, 691, 711, 714, 715, 717, 718, 719, 720, 722, 723, 729], "branches": []}
# gained: {"lines": [690, 691, 711, 714, 715, 717, 718, 719, 720, 722, 723, 729], "branches": []}

import pytest
from tornado.httpclient import HTTPClientError
from tornado.httpclient import HTTPResponse
from tornado.httputil import HTTPHeaders

def test_http_client_error_basic():
    error = HTTPClientError(404)
    assert error.code == 404
    assert error.message == "Not Found"
    assert error.response is None
    assert str(error) == "HTTP 404: Not Found"
    assert repr(error) == "HTTP 404: Not Found"

def test_http_client_error_with_message():
    error = HTTPClientError(500, "Internal Server Error")
    assert error.code == 500
    assert error.message == "Internal Server Error"
    assert error.response is None
    assert str(error) == "HTTP 500: Internal Server Error"
    assert repr(error) == "HTTP 500: Internal Server Error"

def test_http_client_error_with_response():
    headers = HTTPHeaders({"Content-Type": "text/html"})
    response = HTTPResponse(
        request=None,
        code=302,
        headers=headers,
        effective_url="http://example.com",
        buffer=None,
        request_time=0,
        time_info=None,
        reason="Found",
    )
    error = HTTPClientError(302, response=response)
    assert error.code == 302
    assert error.message == "Found"
    assert error.response == response
    assert str(error) == "HTTP 302: Found"
    assert repr(error) == "HTTP 302: Found"

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
