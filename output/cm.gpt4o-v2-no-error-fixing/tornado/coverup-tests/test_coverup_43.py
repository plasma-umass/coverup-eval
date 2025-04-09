# file: tornado/httpclient.py:223-247
# asked: {"lines": [223, 236, 237, 238, 239, 240, 246, 247], "branches": [[236, 237], [236, 238], [239, 0], [239, 240], [246, 0], [246, 247]]}
# gained: {"lines": [223, 236, 237, 238, 239, 240, 246, 247], "branches": [[236, 237], [236, 238], [239, 0], [239, 240], [246, 0], [246, 247]]}

import pytest
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient

@pytest.fixture
def async_http_client():
    client = AsyncHTTPClient(force_instance=True)
    yield client
    client.close()

def test_async_http_client_close_not_closed(async_http_client):
    async_http_client._closed = False
    async_http_client._instance_cache = {async_http_client.io_loop: async_http_client}
    async_http_client.close()
    assert async_http_client._closed

def test_async_http_client_close_already_closed(async_http_client):
    async_http_client._closed = True
    async_http_client.close()
    assert async_http_client._closed

def test_async_http_client_close_with_instance_cache(async_http_client):
    async_http_client._closed = False
    other_client = AsyncHTTPClient(force_instance=True)
    async_http_client._instance_cache = {async_http_client.io_loop: other_client}
    with pytest.raises(RuntimeError, match="inconsistent AsyncHTTPClient cache"):
        async_http_client.close()

def test_async_http_client_close_no_instance_cache(async_http_client):
    async_http_client._closed = False
    async_http_client._instance_cache = None
    async_http_client.close()
    assert async_http_client._closed
