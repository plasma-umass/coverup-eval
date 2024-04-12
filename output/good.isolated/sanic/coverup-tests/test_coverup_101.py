# file sanic/response.py:81-100
# lines [92, 93, 94, 95, 97, 98, 99]
# branches ['92->93', '92->94', '94->95', '94->97']

import pytest
from sanic.response import BaseHTTPResponse

@pytest.fixture
def mock_remove_entity_headers(mocker):
    return mocker.patch('sanic.response.remove_entity_headers', return_value={})

@pytest.fixture
def mock_has_message_body(mocker):
    return mocker.patch('sanic.response.has_message_body', return_value=True)

def test_processed_headers_with_status_304_or_412(mock_remove_entity_headers, mock_has_message_body):
    response = BaseHTTPResponse()
    response.status = 304
    response.headers = {'content-type': 'text/plain', 'content-length': '123'}
    response.content_type = 'text/html'
    
    headers = list(response.processed_headers)
    
    mock_remove_entity_headers.assert_called_once()
    mock_has_message_body.assert_called_once()
    assert (b'content-type', b'text/html') in headers
    assert (b'content-length', b'123') not in headers

def test_processed_headers_with_message_body(mock_remove_entity_headers, mock_has_message_body):
    response = BaseHTTPResponse()
    response.status = 200
    response.headers = {'content-type': 'text/plain'}
    response.content_type = 'text/html'
    
    headers = list(response.processed_headers)
    
    mock_remove_entity_headers.assert_not_called()
    mock_has_message_body.assert_called_once()
    assert (b'content-type', b'text/plain') in headers
