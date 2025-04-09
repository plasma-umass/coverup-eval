# file: tornado/simple_httpclient.py:192-200
# asked: {"lines": [192, 193, 194, 195, 196, 197, 198, 199, 200], "branches": [[193, 0], [193, 194], [195, 196], [195, 197]]}
# gained: {"lines": [192, 193, 194, 195, 196, 197, 198, 199, 200], "branches": [[193, 0], [193, 194], [195, 196], [195, 197]]}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest
from collections import deque
import functools

@pytest.fixture
def client(monkeypatch):
    client = SimpleAsyncHTTPClient()
    client.queue = deque()
    client.active = {}
    client.waiting = set()
    client.max_clients = 2

    def mock_remove_timeout(key):
        pass

    def mock_handle_request(request, release_callback, callback):
        pass

    monkeypatch.setattr(client, '_remove_timeout', mock_remove_timeout)
    monkeypatch.setattr(client, '_handle_request', mock_handle_request)
    return client

def test_process_queue_empty_queue(client):
    client._process_queue()
    assert len(client.active) == 0

def test_process_queue_with_requests(client):
    request1 = HTTPRequest("http://example.com")
    request2 = HTTPRequest("http://example.org")
    callback = lambda response: None

    client.queue.append((1, request1, callback))
    client.queue.append((2, request2, callback))
    client.waiting.add(1)
    client.waiting.add(2)

    client._process_queue()
    assert len(client.active) == 2
    assert 1 in client.active
    assert 2 in client.active

def test_process_queue_partial_requests(client):
    request1 = HTTPRequest("http://example.com")
    request2 = HTTPRequest("http://example.org")
    callback = lambda response: None

    client.queue.append((1, request1, callback))
    client.queue.append((2, request2, callback))
    client.waiting.add(1)

    client._process_queue()
    assert len(client.active) == 1
    assert 1 in client.active
    assert 2 not in client.active
