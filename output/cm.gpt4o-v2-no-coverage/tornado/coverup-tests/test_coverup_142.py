# file: tornado/netutil.py:339-363
# asked: {"lines": [339, 340, 363], "branches": []}
# gained: {"lines": [339, 340], "branches": []}

import pytest
import socket
from tornado.netutil import Resolver
from tornado.concurrent import Future
from typing import List, Tuple, Awaitable, Any

class TestResolver(Resolver):
    def resolve(self, host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC) -> Awaitable[List[Tuple[int, Any]]]:
        future = Future()
        if host == "invalid":
            future.set_exception(IOError("Cannot resolve address"))
        else:
            future.set_result([(family, (host, port))])
        return future

@pytest.fixture
def resolver():
    return TestResolver()

@pytest.mark.asyncio
async def test_resolve_valid_host(resolver):
    host = "localhost"
    port = 80
    result = await resolver.resolve(host, port)
    assert result == [(socket.AF_UNSPEC, (host, port))]

@pytest.mark.asyncio
async def test_resolve_invalid_host(resolver):
    host = "invalid"
    port = 80
    with pytest.raises(IOError, match="Cannot resolve address"):
        await resolver.resolve(host, port)
