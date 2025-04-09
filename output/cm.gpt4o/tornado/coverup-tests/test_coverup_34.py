# file tornado/simple_httpclient.py:192-200
# lines [192, 193, 194, 195, 196, 197, 198, 199, 200]
# branches ['193->exit', '193->194', '195->196', '195->197']

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest
from unittest.mock import MagicMock, patch
import collections

@pytest.fixture
def mock_http_client(mocker):
    client = SimpleAsyncHTTPClient()
    client.queue = collections.deque()
    client.active = {}
    client.max_clients = 2
    client.waiting = set()
    mocker.patch.object(client, '_remove_timeout')
    mocker.patch.object(client, '_handle_request')
    return client

def test_process_queue_executes(mocker, mock_http_client):
    key = 'test_key'
    request = HTTPRequest(url='http://example.com')
    callback = MagicMock()
    
    mock_http_client.queue.append((key, request, callback))
    mock_http_client.waiting.add(key)
    
    mock_http_client._process_queue()
    
    assert key in mock_http_client.active
    mock_http_client._remove_timeout.assert_called_once_with(key)
    mock_http_client._handle_request.assert_called_once()
    assert mock_http_client._handle_request.call_args[0][0] == request
    assert callable(mock_http_client._handle_request.call_args[0][1])
    assert mock_http_client._handle_request.call_args[0][2] == callback
