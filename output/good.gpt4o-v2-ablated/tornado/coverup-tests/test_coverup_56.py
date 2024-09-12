# file: tornado/httpclient.py:223-247
# asked: {"lines": [223, 236, 237, 238, 239, 240, 246, 247], "branches": [[236, 237], [236, 238], [239, 0], [239, 240], [246, 0], [246, 247]]}
# gained: {"lines": [223, 236, 237, 238, 239, 240, 246, 247], "branches": [[236, 237], [236, 238], [239, 0], [239, 240], [246, 0], [246, 247]]}

import pytest
from unittest import mock
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient

class TestAsyncHTTPClient:
    @pytest.fixture
    def client(self):
        client = AsyncHTTPClient(force_instance=True)
        yield client
        client.close()

    def test_close_not_closed(self, client):
        client._closed = False
        client._instance_cache = {client.io_loop: client}
        client.close()
        assert client._closed

    def test_close_already_closed(self, client):
        client._closed = True
        client.close()
        assert client._closed

    def test_close_instance_cache_none(self, client):
        client._closed = False
        client._instance_cache = None
        client.close()
        assert client._closed

    def test_close_inconsistent_cache(self, client):
        client._closed = False
        other_client = AsyncHTTPClient(force_instance=True)
        client._instance_cache = {client.io_loop: other_client}
        with pytest.raises(RuntimeError, match="inconsistent AsyncHTTPClient cache"):
            client.close()
        other_client.close()

    def test_close_cache_none_value(self, client):
        client._closed = False
        client._instance_cache = {client.io_loop: None}
        client.close()
        assert client._closed
