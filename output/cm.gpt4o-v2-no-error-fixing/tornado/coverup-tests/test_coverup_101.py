# file: tornado/netutil.py:339-363
# asked: {"lines": [339, 340, 363], "branches": []}
# gained: {"lines": [339, 340], "branches": []}

import pytest
import socket
from tornado.netutil import Resolver
from tornado.util import Configurable
from typing import List, Any, Tuple, Awaitable

class TestResolver(Resolver):
    def resolve(self, host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC) -> Awaitable[List[Tuple[int, Any]]]:
        return super().resolve(host, port, family)

@pytest.mark.asyncio
async def test_resolver_resolve_not_implemented():
    resolver = TestResolver()
    with pytest.raises(NotImplementedError):
        await resolver.resolve("localhost", 80)
