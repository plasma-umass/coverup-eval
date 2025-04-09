# file tornado/httpclient.py:140-180
# lines [140, 141, 179]
# branches []

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from unittest.mock import patch

@pytest.fixture
def reset_async_http_client():
    original_instance_cache = AsyncHTTPClient._instance_cache
    AsyncHTTPClient._instance_cache = None
    yield
    AsyncHTTPClient._instance_cache = original_instance_cache

@pytest.mark.asyncio
async def test_async_http_client_singleton_behavior(reset_async_http_client):
    with patch.object(IOLoop, 'current', return_value=IOLoop()):
        client1 = AsyncHTTPClient()
        client2 = AsyncHTTPClient()
        assert client1 is client2

@pytest.mark.asyncio
async def test_async_http_client_force_instance(reset_async_http_client):
    with patch.object(IOLoop, 'current', return_value=IOLoop()):
        client1 = AsyncHTTPClient(force_instance=True)
        client2 = AsyncHTTPClient(force_instance=True)
        assert client1 is not client2

@pytest.mark.asyncio
async def test_async_http_client_defaults(reset_async_http_client):
    defaults = {'user_agent': 'MyUserAgent'}
    AsyncHTTPClient.configure(None, defaults=defaults)
    client = AsyncHTTPClient(force_instance=True)
    assert client.defaults == defaults
