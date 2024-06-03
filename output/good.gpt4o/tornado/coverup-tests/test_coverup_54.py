# file tornado/simple_httpclient.py:205-220
# lines [205, 211, 212, 213, 214, 215, 216, 217, 218, 219]
# branches []

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest, HTTPResponse
from unittest.mock import Mock, call

@pytest.fixture
def mock_connection_class(mocker):
    return mocker.patch('tornado.simple_httpclient.SimpleAsyncHTTPClient._connection_class')

@pytest.fixture
def simple_async_http_client(mock_connection_class):
    client = SimpleAsyncHTTPClient()
    mock_connection_class.return_value = Mock()
    return client

def test_handle_request(simple_async_http_client, mock_connection_class):
    request = HTTPRequest(url="http://example.com")
    release_callback = Mock()
    final_callback = Mock()

    simple_async_http_client._handle_request(request, release_callback, final_callback)

    mock_connection_class.assert_called_once()
    mock_connection_class.return_value.assert_called_once_with(
        simple_async_http_client,
        request,
        release_callback,
        final_callback,
        simple_async_http_client.max_buffer_size,
        simple_async_http_client.tcp_client,
        simple_async_http_client.max_header_size,
        simple_async_http_client.max_body_size,
    )
