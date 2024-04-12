# file httpie/models.py:43-86
# lines [43, 44, 46, 47, 49, 50, 53, 54, 55, 57, 58, 59, 60, 61, 62, 64, 65, 66, 69, 70, 71, 74, 76, 78, 79, 80, 82, 83, 86]
# branches []

import pytest
from httpie.models import HTTPResponse
from requests.models import Response
from unittest.mock import MagicMock

@pytest.fixture
def mock_response():
    mock = MagicMock(spec=Response)
    mock.iter_content.return_value = iter([b'chunk'])
    mock.iter_lines.return_value = iter([b'line'])
    mock.encoding = None
    mock.content = b'body content'
    
    # Create a mock for the raw attribute and its chain of attributes
    mock.raw = MagicMock()
    mock.raw._original_response = MagicMock()
    mock.raw._original_response.version = 11
    mock.raw._original_response.status = 200
    mock.raw._original_response.reason = 'OK'
    mock.raw._original_response.msg = MagicMock()
    mock.raw._original_response.msg._headers = [('Header', 'Value')]
    
    return mock

def test_http_response_headers(mock_response):
    http_response = HTTPResponse(mock_response)
    headers = http_response.headers
    assert 'HTTP/1.1 200 OK' in headers
    assert 'Header: Value' in headers

def test_http_response_iter_body(mock_response):
    http_response = HTTPResponse(mock_response)
    chunks = list(http_response.iter_body(chunk_size=5))
    assert chunks == [b'chunk']

def test_http_response_iter_lines(mock_response):
    http_response = HTTPResponse(mock_response)
    lines = list(http_response.iter_lines(chunk_size=5))
    assert lines == [(b'line', b'\n')]

def test_http_response_encoding(mock_response):
    http_response = HTTPResponse(mock_response)
    assert http_response.encoding == 'utf8'

def test_http_response_body(mock_response):
    http_response = HTTPResponse(mock_response)
    assert http_response.body == b'body content'
