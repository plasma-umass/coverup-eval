# file: tornado/simple_httpclient.py:205-220
# asked: {"lines": [205, 211, 212, 213, 214, 215, 216, 217, 218, 219], "branches": []}
# gained: {"lines": [205, 211, 212, 213, 214, 215, 216, 217, 218, 219], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.simple_httpclient import SimpleAsyncHTTPClient

class MockConnection:
    def __init__(self, client, request, release_callback, final_callback, max_buffer_size, tcp_client, max_header_size, max_body_size):
        self.client = client
        self.request = request
        self.release_callback = release_callback
        self.final_callback = final_callback
        self.max_buffer_size = max_buffer_size
        self.tcp_client = tcp_client
        self.max_header_size = max_header_size
        self.max_body_size = max_body_size
        self.start()

    def start(self):
        response = HTTPResponse(self.request, 200)
        self.final_callback(response)
        self.release_callback()

@pytest.fixture
def mock_connection_class(monkeypatch):
    monkeypatch.setattr(SimpleAsyncHTTPClient, "_connection_class", lambda self: MockConnection)

def test_handle_request(mock_connection_class):
    client = SimpleAsyncHTTPClient()
    request = HTTPRequest("http://example.com")
    release_callback_called = False
    final_callback_called = False

    def release_callback():
        nonlocal release_callback_called
        release_callback_called = True

    def final_callback(response):
        nonlocal final_callback_called
        final_callback_called = True
        assert response.code == 200

    client._handle_request(request, release_callback, final_callback)

    assert release_callback_called
    assert final_callback_called
