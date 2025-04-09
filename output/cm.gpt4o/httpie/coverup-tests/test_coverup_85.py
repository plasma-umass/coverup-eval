# file httpie/models.py:43-86
# lines [71, 74]
# branches []

import pytest
from unittest.mock import Mock

from httpie.models import HTTPResponse

@pytest.fixture
def mock_response():
    mock_resp = Mock()
    mock_resp.raw._original_response.version = 11
    mock_resp.raw._original_response.status = 200
    mock_resp.raw._original_response.reason = 'OK'
    return mock_resp

def test_headers_with_attribute_error(mocker, mock_response):
    # Simulate the AttributeError by setting up the mock to not have _headers
    mock_response.raw._original_response.msg = Mock()
    del mock_response.raw._original_response.msg._headers
    mock_response.raw._original_response.msg.headers = ['Content-Type: text/html\r\n', 'Content-Length: 123\r\n']

    http_response = HTTPResponse(mock_response)
    headers = http_response.headers

    assert 'HTTP/1.1 200 OK' in headers
    assert 'Content-Type: text/html' in headers
    assert 'Content-Length: 123' in headers
