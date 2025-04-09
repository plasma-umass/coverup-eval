# file: tornado/simple_httpclient.py:192-200
# asked: {"lines": [196], "branches": [[195, 196]]}
# gained: {"lines": [196], "branches": [[195, 196]]}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest
from unittest.mock import MagicMock

@pytest.fixture
def client():
    return SimpleAsyncHTTPClient()

def test_process_queue(client, monkeypatch):
    # Mocking the necessary attributes and methods
    client.queue = MagicMock()
    client.queue.popleft = MagicMock(return_value=('key', HTTPRequest(url='http://example.com'), lambda x: x))
    client.queue.__bool__ = MagicMock(side_effect=[True, False])
    client.active = {}
    client.max_clients = 10
    client.waiting = set()

    # Mocking _remove_timeout to ensure it is not called
    client._remove_timeout = MagicMock()

    # Call the method
    client._process_queue()

    # Assertions
    client.queue.popleft.assert_called_once()
    client._remove_timeout.assert_not_called()
    assert 'key' not in client.active
