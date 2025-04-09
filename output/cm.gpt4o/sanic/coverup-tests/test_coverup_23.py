# file sanic/response.py:81-100
# lines [81, 82, 92, 93, 94, 95, 97, 98, 99]
# branches ['92->93', '92->94', '94->95', '94->97']

import pytest
from unittest.mock import Mock
from sanic.response import BaseHTTPResponse

def remove_entity_headers(headers):
    # Mock implementation of remove_entity_headers
    return {k: v for k, v in headers.items() if k.lower() not in ["content-length", "content-type"]}

def has_message_body(status):
    # Mock implementation of has_message_body
    return status not in (204, 304, 412)

@pytest.fixture
def mock_response(mocker):
    mocker.patch('sanic.response.remove_entity_headers', side_effect=remove_entity_headers)
    mocker.patch('sanic.response.has_message_body', side_effect=has_message_body)
    return BaseHTTPResponse()

def test_processed_headers_304_status(mock_response):
    mock_response.status = 304
    mock_response.headers = {"content-length": "123", "x-custom-header": "value"}
    mock_response.content_type = "text/plain"

    headers = list(mock_response.processed_headers)

    assert headers == [(b'x-custom-header', b'value')]

def test_processed_headers_200_status(mock_response):
    mock_response.status = 200
    mock_response.headers = {"x-custom-header": "value"}
    mock_response.content_type = "text/plain"

    headers = list(mock_response.processed_headers)

    assert headers == [(b'x-custom-header', b'value'), (b'content-type', b'text/plain')]

def test_processed_headers_412_status(mock_response):
    mock_response.status = 412
    mock_response.headers = {"content-length": "123", "x-custom-header": "value"}
    mock_response.content_type = "text/plain"

    headers = list(mock_response.processed_headers)

    assert headers == [(b'x-custom-header', b'value')]

def test_processed_headers_no_message_body(mock_response):
    mock_response.status = 204
    mock_response.headers = {"x-custom-header": "value"}
    mock_response.content_type = "text/plain"

    headers = list(mock_response.processed_headers)

    assert headers == [(b'x-custom-header', b'value')]
