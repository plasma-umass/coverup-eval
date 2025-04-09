# file httpie/models.py:43-86
# lines [43, 44, 46, 47, 49, 50, 53, 54, 55, 57, 58, 59, 60, 61, 62, 64, 65, 66, 69, 70, 71, 74, 76, 78, 79, 80, 82, 83, 86]
# branches []

import pytest
from unittest.mock import Mock

from httpie.models import HTTPResponse

@pytest.fixture
def mock_response():
    mock_resp = Mock()
    mock_resp.iter_content = Mock(return_value=iter([b'chunk1', b'chunk2']))
    mock_resp.iter_lines = Mock(return_value=iter([b'line1', b'line2']))
    mock_resp.encoding = 'utf-8'
    mock_resp.content = b'response body'
    
    original_response = Mock()
    original_response.version = 11
    original_response.status = 200
    original_response.reason = 'OK'
    original_response.msg._headers = [('Content-Type', 'application/json')]
    original_response.msg.headers = ['Content-Type: application/json']
    mock_resp.raw._original_response = original_response
    
    return mock_resp

def test_iter_body(mock_response):
    http_response = HTTPResponse(mock_response)
    chunks = list(http_response.iter_body(chunk_size=1))
    assert chunks == [b'chunk1', b'chunk2']

def test_iter_lines(mock_response):
    http_response = HTTPResponse(mock_response)
    lines = list(http_response.iter_lines(chunk_size=1))
    assert lines == [(b'line1', b'\n'), (b'line2', b'\n')]

def test_headers(mock_response):
    http_response = HTTPResponse(mock_response)
    headers = http_response.headers
    expected_headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json'
    assert headers == expected_headers

def test_encoding(mock_response):
    http_response = HTTPResponse(mock_response)
    encoding = http_response.encoding
    assert encoding == 'utf-8'

def test_body(mock_response):
    http_response = HTTPResponse(mock_response)
    body = http_response.body
    assert body == b'response body'
