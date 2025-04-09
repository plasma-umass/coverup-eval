# file: tornado/netutil.py:339-363
# asked: {"lines": [339, 340, 363], "branches": []}
# gained: {"lines": [339, 340], "branches": []}

import pytest
import socket
from tornado.netutil import Resolver
from tornado.concurrent import Future

class TestResolver(Resolver):
    def resolve(self, host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC):
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
async def test_resolver_success(resolver):
    host = "localhost"
    port = 80
    family = socket.AF_INET
    result = await resolver.resolve(host, port, family)
    assert result == [(family, (host, port))]

@pytest.mark.asyncio
async def test_resolver_failure(resolver):
    host = "invalid"
    port = 80
    family = socket.AF_INET
    with pytest.raises(IOError, match="Cannot resolve address"):
        await resolver.resolve(host, port, family)
