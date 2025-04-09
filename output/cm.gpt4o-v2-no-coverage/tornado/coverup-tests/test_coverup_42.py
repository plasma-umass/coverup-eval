# file: tornado/httpclient.py:671-678
# asked: {"lines": [671, 672, 673, 674, 675, 676, 678], "branches": [[673, 674], [673, 675], [675, 676], [675, 678]]}
# gained: {"lines": [671, 672, 673, 674, 675, 676, 678], "branches": [[673, 674], [673, 675], [675, 676], [675, 678]]}

import pytest
from io import BytesIO
from tornado.httpclient import HTTPResponse
from tornado.httputil import HTTPHeaders
from tornado.httpclient import HTTPRequest

@pytest.fixture
def http_request():
    return HTTPRequest(url="http://example.com")

def test_http_response_body_empty_buffer(http_request):
    response = HTTPResponse(request=http_request, code=200, buffer=None)
    assert response.body == b""

def test_http_response_body_with_buffer(http_request):
    buffer = BytesIO(b"test body")
    response = HTTPResponse(request=http_request, code=200, buffer=buffer)
    assert response.body == b"test body"

def test_http_response_body_cached(http_request):
    buffer = BytesIO(b"test body")
    response = HTTPResponse(request=http_request, code=200, buffer=buffer)
    # Access body to cache it
    _ = response.body
    # Modify buffer to ensure cached value is returned
    buffer.seek(0)
    buffer.write(b"modified body")
    assert response.body == b"test body"
