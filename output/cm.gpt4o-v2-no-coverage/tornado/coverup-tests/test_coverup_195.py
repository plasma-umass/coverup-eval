# file: tornado/httpclient.py:198-214
# asked: {"lines": [205], "branches": [[204, 205]]}
# gained: {"lines": [205], "branches": [[204, 205]]}

import pytest
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient

class TestAsyncHTTPClient:
    
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, monkeypatch):
        # Setup: Create a fresh IOLoop and patch IOLoop.current to return it
        self.io_loop = IOLoop()
        monkeypatch.setattr(IOLoop, 'current', lambda: self.io_loop)
        
        # Teardown: Clear the instance cache
        yield
        if hasattr(AsyncHTTPClient, '_async_clients'):
            instance_cache = AsyncHTTPClient._async_clients()
            if self.io_loop in instance_cache:
                del instance_cache[self.io_loop]

    def test_force_instance_true(self):
        client = AsyncHTTPClient(force_instance=True)
        assert isinstance(client, AsyncHTTPClient)
        assert client._instance_cache is None

    def test_force_instance_false(self, monkeypatch):
        # Mock the _async_clients method to return a dictionary
        instance_cache = {}
        monkeypatch.setattr(AsyncHTTPClient, '_async_clients', lambda: instance_cache)
        
        client = AsyncHTTPClient(force_instance=False)
        assert isinstance(client, AsyncHTTPClient)
        assert client._instance_cache is instance_cache
        assert instance_cache[self.io_loop] is client

    def test_instance_reuse(self, monkeypatch):
        # Mock the _async_clients method to return a dictionary
        instance_cache = {}
        monkeypatch.setattr(AsyncHTTPClient, '_async_clients', lambda: instance_cache)
        
        client1 = AsyncHTTPClient(force_instance=False)
        client2 = AsyncHTTPClient(force_instance=False)
        
        assert client1 is client2
        assert instance_cache[self.io_loop] is client1
