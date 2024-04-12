# file tornado/simple_httpclient.py:222-224
# lines [222, 223, 224]
# branches []

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from unittest.mock import Mock

@pytest.fixture
def http_client(mocker):
    client = SimpleAsyncHTTPClient()
    mocker.patch.object(client, '_process_queue')
    return client

def test_release_fetch(http_client):
    key = object()
    http_client.active[key] = None  # Simulate an active fetch

    assert key in http_client.active  # Precondition: key is in active dict

    http_client._release_fetch(key)

    assert key not in http_client.active  # Postcondition: key should be removed
    http_client._process_queue.assert_called_once()  # Postcondition: _process_queue should be called
