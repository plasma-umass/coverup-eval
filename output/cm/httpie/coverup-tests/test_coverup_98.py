# file httpie/models.py:43-86
# lines [71, 74]
# branches []

import pytest
from httpie.models import HTTPResponse
from requests.models import Response
from unittest.mock import MagicMock

class MockRaw:
    def __init__(self, version, status, reason, headers):
        self._original_response = MagicMock()
        self._original_response.version = version
        self._original_response.status = status
        self._original_response.reason = reason
        self._original_response.msg = MagicMock()
        self._original_response.msg.headers = headers

@pytest.fixture
def mock_response():
    response = Response()
    response.raw = MockRaw(version=11, status=200, reason='OK', headers=['Content-Type: text/html\r\n', 'Connection: close\r\n'])
    return HTTPResponse(response)

def test_http_response_headers_attribute_error(mock_response):
    # Simulate the AttributeError by deleting the _headers attribute
    del mock_response._orig.raw._original_response.msg._headers
    headers = mock_response.headers
    assert 'HTTP/1.1 200 OK' in headers
    assert 'Content-Type: text/html' in headers
    assert 'Connection: close' in headers
