# file tornado/httpclient.py:671-678
# lines []
# branches ['675->678']

import pytest
from tornado.httpclient import HTTPResponse, HTTPRequest
from io import BytesIO

class MockBuffer(BytesIO):
    def getvalue(self):
        return b"mocked body"

@pytest.fixture
def mock_http_response(mocker):
    request = HTTPRequest(url="http://example.com")
    response = HTTPResponse(request=request, code=200)
    response.buffer = MockBuffer()
    response._body = None
    return response

def test_http_response_body(mock_http_response):
    # Ensure the buffer is not None to hit the elif branch
    assert mock_http_response.buffer is not None
    # Access the body property to trigger the code path
    body = mock_http_response.body
    # Verify the body is set correctly
    assert body == b"mocked body"
    # Verify the _body attribute is now set
    assert mock_http_response._body == b"mocked body"
    # Access the body property again to ensure the cached _body is returned
    body_cached = mock_http_response.body
    assert body_cached == b"mocked body"
