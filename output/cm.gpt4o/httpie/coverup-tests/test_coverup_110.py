# file httpie/models.py:89-138
# lines [125]
# branches ['123->125', '135->138']

import pytest
from unittest.mock import Mock
from httpie.models import HTTPRequest

@pytest.fixture
def mock_request():
    mock_req = Mock()
    mock_req.method = 'GET'
    mock_req.url = 'http://example.com'
    mock_req.headers = {}
    return mock_req

def test_headers_decoding(mock_request):
    mock_request.headers = {'Custom-Header': b'custom-value'}
    request = HTTPRequest(mock_request)
    headers = request.headers
    assert isinstance(headers, str)
    assert 'Host: example.com' in headers
    assert 'Custom-Header: custom-value' in headers

def test_body_encoding(mock_request):
    mock_request.body = 'test body'
    request = HTTPRequest(mock_request)
    body = request.body
    assert isinstance(body, bytes)
    assert body == b'test body'

def test_body_empty(mock_request):
    mock_request.body = None
    request = HTTPRequest(mock_request)
    body = request.body
    assert body == b''
