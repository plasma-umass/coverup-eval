# file: tornado/simple_httpclient.py:226-231
# asked: {"lines": [226, 227, 228, 229, 230, 231], "branches": [[227, 0], [227, 228], [229, 230], [229, 231]]}
# gained: {"lines": [226, 227, 228, 229, 230, 231], "branches": [[227, 0], [227, 228], [229, 230], [229, 231]]}

import pytest
from unittest.mock import Mock, patch
from tornado.ioloop import IOLoop
from tornado.simple_httpclient import SimpleAsyncHTTPClient

@pytest.fixture
def client():
    io_loop = IOLoop.current()
    client = SimpleAsyncHTTPClient()
    client.io_loop = io_loop
    yield client
    io_loop.clear_current()
    io_loop.close(all_fds=True)

def test_remove_timeout_with_key_in_waiting(client):
    key = object()
    mock_request = Mock()
    mock_callback = Mock()
    mock_timeout_handle = Mock()
    
    client.waiting = {key: (mock_request, mock_callback, mock_timeout_handle)}
    client.io_loop.remove_timeout = Mock()

    client._remove_timeout(key)

    client.io_loop.remove_timeout.assert_called_once_with(mock_timeout_handle)
    assert key not in client.waiting

def test_remove_timeout_with_key_in_waiting_no_timeout_handle(client):
    key = object()
    mock_request = Mock()
    mock_callback = Mock()
    
    client.waiting = {key: (mock_request, mock_callback, None)}
    client.io_loop.remove_timeout = Mock()

    client._remove_timeout(key)

    client.io_loop.remove_timeout.assert_not_called()
    assert key not in client.waiting

def test_remove_timeout_with_key_not_in_waiting(client):
    key = object()
    client.waiting = {}
    client.io_loop.remove_timeout = Mock()

    client._remove_timeout(key)

    client.io_loop.remove_timeout.assert_not_called()
    assert key not in client.waiting
