# file: tornado/httpclient.py:198-214
# asked: {"lines": [198, 199, 200, 201, 203, 204, 205, 206, 211, 212, 213, 214], "branches": [[200, 201], [200, 203], [204, 205], [204, 206], [212, 213], [212, 214]]}
# gained: {"lines": [198, 199, 200, 201, 203, 204, 205, 206, 211, 212, 213, 214], "branches": [[200, 201], [200, 203], [204, 205], [204, 206], [212, 213], [212, 214]]}

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

@pytest.fixture
def reset_ioloop():
    original_loop = IOLoop.current(instance=False)
    yield
    if original_loop:
        original_loop.make_current()
    else:
        IOLoop.clear_current()

def test_async_http_client_force_instance(reset_ioloop):
    client = AsyncHTTPClient(force_instance=True)
    assert isinstance(client, AsyncHTTPClient)
    assert client._instance_cache is None

def test_async_http_client_instance_cache(reset_ioloop):
    io_loop = IOLoop.current()
    client = AsyncHTTPClient()
    assert isinstance(client, AsyncHTTPClient)
    assert client._instance_cache is not None
    assert client._instance_cache[io_loop] is client

def test_async_http_client_reuse_instance(reset_ioloop):
    io_loop = IOLoop.current()
    client1 = AsyncHTTPClient()
    client2 = AsyncHTTPClient()
    assert client1 is client2
    assert client1._instance_cache[io_loop] is client1
    assert client2._instance_cache[io_loop] is client2
