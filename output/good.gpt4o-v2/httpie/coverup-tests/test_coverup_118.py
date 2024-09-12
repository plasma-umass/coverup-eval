# file: httpie/models.py:89-138
# asked: {"lines": [125], "branches": [[109, 112], [123, 125], [135, 138]]}
# gained: {"lines": [], "branches": [[109, 112]]}

import pytest
from unittest.mock import Mock
from httpie.models import HTTPRequest

@pytest.fixture
def mock_request():
    mock_request = Mock()
    mock_request.method = 'GET'
    mock_request.url = 'http://example.com/path?query=1'
    mock_request.headers = {}
    mock_request.body = 'test body'
    return mock_request

def test_headers_with_host(mock_request):
    mock_request.headers = {'Host': 'example.com'}
    request = HTTPRequest(mock_request)
    headers = request.headers
    assert 'Host: example.com' in headers

def test_headers_without_host(mock_request):
    request = HTTPRequest(mock_request)
    headers = request.headers
    assert 'Host: example.com' in headers

def test_headers_bytes_decoding(mock_request):
    mock_request.headers = {'Host': 'example.com'}
    request = HTTPRequest(mock_request)
    # Simulate the headers being bytes
    request._orig.headers = {'Host': b'example.com'}
    headers = request.headers
    assert isinstance(headers, str)

def test_body_encoding(mock_request):
    request = HTTPRequest(mock_request)
    body = request.body
    assert body == b'test body'

def test_body_empty(mock_request):
    mock_request.body = ''
    request = HTTPRequest(mock_request)
    body = request.body
    assert body == b''
