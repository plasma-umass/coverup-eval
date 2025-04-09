# file: tornado/httpclient.py:314-336
# asked: {"lines": [336], "branches": []}
# gained: {"lines": [336], "branches": []}

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.testing import AsyncTestCase, gen_test

class TestAsyncHTTPClient(AsyncTestCase):
    @gen_test
    async def test_configure_with_class(self):
        # Ensure the default implementation is SimpleAsyncHTTPClient
        AsyncHTTPClient.configure(None)
        client = AsyncHTTPClient()
        assert isinstance(client, SimpleAsyncHTTPClient)

        # Reset to default
        AsyncHTTPClient.configure(None)
        client = AsyncHTTPClient()
        assert isinstance(client, SimpleAsyncHTTPClient)

    @gen_test
    async def test_configure_with_class_name(self):
        # Ensure the default implementation is SimpleAsyncHTTPClient
        AsyncHTTPClient.configure(None)
        client = AsyncHTTPClient()
        assert isinstance(client, SimpleAsyncHTTPClient)

        # Reset to default
        AsyncHTTPClient.configure(None)
        client = AsyncHTTPClient()
        assert isinstance(client, SimpleAsyncHTTPClient)

    @gen_test
    async def test_configure_with_kwargs(self):
        # Configure with additional kwargs
        AsyncHTTPClient.configure(SimpleAsyncHTTPClient, max_clients=10)
        client = AsyncHTTPClient()
        assert isinstance(client, SimpleAsyncHTTPClient)
        assert client.max_clients == 10

        # Reset to default
        AsyncHTTPClient.configure(None)
        client = AsyncHTTPClient()
        assert isinstance(client, SimpleAsyncHTTPClient)

    @gen_test
    async def test_configure_with_invalid_class_name(self):
        with pytest.raises(ImportError):
            AsyncHTTPClient.configure("nonexistent.module.NonExistentClass")

        # Reset to default
        AsyncHTTPClient.configure(None)
        client = AsyncHTTPClient()
        assert isinstance(client, SimpleAsyncHTTPClient)
