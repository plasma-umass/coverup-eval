# file tornado/simple_httpclient.py:222-224
# lines [222, 223, 224]
# branches []

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest
from unittest.mock import MagicMock

@pytest.fixture
def mock_http_client(mocker):
    client = SimpleAsyncHTTPClient()
    client.active = {}
    client._process_queue = MagicMock()
    yield client
    client.close()

def test_release_fetch(mock_http_client):
    key = 'test_key'
    mock_http_client.active[key] = 'test_value'
    
    mock_http_client._release_fetch(key)
    
    assert key not in mock_http_client.active
    mock_http_client._process_queue.assert_called_once()
