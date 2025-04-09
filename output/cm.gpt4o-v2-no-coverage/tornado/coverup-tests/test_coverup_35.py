# file: tornado/simple_httpclient.py:192-200
# asked: {"lines": [192, 193, 194, 195, 196, 197, 198, 199, 200], "branches": [[193, 0], [193, 194], [195, 196], [195, 197]]}
# gained: {"lines": [192, 193, 194, 195, 196, 197, 198, 199, 200], "branches": [[193, 0], [193, 194], [195, 196], [195, 197]]}

import pytest
from unittest.mock import MagicMock, call
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest, HTTPResponse
from collections import deque

@pytest.fixture
def client(monkeypatch):
    client = SimpleAsyncHTTPClient()
    client.queue = deque()
    client.active = {}
    client.waiting = {}
    client.max_clients = 2
    client.io_loop = MagicMock()
    client._connection_class = MagicMock(return_value=MagicMock())
    monkeypatch.setattr(client, '_remove_timeout', MagicMock())
    monkeypatch.setattr(client, '_release_fetch', MagicMock())
    monkeypatch.setattr(client, '_handle_request', MagicMock())
    return client

def test_process_queue_empty_queue(client):
    client._process_queue()
    assert not client._remove_timeout.called
    assert not client._handle_request.called

def test_process_queue_with_requests(client):
    request1 = HTTPRequest(url="http://example.com")
    request2 = HTTPRequest(url="http://example.org")
    callback = MagicMock()
    client.queue.append((1, request1, callback))
    client.queue.append((2, request2, callback))
    client.waiting = {1: (request1, callback, None), 2: (request2, callback, None)}

    client._process_queue()

    assert client._remove_timeout.call_count == 2
    assert client._handle_request.call_count == 2
    assert len(client.active) == 2
    assert client.active[1] == (request1, callback)
    assert client.active[2] == (request2, callback)

def test_process_queue_with_some_waiting(client):
    request1 = HTTPRequest(url="http://example.com")
    request2 = HTTPRequest(url="http://example.org")
    callback = MagicMock()
    client.queue.append((1, request1, callback))
    client.queue.append((2, request2, callback))
    client.waiting = {1: (request1, callback, None)}

    client._process_queue()

    assert client._remove_timeout.call_count == 1
    assert client._handle_request.call_count == 1
    assert len(client.active) == 1
    assert client.active[1] == (request1, callback)
    assert 2 not in client.active

def test_process_queue_releases_fetch(client):
    request1 = HTTPRequest(url="http://example.com")
    callback = MagicMock()
    client.queue.append((1, request1, callback))
    client.waiting = {1: (request1, callback, None)}

    client._process_queue()
    release_callback = client._handle_request.call_args[0][1]
    release_callback()

    assert client._release_fetch.called_once_with(1)
