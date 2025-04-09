# file: tornado/simple_httpclient.py:192-200
# asked: {"lines": [192, 193, 194, 195, 196, 197, 198, 199, 200], "branches": [[193, 0], [193, 194], [195, 196], [195, 197]]}
# gained: {"lines": [192, 193, 194, 195, 197, 198, 199, 200], "branches": [[193, 0], [193, 194], [195, 197]]}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest, HTTPResponse
from unittest.mock import MagicMock, patch
from collections import deque

@pytest.fixture
def client():
    return SimpleAsyncHTTPClient()

def test_process_queue_executes_all_lines(client):
    # Mocking necessary attributes and methods
    client.queue = deque([
        ('key1', HTTPRequest(url='http://example.com'), MagicMock()),
        ('key2', HTTPRequest(url='http://example.com'), MagicMock())
    ])
    client.active = {}
    client.max_clients = 2
    client.waiting = {'key1', 'key2'}
    client._remove_timeout = MagicMock()
    client._handle_request = MagicMock()

    # Call the method
    client._process_queue()

    # Assertions to ensure all lines are executed
    assert client._remove_timeout.call_count == 2
    assert client._handle_request.call_count == 2
    assert 'key1' in client.active
    assert 'key2' in client.active

    # Clean up
    client.queue.clear()
    client.active.clear()
    client.waiting.clear()
