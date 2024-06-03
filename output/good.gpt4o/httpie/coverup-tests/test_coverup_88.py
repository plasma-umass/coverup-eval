# file httpie/models.py:89-138
# lines [125]
# branches ['109->112', '123->125', '135->138']

import pytest
from unittest.mock import Mock
from httpie.models import HTTPRequest
from urllib.parse import urlsplit

@pytest.fixture
def mock_request():
    mock = Mock()
    mock.method = 'GET'
    mock.url = 'http://example.com/path?query=1'
    mock.headers = {}
    mock.body = 'test body'
    return mock

def test_headers_with_host(mock_request):
    mock_request.headers = {}
    request = HTTPRequest(mock_request)
    headers = request.headers
    assert 'Host: example.com' in headers

def test_headers_without_host(mock_request):
    mock_request.headers = {'Host': 'example.com'}
    request = HTTPRequest(mock_request)
    headers = request.headers
    assert 'Host: example.com' in headers

def test_headers_bytes_decoding(mock_request):
    mock_request.headers = {}
    request = HTTPRequest(mock_request)
    headers = request.headers
    assert isinstance(headers, str)

def test_body_encoding(mock_request):
    mock_request.body = 'test body'
    request = HTTPRequest(mock_request)
    body = request.body
    assert body == b'test body'

def test_body_empty(mock_request):
    mock_request.body = ''
    request = HTTPRequest(mock_request)
    body = request.body
    assert body == b''

