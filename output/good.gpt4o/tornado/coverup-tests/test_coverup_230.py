# file tornado/httpclient.py:671-678
# lines [674]
# branches ['673->674', '675->678']

import pytest
from tornado.httpclient import HTTPResponse, HTTPRequest
from io import BytesIO

class MockBuffer(BytesIO):
    def getvalue(self):
        return b"mocked body"

@pytest.fixture
def mock_http_response(mocker):
    request = HTTPRequest("http://example.com")
    response = HTTPResponse(request, 200)
    response.buffer = MockBuffer()
    response._body = None
    return response

def test_http_response_body_with_buffer(mock_http_response):
    response = mock_http_response
    assert response.body == b"mocked body"
    assert response._body == b"mocked body"

def test_http_response_body_without_buffer(mocker):
    request = HTTPRequest("http://example.com")
    response = HTTPResponse(request, 200)
    response.buffer = None
    assert response.body == b""
