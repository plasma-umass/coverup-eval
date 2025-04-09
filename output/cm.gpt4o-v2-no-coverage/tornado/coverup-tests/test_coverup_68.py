# file: tornado/simple_httpclient.py:233-252
# asked: {"lines": [233, 241, 242, 244, 245, 246, 247, 248, 249, 251, 252], "branches": []}
# gained: {"lines": [233, 241, 242, 244, 245, 246, 247, 248, 249, 251, 252], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse, HTTPError
from tornado.ioloop import IOLoop
from tornado.simple_httpclient import SimpleAsyncHTTPClient

class HTTPTimeoutError(HTTPError):
    """Error raised by SimpleAsyncHTTPClient on timeout.

    For historical reasons, this is a subclass of `.HTTPClientError`
    which simulates a response code of 599.

    .. versionadded:: 5.1
    """

    def __init__(self, message: str) -> None:
        super().__init__(599, message=message)

    def __str__(self) -> str:
        return self.message

@pytest.fixture
def http_client(monkeypatch):
    client = SimpleAsyncHTTPClient()
    client.io_loop = IOLoop.current()
    client.waiting = {}
    client.queue = []
    monkeypatch.setattr(client, 'waiting', client.waiting)
    monkeypatch.setattr(client, 'queue', client.queue)
    return client

def test_on_timeout_with_info(http_client):
    request = HTTPRequest(url="http://example.com")
    callback = lambda response: None
    timeout_handle = object()
    key = object()
    info = "test_info"
    
    http_client.waiting[key] = (request, callback, timeout_handle)
    http_client.queue.append((key, request, callback))
    
    http_client._on_timeout(key, info)
    
    assert key not in http_client.waiting
    assert (key, request, callback) not in http_client.queue

def test_on_timeout_without_info(http_client):
    request = HTTPRequest(url="http://example.com")
    callback = lambda response: None
    timeout_handle = object()
    key = object()
    
    http_client.waiting[key] = (request, callback, timeout_handle)
    http_client.queue.append((key, request, callback))
    
    http_client._on_timeout(key)
    
    assert key not in http_client.waiting
    assert (key, request, callback) not in http_client.queue
